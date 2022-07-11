from twitterUserinfo import username,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class twitter:
    def __init__(self,username,password):
        self.browserprofile=webdriver.ChromeOptions()
        self.browserprofile.add_experimental_option("prefs",{'intl.accept_languages':'en,en_US'} )
        # burda verdiğimiz işlemin ingilizce olmasını saglıyoruz



        self.bassword=webdriver.Chrome(chrome_options=self.browserprofile)
        self.username=username
        self.password=password
    
    def login(self):
        self.bassword.get("https://twitter.com/login")
        time.sleep(5)
        file=self.bassword.find_element(By.NAME,"text")
        file.send_keys(self.username)
        file.send_keys(Keys.ENTER)
        time.sleep(2)

        files=self.bassword.find_element(By.NAME,"password")
        files.send_keys(self.password)
        files.send_keys(Keys.ENTER)
        time.sleep(5)
    def search(self,hashtag):
        # o hastag de en öndeki olan şeyi bize veriyor ordaki en baştaki şeyi
        self.bassword.get("https://twitter.com/explore")
        time.sleep(3)
        aratme=self.bassword.find_element(By.CSS_SELECTOR,"input[role='combobox']")
        aratme.send_keys(hashtag)
        aratme.send_keys(Keys.ENTER)
        time.sleep(3)
        liste=self.bassword.find_element(By.CSS_SELECTOR,"div[aria-label='Timeline: Search timeline']").find_elements(By.CSS_SELECTOR,"div[data-testid='cellInnerDiv']")
        result=[]
        print(len(liste))
        for newsite in liste:
            listemiz=""
            newliste=newsite.find_element(By.CSS_SELECTOR,"div[data-testid='tweetText']" ).find_elements(By.TAG_NAME,"span")
            for i in newliste:
                listemiz+=i.text
            result.append(listemiz)


        counter=0
        lasth_heigth=self.bassword.execute_script("return document.documentElement.scrollHeight")
        while True:
            if(counter>3):
                break
            self.bassword.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(4)
            new_height=self.bassword.execute_script("return document.documentElement.scrollHeight")
            if (new_height !=lasth_heigth):
                lasth_heigth=new_height
                liste=self.bassword.find_element(By.CSS_SELECTOR,"div[aria-label='Timeline: Search timeline']").find_elements(By.CSS_SELECTOR,"div[data-testid='cellInnerDiv']")
                print(len(liste))
                for newsite in liste:
                    listemiz=""
                    newliste=newsite.find_element(By.CSS_SELECTOR,"div[data-testid='tweetText']" ).find_elements(By.TAG_NAME,"span")
                    for i in newliste:
                        listemiz+=i.text
                    listemiz.replace("  "," ")
                    result.append(listemiz)
                # aslında burda screanwrite en alta koyupta yapabilirdik ama şöyle birşey var bizim aldığımız 
                #sayfa yenilendikten sonra onu farklı bir yerde öncekileri farklı yerde daha öncekileri daha farklı yerde 
                #tutuyor bu durumda ise yapmamız gerekn şey hepisini aldığı gibi yazdırma olabilir ya da elemts de divin başlangıc 
                #noktasından itibaren farklı bir değer atarak yapabiliriz şunun gibi

                #liste=self.bassword.find_elements(By.CSS_SELECTOR,"div[aria-label='Timeline: Search timeline']")

                #bu sistem sayesinde sistemin sistemesi önleniyor 
                #biz en son nereye geldiysek sadece ordaki tweetler ekrana yazdırılıyor

            else:
                break
            counter+=1
        counsayma=1
        for i in result:
            print(f"{counsayma} {i} ")
            print("**"*50)
            counsayma+=1
        counters=1
        with open("twitter #python.txt","w",encoding="UTF-8") as file :
            for i in result:
                file.write(f" {counters}-)   { str(i)}\n")
                counters+=1


        # for newsite in liste:
        #     listemiz=""
        #     newliste=newsite.find_element(By.CSS_SELECTOR,"div[data-testid='tweetText']" ).find_elements(By.TAG_NAME,"span")
        #     for i in newliste:
        #         listemiz+=i.text
        # print(listemiz)






        





        





twiter=twitter(username,password)


twiter.login()
twiter.search("#python")