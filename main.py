import smtplib

from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
my_email="nalindummy1@gmail.com"
password="jcyrujpuarikiqoy"


web_url="https://www.amazon.in/Beats-Studio3-Wireless-Over%E2%80%91Ear-Headphones/dp/B08529DT8N/ref=sr_1_1?crid=CN6FUUN0G3VJ&keywords=headphone%2Bbeat&qid=1700887944&sprefix=headohine%2Bbeat%2Caps%2C236&sr=8-1&th=1"
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
         "Accept-Language":"en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7,hi;q=0.6","Cookie": "PHPSESSID=47e2398401cd9cffc1f90fab80454909"}
response=requests.get(url=web_url,headers=header)
data=response.text
soup=BeautifulSoup(data,"lxml")

price_whole = str(soup.select_one("span.a-price-whole")).split(">")[1].split("<")[0]
#price_fraction = str(soup.select_one("span.a-price-fraction")).split(">")[1].split("<")[0]
price = f"{price_whole}"
price=int(str(price).replace(",",""))
if price<25000:
    msg=f'''Subject: Amazon Price alert!!
              price of your product is now {price}  '''

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="nalinsharma201@gmail.com",msg=msg)
