import os
import requests
import smtplib
from email.message import EmailMessage

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key_stock = os.environ.get("STOCK_API_KEY")
api_key_news = os.environ.get("NEWS_API_KEY")
my_email = "olanisebemichael633@gmail.com"
recipient_email = "olanisebemichael@yahoo.com"
my_password = "ntnkwkfdgefxdpza"

def send_news(market_status):
    """this gets the news based on the company name and sends an  email"""
    parameters_news = {
        "q": f"+{COMPANY_NAME}",
        "to": yesterday,
        "from": previous_day,
        "sortBy": "relevancy",
        "language": "en",
        "apiKey": api_key_news
    }
    response_news = requests.get("https://newsapi.org/v2/everything", params=parameters_news)
    response_news.raise_for_status()
    full_news = response_news.json()
    sub_news_dict = {
        "title" : [], # the dict the first 3 relevant new from the news api
        "description" : []
    }
    for x in range(3):
        sub_news_dict["title"].append(full_news["articles"][x]["title"])
        sub_news_dict["description"].append(full_news["articles"][x]["description"])

    # sending the email
    for x in range(3):
        msg = EmailMessage()
        msg["Subject"] = f"{sub_news_dict["title"][x]} {market_status}"
        msg["From"] = my_email
        msg["To"] = recipient_email
        msg.set_content(f"Title:{sub_news_dict["title"][x]}\n\nArticle:{sub_news_dict["description"][x]}.")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.send_message(msg)

# getting the data for the stock prices from the api
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": api_key_stock
}
response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
stock_prices_tsla = response.json()

# extracting the price of the stock for yesterday and the previous day from the data.json
list_of_dates = list(stock_prices_tsla["Time Series (Daily)"].keys()) # gets all the dates of trading that stock
yesterday = list_of_dates[0] # returns yesterday's date
yesterday_closing_price = stock_prices_tsla["Time Series (Daily)"][yesterday]["4. close"]
previous_day = list_of_dates[1] # returns the day before yesterday
previous_day_closing_price = stock_prices_tsla["Time Series (Daily)"][previous_day]["4. close"]

# calculating the percentage change in price between yesterday and the previous day
change_in_price = float(yesterday_closing_price) - float(previous_day_closing_price)
percentage_change =  round(change_in_price / float(previous_day_closing_price) * 100, 2)

# determining whether the stock went up, down or no change
if percentage_change >= 4.0:
    status = f"The market for {STOCK} went up by {percentage_change}%⬆️"
    send_news(status)
elif percentage_change <= -4.0:
    status = f"The market for {STOCK} went down ⬇️"
    send_news(status)
else:
    status = f"The market for {STOCK} had no change⚖️"
    send_news(status)

