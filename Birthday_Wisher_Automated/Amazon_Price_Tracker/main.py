from bs4 import BeautifulSoup
import requests
import smtplib
import os

def send_email():
    my_email = "olanisebemichael633@gmail.com"
    # my_password = os.environ.get("app_password")
    my_password = "sargmqqbygturchg"
    recipient_email = "olanisebemichael@yahoo.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject: Amazon price tracker\n\nThe pressure cooker is now {price}. Which meets up to your budget"
        )



URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 "
                  "Safari/537.36 Edg/138.0.0.0",

}
response = requests.get(URL, headers=header)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")
price_without_symbol = soup.find(class_="a-offscreen").get_text().split("$")[1]
product_title = soup.find(id="productTitle").get_text(strip=True)
price = float(price_without_symbol)
print(price)
print(product_title)

if price < 100:
    send_email()

