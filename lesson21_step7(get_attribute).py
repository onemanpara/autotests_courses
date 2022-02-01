from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = ("http://suninjuly.github.io/get_attribute.html")

try:
    browser.get(link)
    img = browser.find_element_by_xpath("//img")
    x = img.get_attribute("valuex") #присваем значение из элемента img равное valuex
    y = calc(x)
    value = browser.find_element_by_xpath("//input[@id='answer']")
    value.send_keys(y)
    checkbox = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    checkbox.click()
    radio = browser.find_element_by_xpath("//input[@id='robotsRule']")
    radio.click()
    button = browser.find_element_by_xpath("//button")
    button.click()

finally:
    time.sleep(20)
    browser.quit()

