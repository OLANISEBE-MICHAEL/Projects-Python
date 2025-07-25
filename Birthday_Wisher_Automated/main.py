import pandas as pd
import datetime as dt
import random
import smtplib

now = dt.datetime.now().date()# obtaining all time categories at this instant
current_date = (now.month, now.day) # getting the current date of today
birthdays_df = pd.read_csv("birthdays.csv")
birthday_message = ""
celebrant_email = ""

def get_birthday_message(name):
    """this picks a random letter to send based on the participant's birthday"""
    letter_to_send = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter_to_send) as lt:
        birthday_letter = lt.read()
        birthday_letter = birthday_letter.replace("[NAME]", name)
        return birthday_letter


def send_email(message, email):
    """this sends a birthday message via email if today is your birthday"""
    my_email = "olanisebemichael633@gmail.com"
    password = "ntnkwkfdgefxdpza"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user= my_email, password= password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs= email,
            msg= f"Subject: Happy Birthday Message\n\n{message}"
        )

# looping through my dataframe of all dob to find out their birthday
for index, row in birthdays_df.iterrows():
    date_of_birth = dt.datetime(year= row.year, month= row.month, day= row.day).date()
    birthday = (date_of_birth.month, date_of_birth.day)
    if birthday == current_date: # Happy birthday!
        birthday_message = get_birthday_message(row["name"])
        celebrant_email = row.email
        send_email(birthday_message, celebrant_email)
