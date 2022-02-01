import math
import time
from selenium import webdriver


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/find_link_text"

try:
    browser.get(link)
    link1 = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link1.click()
    input1 = browser.find_element_by_xpath("//input[@name='first_name']")
    input1.send_keys('Ivan')
    input2 = browser.find_element_by_xpath("//input[@name='last_name']")
    input2.send_keys('Petrov')
    input3 = browser.find_element_by_xpath("//input[@class='form-control city']")
    input3.send_keys('Smolensk')
    input4 = browser.find_element_by_xpath("//input[@id='country']")
    input4.send_keys('Russia')
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
