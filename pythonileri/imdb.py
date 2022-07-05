from msilib.schema import tables
from random import betavariate
from bs4 import BeautifulSoup
import requests

from bs4 import BeautifulSoup




url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"

screan=requests.get(url)
content=screan.content


soup= BeautifulSoup(content,"html.parser")
#print(soup.prettify())
print("**"*50)
body=soup.find("tbody",{"class":"lister-list"}) #özellikle bunu getirmesini istiyoruz
listesi= body.find_all("tr")

#print(listesi)
# bu ikisi aynı şey üsteki benim alttaki hocanın yaptığı hangisi istersek oan göre kullanabiliriz
print(listesi[0].find("td",{"class":"posterColumn"}).find("a").find("img").get("alt"))
print(listesi[0].find("td",{"class":"titleColumn"}).find("a").text)
counter=1
for i in listesi:
    moviename= (i.find("td",{"class":"posterColumn"}).find("a").find("img").get("alt"))
    movieyear=(i.find("td",{"class":"titleColumn"}).find("span").text)
    movieraiting=(i.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text)
    print(f"{counter}. film adı={moviename.ljust(68)} film yılı={movieyear} film raiting= {movieraiting}")
    counter+=1








