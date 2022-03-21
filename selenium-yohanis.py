from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pickle

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

# print(driver.get_cookies())
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
cookies = driver.get_cookies()

# for cookie in cookies:
print(cookies[0])
# 	print("\n")

# driver.close()

# driver = webdriver.Firefox()
# driver.add_cookie(cookies[0])
# driver.get("https://eod.sifoma.id/dashboard")


# email_elem.send_keys("sinergy")
# driver.quit()