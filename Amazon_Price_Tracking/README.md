

markdown
# Amazon Price Tracker

A web scraping tool that monitors the price of a product on Amazon and sends an email alert when the price drops below a target value.

## Features

- Scrapes Amazon product price and title using BeautifulSoup
- Sends email alerts via SMTP when the price is right
- Makes use of custom headers to mimic a real browser

## Technologies

- Python
- BeautifulSoup
- Requests
- smtplib (email sending)

## How to Use

1. Set your `my_email`, `my_password`, and `recipient_email`.
2. Update the product URL and price threshold.
3. Run the script:

bash
python amazon_tracker.py
