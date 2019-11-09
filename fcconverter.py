from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.convertworld.com/hu/homerseklet/fahrenheit.html")

fahrenheit = input("A fahrenheit értéke: ")
driver.find_element(By.NAME, "amount").send_keys(fahrenheit)
decimals= input("Hány tizedesre (1-10): ")
driver.find_element(By.NAME, "decimals").click()
dropdown = driver.find_element(By.NAME, "decimals")
dropdown.find_element(By.XPATH, "//option[. = '" + decimals + " tizedesjegyek száma" + "']").click()
driver.find_element(By.NAME, "decimals").click()
# decimals = driver.find_element(By.CSS_SELECTOR, "#conv_temperature_ext > p:nth-child(2) > select.form-control.extended-decimals > option[selected='"+"selected"+"']").get_attribute("value")
driver.find_element(By.CLASS_NAME, "ok").click()
f = driver.find_element(By.ID, "result-from").text
web_text = driver.find_element(By.ID, "result-equals").text
c = driver.find_element(By.XPATH, "//*[@id='result-to']/b").text

print(decimals)
decimals_int = int(decimals)
c_withoutC = c[:-2]
c_withoutC = c_withoutC .replace(',', '.')
print(c_withoutC)
c_float = float(c_withoutC)
result = f + " " + web_text + " " + str(c_float) + " C"
celsius = round((float(fahrenheit) - 32)/1.8, decimals_int)
print(celsius)
result_text = fahrenheit + " F egyenlő " + str(celsius) + " C"
print(result)
assert result == result_text
driver.save_screenshot("fc_result.png")



