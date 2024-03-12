import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce-error")
driver.find_element(By.ID, "login-button").click()

h3Element = driver.find_element(By.XPATH, "//*[@id='login_button_container' ]/div/form/div[3]/h3")
assert h3Element.text == "Epic sadface: Username and password do not match any user in this service"




