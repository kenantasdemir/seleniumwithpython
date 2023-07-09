from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.amazon.com.tr")


driver.mobile.tap()
driver.mobile.swipe()

driver.mobile.orientation = "PORTRAIT"
driver.mobile.orientation = "LANDSCAPE"







