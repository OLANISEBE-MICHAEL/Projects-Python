📈 4. Stock Market & News Alert System
# Stock Market & News Alert System

A stock monitoring tool for Tesla Inc. (TSLA) that checks daily stock price changes using Alpha Vantage. If the price changes more than ±4%, it fetches related news articles and sends email alerts.

## Features

- Fetches daily stock price data from Alpha Vantage API
- Calculates percentage change between two recent trading days
- If movement ≥ ±4%, fetches top 3 relevant news from NewsAPI
- Sends email alerts with article titles and descriptions

## Technologies

- Python
- Requests
- Alpha Vantage API
- NewsAPI
- SMTP Email

## Requirements

- Environment variables:
  - `STOCK_API_KEY` – Alpha Vantage API key
  - `NEWS_API_KEY` – NewsAPI key
- Email setup (email address, app password)

## How to Run

```bash
python stock_news_alert.py
