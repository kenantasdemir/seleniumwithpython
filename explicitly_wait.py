from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5500/page.html")

try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"myBtn"))
    )
    print("element hazır durumda")
finally:
    driver.quit()