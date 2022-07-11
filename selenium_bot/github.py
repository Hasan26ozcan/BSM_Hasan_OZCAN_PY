from os import link
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from githubUserInfo import username,password
from selenium import webdriver
import time


class Github:
    def __init__(self,username,password):
        self.browser=webdriver.Chrome()
        self.username=username
        self.password=password
        self.liste=[]
    def sıgIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        usernamelogin=self.browser.find_element(By.NAME,"login")
        usernamelogin.send_keys(username)
        
        passwordlogin=self.browser.find_element(By.NAME,"password")
        passwordlogin.send_keys(password)

        passwordlogin.send_keys(Keys.ENTER)
    def getfallowers(self):
        self.loadfallowers()
    def loadfallowers(self):
        items=self.liste.append(self.browser.find_elements(By.CSS_SELECTOR,".d-table.table-fixed"))
        for i in items:
            self.liste.append(i.find_element(By.CSS_SELECTOR,"Link--secondary").text)
        while True:
            links=self.browser.find_element(By.CLASS_NAME,"BtnGroup").find_element(By.TAG_NAME,"a")

            if 1==len(links):
                if links.text=="Next":
                    links.click()
                    self.loadfallowers()
                else:
                    break
            else:
                for link in links:
                    if (link.text=="Next"):
                        link.click()
                    self.loadfallowers()


        print(self.liste)
    def okuma(self):
        self.liste.append(self.browser.find_elements(By.XPATH,"//*[@id='js-pjax-container']/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/a/span[2]").text)
        print(self.liste)
        

github=Github(username=username,password=password)
github.sıgIn()
github.getfallowers()
print("**"*50)
github.okuma()












