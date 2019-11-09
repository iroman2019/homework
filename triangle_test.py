from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://iroman2019.github.io/homework/triangles.html")

a_input = driver.find_element(By.ID, "a-input")
b_input = driver.find_element(By.ID, "b-input")
c_input = driver.find_element(By.ID, "c-input")
calculate_button = driver.find_element(By.ID, "calculate-button")

# Egyenlő oldal teszt
a_input.send_keys(3)
b_input.send_keys(3)
c_input.send_keys(3)
calculate_button.click()
last_li = driver.find_element(By.XPATH, "//li[last()]").text
print(last_li)
assert last_li == "a = 3, b = 3, c = 3: Egyenlő oldalú"

