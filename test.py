
#importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
 

driver = webdriver.Chrome()
 
url = "https://testpages.herokuapp.com/styled/index.html"

# Opening the website
driver.get(url)
 
# getting the button by class name
button = driver.find_element_by_partial_link_text("Dynamic Buttons Challenge 01")
 
# clicking on the button
button.click()
driver.implicitly_wait(5000)
driver.find_element(By.ID,"button00").click()
driver.find_element(By.ID,"button01").click()
driver.find_element(By.ID,"button02").click()
driver.find_element(By.ID,"button03").click()
text = driver.find_element(By.ID,"buttonmessage").text
assert 'All Buttons Clicked' in text