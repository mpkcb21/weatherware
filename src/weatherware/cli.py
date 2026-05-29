"""Weatherware CLI — what should I wear today?"""

import click
import requests

from .weather import get_weather, describe_weather
from .recommend import recommend


def _fmt_section(label: str, value: str) -> str:
    return f"  {label:<14} {value}"


@click.command()
@click.argument("city", nargs=-1, required=True)
@click.option(
    "--cold-bias",
    is_flag=True,
    default=False,
    help="You run cold — shifts recommendations warmer.",
)
@click.option(
    "--raw",
    is_flag=True,
    default=False,
    help="Also print raw weather stats.",
)
def main(city: tuple[str, ...], cold_bias: bool, raw: bool) -> None:
    """What should I wear today?

    CITY is the city name, e.g. "San Diego" or "New York".
    """
    city_str = " ".join(city)

    try:
        weather, location = get_weather(city_str)
    except ValueError as e:
        raise click.ClickException(str(e))
    except requests.RequestException as e:
        raise click.ClickException(f"Network error: {e}")

    outfit = recommend(weather, cold_bias=cold_bias)
    condition = describe_weather(weather["weather_code"])

    click.echo()
    click.secho(f"  📍 {location}", bold=True)
    click.echo(
        f"  {condition.capitalize()} · "
        f"{weather['temp_f']:.0f}°F (feels like {weather['feels_like_f']:.0f}°F)"
    )
    click.echo()

    if outfit.warnings:
        for w in outfit.warnings:
            click.secho(f"  {w}", fg="yellow")
        click.echo()

    click.secho("  What to wear:", bold=True)
    click.echo(_fmt_section("Top:", outfit.top))
    click.echo(_fmt_section("Bottom:", outfit.bottom))
    click.echo(_fmt_section("Outer layer:", outfit.outer))

    if outfit.accessories:
        acc_str = ", ".join(outfit.accessories)
        click.echo(_fmt_section("Accessories:", acc_str))

    if raw:
        click.echo()
        click.secho("  Weather details:", bold=True)
        click.echo(_fmt_section("Wind:", f"{weather['wind_mph']:.0f} mph (gusts {weather['wind_gusts_mph']:.0f} mph)"))
        click.echo(_fmt_section("Humidity:", f"{weather['humidity_pct']:.0f}%"))
        click.echo(_fmt_section("UV index:", f"{weather['uv_index']:.0f}"))
        click.echo(_fmt_section("Rain chance:", f"{weather['max_precip_prob_pct']:.0f}% (today's max)"))
        click.echo(_fmt_section("Day range:", f"{weather['day_feels_min_f']:.0f}°F – {weather['day_feels_max_f']:.0f}°F feels-like"))

    click.echo()