from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import WebDriverWait
from selenium import webdriver

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))  
#idsi someid olan elementin tıklanabilir hale gelmesini 10 saniye boyunca bekler.



