import requests

from bs4 import BeautifulSoup



url="https://www.n11.com/bilgisayar/dizustu-bilgisayar"


url1= requests.get(url)
url1=url1.content

soup=BeautifulSoup(url1,"html.parser")
print(soup)
print("***"*50)
listesi=(soup.find("ul",{"class":"list-ul"}).find_all("li"))
print(listesi[1].find("span",{"class":"oldPrice cPoint priceEventClick"}).find("del").text)
for i in listesi:
    computername=(i.find("span",{"class":"newPrice cPoint priceEventClick"}).get("title"))
    computerprice=(i.find("span",{"class":"newPrice cPoint priceEventClick"}).find("ins").text)
    computercargo=i.find("div",{"class":"cargoBadgeField"}).find("span",{"class":"cargoBadgeText"}).text
    computerlink=i.find("div",{"class":"pro"}).find("a",{"class":"plink"}).get("href")
    print(computername.ljust(120),computerprice.ljust(15),computercargo,)
    print(computerlink)
