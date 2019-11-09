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
driver.save_screenshot("result.png")

# Törölni kell, mert a következő teszt hozzáfüzné a korábbi értékekhez az új számokat
a_input.clear()
b_input.clear()
c_input.clear()

# Nincs háromszög
a_input.send_keys(20)
b_input.send_keys(5)
c_input.send_keys(10)
calculate_button.click()
last_li = driver.find_element(By.XPATH, "//li[last()]").text
print(last_li)
assert last_li == "a = 20, b = 5, c = 10: Nem háromszög"
driver.save_screenshot("not_triangle.png")

# Törölni kell, mert a következő teszt hozzáfüzné a korábbi értékekhez az új számokat
a_input.clear()
b_input.clear()
c_input.clear()

# Negatív
a_input.send_keys(10)
b_input.send_keys(-2)
c_input.send_keys(4)
calculate_button.click()
last_li = driver.find_element(By.XPATH, "//li[last()]").text
print(last_li)
assert last_li == "a = 10, b = -2, c = 4: Negatív"
driver.save_screenshot("negativ.png")

# Törölni kell, mert a következő teszt hozzáfüzné a korábbi értékekhez az új számokat
a_input.clear()
b_input.clear()
c_input.clear()

# Nem szám
a_input.send_keys(2)
b_input.send_keys(5)
c_input.send_keys("q")
calculate_button.click()
last_li = driver.find_element(By.XPATH, "//li[last()]").text
print(last_li)
assert last_li == "a = 2, b = 5, c = q: Harmadik nem szám"
driver.save_screenshot("not_number.png")

# Törölni kell, mert a következő teszt hozzáfüzné a korábbi értékekhez az új számokat
a_input.clear()
b_input.clear()
c_input.clear()

# Egyenlő szárú
a_input.send_keys(10)
b_input.send_keys(5)
c_input.send_keys(10)
calculate_button.click()
last_li = driver.find_element(By.XPATH, "//li[last()]").text
print(last_li)
assert last_li == "a = 10, b = 5, c = 10: Egyenlő szárú"
driver.save_screenshot("egyenlo_szaru.png")

# Törölni kell, mert a következő teszt hozzáfüzné a korábbi értékekhez az új számokat
a_input.clear()
b_input.clear()
c_input.clear()

# Általános
a_input.send_keys(10)
b_input.send_keys(5)
c_input.send_keys(8)
calculate_button.click()
last_li = driver.find_element(By.XPATH, "//li[last()]").text
print(last_li)
assert last_li == "a = 10, b = 5, c = 8: Általános"
driver.save_screenshot("standard.png")