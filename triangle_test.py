from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

a=input("Az 'a' oldal hossza: ")
driver.find_element(By.ID, "a-input") .send_keys(a)