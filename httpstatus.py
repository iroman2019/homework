from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
status_code = input("A státusz kód?: ")
driver.get("https://httpstatuses.com/")

status_name = driver.find_element(By.XPATH, "//li[a[span[text()='"+status_code+"']]]/a").text
print(status_name)

driver.get("https://httpstatusdogs.com/ ")
status_name2 = driver.find_element(By.XPATH, "//div[a[img[@alt='"+status_name+"']]]/a/img")
status_name2.screenshot("status_dog.png")
