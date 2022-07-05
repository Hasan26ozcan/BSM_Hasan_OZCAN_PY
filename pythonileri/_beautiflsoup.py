html_doc="""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ilk web sayfama</title>
</head>
<body>
    <h1>
        sayfama ilk yazım
    </h1>
    <!--...sayfada bulunan bütün tasarım aslında body içerisinde yer alıyor
    -->
    <div class ="grup 1">
    <h2>baslık 1</h2>
    <ul>
        <li>Menu 1</li>



        <li>Menu 2</li>
        <li>Menu 3</li>
        <li>Menu 4</li>
    </ul>
    </div>
    <div class ="grup 2">
        <h2>baslık 2</h2>
        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
            <li>Menu 4</li>
        </ul>
        </div>
    <div class ="grup 3">
    <h2>baslık 1</h2>
    <ul>
        <li>Menu 1</li>
        <li>Menu 2</li>
        <li>Menu 3</li>
        <li>Menu 4</li>
    </ul>
    </div>
    <img src="htmlimg.png" alt="htmlimg">
</body>
</html>
<a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
<a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
<a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>

"""





from bs4 import BeautifulSoup

soup= BeautifulSoup(html_doc,"html.parser")

result=soup.prettify()# düzgün bir şekilde yazdırmamızı saglıyor
print(result)
result=soup.title#böyle ise sadece title bilgisini getiriyor
print(result)
result=soup.head
print(result)
result=soup.body
print(result)
result=soup.title.name
print(result)
result=soup.title.string
print(result)
result=soup.h1
print(result)
result=soup.h2
print(result)
result=soup.h2.name
print(result)
result=soup.h2.string
print(result)
result=soup.h1.string
print(result)
print("**"*50)
result=soup.find_all("h2")
print(result)
result=soup.find_all("h2")[0]
print(result)
result=soup.find_all("h2")[1]
print(result)

result=soup.div
print(result)

result=soup.find_all("div")[0].ul.find_all("li")[1]
print(result)
print("//"*50)
result=soup.div.findChildren
print(result)

result=soup.div.find_next_sibling().find_next_sibling().find_previous_sibling()# bir ilerisine gitti ve bu sayede nextini alma islemi basarıyla gerceklesti
print(result)

result=soup.div.find_previous_sibling()
print(result)

result=soup.find_all("a")
print(result)
print(result[0])
for i in result:
    print(i.get("class"))

