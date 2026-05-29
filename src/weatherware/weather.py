"""Fetch weather data from Open-Meteo (no API key required)."""

import requests


GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


def geocode(city: str) -> tuple[float, float, str]:
    """Return (lat, lon, resolved_name) for a city string."""
    resp = requests.get(GEOCODE_URL, params={"name": city, "count": 1}, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    if not data.get("results"):
        raise ValueError(f"Could not find location: '{city}'")
    r = data["results"][0]
    name = f"{r['name']}, {r.get('admin1', '')}, {r.get('country', '')}".strip(", ")
    return r["latitude"], r["longitude"], name


def fetch_weather(lat: float, lon: float) -> dict:
    """Fetch current + hourly weather for today."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": [
            "temperature_2m",
            "apparent_temperature",
            "relative_humidity_2m",
            "precipitation",
            "weather_code",
            "wind_speed_10m",
            "wind_gusts_10m",
            "uv_index",
            "is_day",
        ],
        "hourly": [
            "temperature_2m",
            "apparent_temperature",
            "precipitation_probability",
        ],
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
        "forecast_days": 1,
        "timezone": "auto",
    }
    resp = requests.get(FORECAST_URL, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    current = data["current"]
    hourly = data["hourly"]

    apparent_temps = hourly["apparent_temperature"]
    precip_probs = hourly["precipitation_probability"]

    return {
        "temp_f": current["temperature_2m"],
        "feels_like_f": current["apparent_temperature"],
        "humidity_pct": current["relative_humidity_2m"],
        "precipitation_in": current["precipitation"],
        "weather_code": current["weather_code"],
        "wind_mph": current["wind_speed_10m"],
        "wind_gusts_mph": current["wind_gusts_10m"],
        "uv_index": current["uv_index"],
        "is_day": current["is_day"],
        "day_feels_min_f": min(apparent_temps),
        "day_feels_max_f": max(apparent_temps),
        "max_precip_prob_pct": max(precip_probs) if precip_probs else 0,
    }


def get_weather(city: str) -> tuple[dict, str]:
    """Geocode city, fetch weather. Returns (weather_dict, resolved_name)."""
    lat, lon, name = geocode(city)
    weather = fetch_weather(lat, lon)
    return weather, name


WMO_CODES = {
    0: "clear sky",
    1: "mainly clear", 2: "partly cloudy", 3: "overcast",
    45: "fog", 48: "icy fog",
    51: "light drizzle", 53: "drizzle", 55: "heavy drizzle",
    61: "light rain", 63: "rain", 65: "heavy rain",
    71: "light snow", 73: "snow", 75: "heavy snow",
    77: "snow grains",
    80: "light showers", 81: "showers", 82: "heavy showers",
    85: "snow showers", 86: "heavy snow showers",
    95: "thunderstorm", 96: "thunderstorm with hail", 99: "thunderstorm with heavy hail",
}


def describe_weather(code: int) -> str:
    return WMO_CODES.get(code, "unknown conditions")