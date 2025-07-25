import requests
import datetime as dt
import smtplib
import time

MY_LAT = 6.524379
MY_LONG = 3.379206
my_email = "olanisebemichael633@gmail.com"
password = "ntnkwkfdgefxdpza"
recipient_email = "olanisebemichael@yahoo.com"

def is_iss_overhead():
    """this checks if the iss is overhead me in my location"""
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json() # reads the data
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    # if the satellite is the range +/- 5
    if (MY_LAT - 5) <= latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= longitude <= (MY_LONG + 5):
        return True
    return ""

def send_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user= my_email, password= password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs= recipient_email,
            msg= "Subject:ISS Message\n\nLook up there is a satellite"
        )

def is_night():
    """checks if the current hour is in the night time"""
    # get the time of sunset and sunrise
    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LONG,
        "formatted" : 0
    }
    response_2 = requests.get("https://api.sunrise-sunset.org/json", params= parameters)
    response_2.raise_for_status()
    data_2 = response_2.json()
    sunrise = int(data_2["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_2["results"]["sunset"].split("T")[1].split(":")[0])
    hour_now = dt.datetime.now().hour

    if hour_now >= sunset or hour_now <= sunrise:
        return True
    return  ""

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        send_email()

