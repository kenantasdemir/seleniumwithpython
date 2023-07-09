from selenium import webdriver
import time

# WebDriver'ı başlatma
driver = webdriver.Chrome()

# Tarayıcıya bir URL açma
driver.get("http://127.0.0.1:5500/page.html")

time.sleep(5)


driver.close()

# Tarayıcıyı kapatma
driver.quit()
