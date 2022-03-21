from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pickle
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://dev-yohanis.sifoma.id")

time.sleep(3)
assert "Laravel" in driver.title
print("Success Open Home")
driver.quit()