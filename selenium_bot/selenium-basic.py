
from selenium import webdriver
import time

driver=webdriver.Chrome()
url="https://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
#driver.save_screenshot("github.com-homepage.png")
#aldığımız ekran görüntüüsünü o dosyaya başarılı bir şekilde oluşturdu


driver.get(f"{url}/Hasan26ozcan")

time.sleep(2)

if "Hasan26ozcan" in driver.title:
    driver.save_screenshot("github-Hasan26ozcan.jpg")

driver.back()
print(driver.title)

time.sleep(2)
driver.close()















