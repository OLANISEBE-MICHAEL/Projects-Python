# Cookie Clicker Bot

An automation bot built using SeleniumBase to play the online game [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/). The bot clicks the big cookie continuously and buys available upgrades automatically for 5 minutes.

## Features

- Uses undetected Chrome automation via SeleniumBase
- Automatically selects language and waits for page elements
- Clicks the big cookie and purchases upgrades when available
- Tracks cookie count and prints the final result

## Technologies

- Python
- SeleniumBase
- WebDriverWait & expected_conditions

## How to Run

```bash
pip install seleniumbase
python cookie_clicker_bot.py
