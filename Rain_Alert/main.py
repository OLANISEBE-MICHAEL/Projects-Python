import requests
import smtplib

def send_email():
    my_email = "olanisebemichael633@gmail.com"
    my_password = "ntnkwkfdgefxdpza"
    recipient_email = "olanisebemichael@yahoo.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg="Subject:Weather Update\n\nIt's likely it rains today. Don't forget to bring an Umbralla"
        )

# getting the weather data from the open weather api
api_key = "27b38f30275fdca8c7bf598684861455"
parameters = {
    "lat" : 6.528490,
    "lon" : 3.355320,
    "appid" : api_key,
    "cnt" : 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False
weather_id = [x["weather"][0]["id"] for x in weather_data["list"]] # getting the list of  weather codes for the next 12 hrs

for id in weather_id:
    if int(id) < 700:
        will_rain = True

if will_rain:
  send_email()