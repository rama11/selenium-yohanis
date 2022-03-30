from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://dev-yohanis.sifoma.id/login")

assert "Work Activity" in driver.title

email_elem = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
email_elem.clear()
email_elem.send_keys("agastya@sinergy.co.id")
email_elem.send_keys(Keys.RETURN)

pass_elem = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
pass_elem.clear()
pass_elem.send_keys("asdasdasd")
pass_elem.send_keys(Keys.RETURN)

time.sleep(3)
assert "Work Activity - Tech Support" in driver.title
menu_elem = driver.find_element(By.CSS_SELECTOR, "a[href='https://dev-yohanis.sifoma.id/time-sheet']")
menu_elem.click()

time.sleep(3)
assert "Work Activity - Tech Support" in driver.title
# print("Success Open Work Sheet")

button_create = driver.find_element(By.CSS_SELECTOR, "button[data-target='#addActivityModal']")
button_create.click()

modal_elem = driver.find_element(By.CSS_SELECTOR,"label.col-sm-2.col-form-label")

time.sleep(3)
date_time_input = driver.find_element(By.ID,"addDateTime")
date_time_input.click()
time.sleep(3)
modal_elem.click()

# customer_elem = driver.find_element(By.CSS_SELECTOR, "span[class='select2 select2-container select2-container--default']")
time.sleep(2)
customer_elem = driver.find_element(By.ID, "select2-selectCustomer-container")
customer_elem.click()
search_elem = driver.find_element(By.CSS_SELECTOR,"input[class='select2-search__field']")
search_elem.send_keys("Internal")
search_elem.send_keys(Keys.RETURN)

time.sleep(2)
pid_elem = driver.find_element(By.ID, "select2-selectPID-container")
pid_elem.click()
search_elem = driver.find_element(By.CSS_SELECTOR,"input[class='select2-search__field']")
search_elem.send_keys("Internal")
search_elem.send_keys(Keys.RETURN)

time.sleep(2)
desc_elem = driver.find_element(By.ID, "addDescription")
desc_elem.send_keys("Test Selenium")
desc_elem.send_keys(Keys.RETURN)

time.sleep(2)
site_btn = driver.find_element(By.CSS_SELECTOR, "button[data-id='addSiteLocation']")
site_btn.click()
site_btn.send_keys(Keys.DOWN)
site_btn.send_keys(Keys.RETURN)

time.sleep(2)
duration_btn = driver.find_element(By.CSS_SELECTOR, "button[data-id='addDuration']")
duration_btn.click()
duration_btn.send_keys(Keys.DOWN)
duration_btn.send_keys(Keys.RETURN)

time.sleep(2)
status_btn = driver.find_element(By.CSS_SELECTOR, "button[data-id='addStatus']")
status_btn.click()
status_btn.send_keys(Keys.DOWN)
status_btn.send_keys(Keys.RETURN)

time.sleep(2)
btn_create = driver.find_element(By.CSS_SELECTOR, "button[onclick='createActivity()']")
btn_create.click()

time.sleep(2)
btn_confirm = driver.find_element(By.CSS_SELECTOR, "button[class='swal2-confirm btn btn-success']")
btn_confirm.click()

time.sleep(2)
assert "Success!" in driver.find_element(By.ID, "swal2-title").text
print("Success Add Activity")

btn_reload = driver.find_element(By.CSS_SELECTOR, "button[class='swal2-confirm swal2-styled']")
btn_reload.click()

time.sleep(2)
driver.quit()