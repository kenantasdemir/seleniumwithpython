from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.com.tr")

print(driver.get_window_position())
print(driver.get_window_rect())
print(driver.get_window_size())

print(driver.get_log("browser"))

# Selenium WebDriver'da get_log() yöntemi, tarayıcıya bağlı olarak farklı log türlerini almanızı sağlar. 
# Ancak, her tarayıcı bu log türlerini desteklemeyebilir veya farklı şekilde adlandırabilir. 
# Bu nedenle, tarayıcı türüne bağlı olarak hangi log türlerinin desteklendiğini kontrol etmek önemlidir.

# Örneğin, Chrome tarayıcısı için get_log() yöntemini kullanarak browser loglarını alabilirsiniz. 
# Ancak, Firefox tarayıcısı için get_log() yöntemi, 
# browser loglarını desteklemeyebilir ve farklı bir log türü adı kullanabilir.

print(driver.log_types)


# driver.execute_script("window.print();")


# links=driver.find_elements(By.TAG_NAME,"a")
# for link in links:
#     print(link.tag_name + " " + link.text)

time.sleep(3)

# print(driver.page_source)
#sayfanın kaynak kodlarını verir.

print(driver.current_url)
driver.set_window_size(800,600)
#genişlik yükseklik

time.sleep(3)

driver.refresh()
#sayfayı yeniler

time.sleep(3)

driver.maximize_window()

time.sleep(3)

driver.minimize_window()


time.sleep(3)


driver.fullscreen_window()
