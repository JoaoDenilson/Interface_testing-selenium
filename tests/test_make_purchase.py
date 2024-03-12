import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# Taking Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Add item to cart
# driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
driver.find_element(By.XPATH, "//*[@id='item_4_title_link']//*[text()='Sauce Labs Backpack']").click()
driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

# Checking that the item has been added to the cart
driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

# Returning to view products
driver.find_element(By.ID, "continue-shopping").click()

# Add item 2 to cart
driver.find_element(By.XPATH, "//*[@id='item_0_title_link']//*[text()='Sauce Labs Bike Light']").click()
driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

# Checking all items has been added to the cart
driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()

# Check-out all cart item
driver.find_element(By.ID, "checkout").click()

# Fill purchase data
driver.find_element(By.ID, "first-name").send_keys("João")
driver.find_element(By.ID, "last-name").send_keys("Denison")
driver.find_element(By.ID, "postal-code").send_keys("63452-222")
driver.find_element(By.ID, "continue").click()

# Checkout: Overview | Finalizing purchase
driver.find_element(By.ID, "finish").click()

# Checking purchase order
assert driver.find_element(By.XPATH, "//*[@class='complete-header' and text()='Thank you for your order!']").is_displayed()

