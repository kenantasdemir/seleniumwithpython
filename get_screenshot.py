from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.amazon.com.tr")


driver.save_screenshot("amazon.png")

driver.quit()