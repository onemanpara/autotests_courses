from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = ("http://suninjuly.github.io/redirect_accept.html")

try:
    browser.get(link)
    button = browser.find_element_by_xpath("//button")
    button.click()
    new_window = browser.window_handles[1] #задаём в переменную новую открытую вкладку
    browser.switch_to.window(new_window) #переключаемся на новую вкладку
    input = browser.find_element_by_xpath("//span[@id='input_value']")
    x = input.text
    y = calc(x)
    answer = browser.find_element_by_xpath("//input[@id='answer']")
    answer.send_keys(y)
    button1 = browser.find_element_by_xpath("//button")
    button1.click()
    print(browser.switch_to.alert.text)

finally:
    time.sleep(20)
    browser.quit()

