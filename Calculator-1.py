from selenium.webdriver.support.ui import Select 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.safari.service import Service
from selenium import webdriver 
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

url = "https://testpages.herokuapp.com/styled/calculator"
driver.get(url)
operators = ["minus","times","plus","divide"]
for i in range(4):
    
    input1 = driver.find_element_by_id("number1")
    input2 = driver.find_element_by_id("number2")
    input1.clear()
    input2.clear()
    input1.send_keys(10)
    input2.send_keys(10)
    select = Select(driver.find_element_by_name("function"))
    select.select_by_visible_text(operators[i])
    driver.find_element_by_id("calculate").click()
    print(driver.find_element(By.ID, "answer").text)


