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
Paste that into your README.md, commit as "update README with correct install URL", and push.You said: uv add "git+https://github.uv add "git+https://github.com/mpkcb21/weatherware.git" is this for everyone or does everyone use their own user nameClaude responded: That URL is specific to your repo — it's your code on your GitHub account.That URL is specific to your repo — it's your code on your GitHub account. Anyone can install it with that exact command since the repo is public. That's the whole point — you share that URL and anyone can install your tool.You said: do you need the bash commanddo you need the bash commandClaude responded: No, you just need the URL.No, you just need the URL. Submit https://github.com/mpkcb21/weatherware on Gradescope and you're done.You said: no like in the instructions why do you keep putting bash iin front of everythingno like in the instructions why do you keep putting bash iin front of everythingClaude responded: That's just markdown formatting — it tells GitHub to syntax-highlight the code block as a terminal command.That's just markdown formatting — it tells GitHub to syntax-highlight the code block as a terminal command. It doesn't affect anything, it's just for readability. The grader won't care.
