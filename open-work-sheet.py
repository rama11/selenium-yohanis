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
print("Success Open Work Sheet")


driver.quit()