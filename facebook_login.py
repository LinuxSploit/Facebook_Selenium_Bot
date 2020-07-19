#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common import keys

email = input("Enter email: ")
pw = input("Enter Password: ")

driver = webdriver.Firefox()

driver.get("https://web.facebook.com/login.php?_rdc=1&_rdr")

email_id = driver.find_element_by_id("email")

email_id.send_keys(email)

pw_id = driver.find_element_by_id("pass")

pw_id.send_keys(pw)

submit = driver.find_element_by_id("loginbutton")

submit.click()
