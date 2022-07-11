from unittest import result
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
url="https://github.com/"
driver= webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(2)



searchInput=driver.find_element(By.NAME,"q",)
time.sleep(2)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(4)
results=driver.page_source
print(results)
#sonra beatifulsource ile yapabiliriz devamını


resulta=searchInput.find_elements(By.XPATH,"//*[@id='js-pjax-container']/div/div[3]/div/ul/li[1]/div[2]/div[1]/div[1]/a")
for i in resulta:
    print(i.text)


#driver.close()

