from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()


driver.implicitly_wait(10) #bir sonraki adıma geçmeden önce 10 saniye bekler.

driver.get("http://127.0.0.1:5500/page.html")



select = Select(driver.find_element(By.NAME,'iller'))
select.select_by_index(0)
select.select_by_visible_text("İzmir")
select.select_by_value("kayseri")



print("**********************************************")



element =driver.find_element(By.XPATH,"//*[@id='iller']")
all_options = element.find_elements(By.TAG_NAME,"option")
for option in all_options:
    print("value is ",option.get_attribute("value"))
    option.click()


print("**********************************************")


for item in select.all_selected_options:
    print(item.accessible_name)
    print("***")

print("ilk seçilen option ",select.first_selected_option.accessible_name)


btn = driver.find_element(By.ID,"disabledBtn")
if(btn.is_enabled()):
    print("buton aktif")
else:
    print("buton disabled")


css_value = btn.value_of_css_property("color")
print(css_value)

className = btn.get_dom_attribute("class")
print("className " ,className)

btnStyle = btn.get_attribute("style")
print(btnStyle)


hiddenInput = driver.find_element(By.ID,"hiddenInput")
print("element kullanıcı tarafından görülebilir mi: ",hiddenInput.is_displayed())
print(hiddenInput.get_property("value"))


print("*********************************************************")


select = Select(driver.find_element(By.ID,"iller"))
select.deselect_all()


options = select.options
for option in options:
    print(option.accessible_name)




driver.find_element(By.ID,'submit').click()


form = driver.find_element(By.ID,"myForm")
form.submit()

driver.back()
time.sleep(2)
driver.forward()


# cookie = {'name' : 'Kenan', 'surname' : 'Taşdemir'}
# driver.add_cookie(cookie)

# for cookie in driver.get_cookies():
#     print(cookie)


print("*********************************************************")


driver.close()
print("close metodu çalıştı. tarayıcıyı kapatır fakat bağlantı devam eder.")
#baglantıyı da sonlandırmak için driver.quit() kullanmalısınız.


driver.quit()





