import time

from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
link = ("http://suninjuly.github.io/execute_script.html")

try:
    browser.get(link)
    num = browser.find_element_by_xpath("//span[@id='input_value']")
    x = num.text
    y = calc(x)
    answer = browser.find_element_by_xpath("//input[@id='answer']")
    answer.send_keys(y)
    button = browser.find_element_by_xpath("//button")
    #скрипт, который скроллит до элемента button пока он не появится в видмой части
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element_by_xpath("//label[@for='robotCheckbox']")
    checkbox.click()
    radio = browser.find_element_by_xpath("//label[@for='robotsRule']")
    radio.click()
    button.click()

finally:
    time.sleep(20)
    browser.quit()
