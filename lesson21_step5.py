from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = ("http://suninjuly.github.io/math.html")

try:
    browser.get(link)
    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text #извлечь только текст из переменной
    y = calc(x)
    answer = browser.find_element_by_xpath("//input[@id='answer']")
    answer.send_keys(y)
    checkbox = browser.find_element_by_xpath("//label[@for='robotCheckbox']")
    checkbox.click()
    radio = browser.find_element_by_xpath("//label[@for='robotsRule']")
    radio.click()
    button = browser.find_element_by_xpath("//button")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
