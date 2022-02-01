import time
from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = ("http://suninjuly.github.io/alert_accept.html")

try:
    browser.get(link)
    button = browser.find_element_by_xpath("//button")
    button.click()
    alert = browser.switch_to.alert #задаём переменной alert команду переключения на алерт
    alert.accept() #принимаем алерт
    input = browser.find_element_by_xpath("//span[@id='input_value']")
    x = input.text
    y = calc(x)
    answer = browser.find_element_by_xpath("//input[@id='answer']")
    answer.send_keys(y)
    button2 = browser.find_element_by_xpath("//button")
    button2.click()
    print(browser.switch_to.alert.text) #выводим в консоль текст из алерта

finally:
    time.sleep(20)
    browser.quit()
