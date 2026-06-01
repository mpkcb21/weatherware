# Weatherware
Sometimes you look outside, and it's sunny, so you dress according to the sun, but once you go outside, it's really cold, and you regret not bringing a jacket, or
in the opposite case its really cold when you leave the house, and a couple of hours later, you find yourself sweating because the temperature changed so quickly. 
Weatherware is the solution for that. You just use Weatherware on your computer, and it suggests to you what to wear for the day and to dress accordingly, in some cases
it even gives you a UV warning to remind you to wear sunscreen and take care of your skin. Weatherware is a convenient way to easily choose what to wear and feel comfortable
for the whole day without having to think about it or spend time planning what to wear. 

## Installation

```bash
uv add "git+https://github.com/mpkcb21/weatherware.git"
```

## Usage

```bash
weatherware 
```

Basic usage:
```bash
weatherware "San Diego"
weatherware "New York"
weatherware Chicago
```

If you run cold, use `--cold-bias` to shift recommendations warmer:
```bash
weatherware "San Francisco" --cold-bias
```

Show full weather stats alongside the recommendation:
```bash
weatherware "Boston" --raw
```

## Example Output

```
  📍 San Diego, California, United States
  Partly cloudy · 62°F (feels like 51°F)

  ⚠️  Deceptive: actual 62°F but feels like 51°F (wind chill of 11°F) — dress warmer than it looks.
  💨 Windy (22 mph, gusts up to 35 mph) — avoid loose layers.
  🌡️  Big temp swing today (48°F → 72°F feels-like) — dress in layers you can remove.

  What to wear:
  Top:           sweater or fleece
  Bottom:        jeans or heavier trousers
  Outer layer:   medium jacket or hoodie
  Accessories:   sunglasses
```
