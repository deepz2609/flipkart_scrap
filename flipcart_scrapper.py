import requests
from bs4 import BeautifulSoup

try:
    url=input("Enter the url: ")
    req=requests.get(url)
    soup=BeautifulSoup(req.content ,"html.parser")
    product_name=soup.find("span", class_="B_NuCI")
    product_ratings = soup.find("div", class_="_3LWZlK")
    price = soup.find("div", class_="_30jeq3 _16Jk6d")

    print("\nName of the product: ",product_name.text)
    print(f"Ratings {product_ratings.text}*")
    print("Price: ",price.text)
except Exception as e:
    print(e)