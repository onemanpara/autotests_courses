from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
link = ("http://suninjuly.github.io/selects1.html")

try:
    browser.get(link)
    num1 = browser.find_element_by_xpath("//span[@id='num1']")
    x = num1.text #вытягиваем из элемента num1 текст (число)
    num2 = browser.find_element_by_xpath("//span[@id='num2']")
    y = num2.text #вытягиваем из элемента num2 текст (число)
    sum = (int(x)+int(y)) #обязательно присваем числу числовое значение int
    select = Select(browser.find_element_by_xpath("//select"))
    select.select_by_value(str(sum)) #присваему числу строковое значние str т.к. поиск происходит по строке
    button = browser.find_element_by_xpath("//button")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
