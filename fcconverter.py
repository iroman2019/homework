from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.convertworld.com/hu/homerseklet/fahrenheit.html")

fahrenheit = input("A fahrenheit értéke: ")
driver.find_element(By.NAME, "amount").send_keys(fahrenheit)
driver.find_element(By.CLASS_NAME, "ok").click()
f = driver.find_element(By.ID, "result-from").text
web_text = driver.find_element(By.ID, "result-equals").text
c = driver.find_element(By.XPATH, "//*[@id='result-to']/b").text
result = f + " " + web_text + " " + c
print(result)
# assert result == "15 F egyenlő -9,44 C"
driver.save_screenshot("fc_result.png")



