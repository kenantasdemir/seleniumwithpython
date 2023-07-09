from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()  
driver.get("https://www.amazon.com")

search_box = driver.find_element(By.ID,"twotabsearchtextbox")
search_box.send_keys("telefon")
time.sleep(5)
search_box.clear()

# cerez = {"foo":"bar","ad":"Kenan"}
# driver.add_cookie(cerez)

cerezler = driver.get_cookies()
print(cerezler)


search_box.send_keys(Keys.RETURN)


pause = 5
scroll_step = 300
page_height = driver.execute_script("return document.body.scrollHeight")


# iteration = 5
# for i in range(iteration):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(pause)


#window.pageYOffset y ekseninde kaydırılan piksel sayısını verir.
# window.innerHeight Sayfanın şu anda görünen bölümünün yüksekliğini ifade eder.
while driver.execute_script("return window.pageYOffset + window.innerHeight") < page_height:
    driver.execute_script(f"window.scrollBy(0, {scroll_step});")
    time.sleep(pause)

# Tarayıcıyı kapatma
driver.quit()
