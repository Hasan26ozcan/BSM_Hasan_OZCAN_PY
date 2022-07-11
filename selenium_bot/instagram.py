from hashlib import new
from itertools import count
from tkinter import Button, dialog
from turtle import pen
from attr import s
from instagramusername import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Intagram:
    def __init__(self,username,password):
        self.browser=webdriver.Chrome()
        self.username=username
        self.password=password
        self.fallowerlist=[]

    def sıgnın(self):    
        self.browser.get("https://www.instagram.com/accounts/login/?")
        time.sleep(5)
        username = self.browser.find_element(By.NAME,'username')
        username.send_keys(self.username)
        loginpassword=self.browser.find_element(By.NAME,'password')
        loginpassword.send_keys(self.password)
        loginpassword.send_keys(Keys.ENTER)
        time.sleep(5)

    def gettakipçiliste(self):
        self.browser.get(f"https://www.instagram.com/therock/")
        time.sleep(5)
        takipbuton=self.browser.find_element(By.TAG_NAME,"ul")
        buttons=takipbuton.find_element(By.TAG_NAME,"a")
        buttons.send_keys(Keys.ENTER)
        time.sleep(5)

        takipçi=self.browser.find_element(By.CSS_SELECTOR,"div[role=dialog]").find_element(By.TAG_NAME,"ul")
        # burdaki en önemli  şeylerden bir tanesi hangi css selector kullanılması onun içinde 
        #burdaki siteme dikkat etmemiz gerekiyor
        fallowercount=len(takipçi.find_elements(By.TAG_NAME,"li"))

        print(f"first count {fallowercount} ")

        action =webdriver.ActionChains(self.browser)
        while True:
            takipçi.click()
            for i in range(0,8):
                action.key_down(Keys.SPACE).perform()# bu tuş durumunu aktif hale getiriyor
                time.sleep(2)

            time.sleep(5)


            newcount=len(takipçi.find_elements(By.TAG_NAME,"li"))

            if(newcount!=fallowercount):
                fallowercount=newcount
                print(newcount)
                time.sleep(1)
            else:
                break
        fallower=takipçi.find_elements(By.TAG_NAME,"li")


        
        for i in fallower:
            print(i.find_element(By.TAG_NAME,"a").get_attribute("href"))
        # print(f"firt count {fallowercount} ")
        # action=webdriver.ActionChains(self.browser)
        # while True:
        #     action.click()
        #     action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()# bu sayede o yerde space tuşuna basmamızı sağlıyor

        #     newcount=len(takipçi.find_elements(By.TAG_NAME,"li"))
        #     if(newcount != fallowercount):
        #         fallowercount=newcount
        #         print(f"new count {newcount} ")

        #     else:
        #         break
        # fallowers=takipçi.find_elements(By.TAG_NAME,"li")


        # for i in fallowers:
        #     self.fallowerlist.append(i.find_element(By.CLASS_NAME,"_aacl _aaco _aacw _aacx _aad7 _aade").text)

        # with open("fallowerlist.txt","w",encoding="UTF-8") as file:
        #     for i in self.fallowerlist:
        #         file.write(i)



    def followUser(self,username):
        self.browserservice=webdriver.ChromeOptions()
        self.browserservice.add_experimental_option("prefs",{'intl.accept_languages':"en,en_US"})
        self.browser=webdriver.Chrome("chromedriver.exe",chrome_options=self.browserservice)
# biz bu kısımda onun dilini değiştirdik ve açılan tarayıcının dilinin ingilizce olmasını sağladık

        self.browser.get(f"https://www.instagram.com/{username}/")
        time.sleep(4)
        hareket=self.browser.find_element(By.CSS_SELECTOR,"main[role='main']").find_element(By.CSS_SELECTOR,"button[type='button']")
        
        hareket.send_keys(Keys.ENTER)











        # self.browser.get(f"https://www.instagram.com/{username}/")
        # followers= self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_12']/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[2]/div/div[2]/button")
        # if followers.text=="Following":
        #     followers.click()
        # else:
        #     print("zaten kullanıcıyı takip ediyorsunuz")
    def UnfollowUser(self,username):
        self.browserservice=webdriver.ChromeOptions()
        self.browserservice.add_experimental_option("prefs",{'intl.accept_languages':"en,en_US"})
        self.browser=webdriver.Chrome("chromedriver.exe",chrome_options=self.browserservice)
        self.browser.get(f"https://www.instagram.com/{username}/")
        unfollowbutton=self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_12']/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/button")
        ubfollowstr= self.browser.find_element(By.XPATH,"")
        if( ubfollowstr.text=="Unfollow"):
            unfollowbutton.click()
            Button=self.browser.find_element(By.XPATH,"//button[text]='Unfollow'")
            accept=self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_12']/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]")

            accept.click()
        else:
            print("zaten takip etmiyorsunuz:")


 
ınstagram= Intagram(username=username,password=password)
ınstagram.sıgnın()
#ınstagram.gettakipçiliste()
ınstagram.followUser(username="therock")
# ınstagram.UnfollowUser(username=username)











