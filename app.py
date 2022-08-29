# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Firefox()

# get url
driver.get("https://www.youtube.com/")

# get element
element = driver.find_element(By.ID, "logo")

# click screenshot
element.screenshot('screenshot.png')
