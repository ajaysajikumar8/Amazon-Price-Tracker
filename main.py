import requests
import lxml
from bs4 import BeautifulSoup
from twilio.rest import Client

account_sid = ""
auth_token = ""
twilio_num = ""
my_num = ""

URL = r"https://www.amazon.in/Apple-iPhone-13-256GB-Blue/"
headers = {
    "User-Agent": "your-user-agent",
    "Accept-Language": "your-accept-language"
}

response = requests.get(url=URL, headers=headers)
website = response.content

soup = BeautifulSoup(website, "lxml")

raw_price = soup.find(name="span", class_="a-price-whole")
unwanted = raw_price.find(name="span", class_="a-price-decimal")
unwanted.extract()

price = float(raw_price.get_text().replace(",", ""))


target_price = 80000
product_title = soup.find(name="span", id="productTitle").get_text().strip()

client = Client(account_sid, auth_token)
if price < target_price:
    text = f"{product_title} is now available at ₹{price}\n{URL}"

    message = client.messages \
        .create(
            body= text,
            from_= twilio_num,
            to=my_num
        )
