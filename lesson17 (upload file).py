import time
from selenium import webdriver
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла

browser = webdriver.Chrome()
link = ("http://suninjuly.github.io/file_input.html")

try:
    browser.get(link)
    input = browser.find_elements_by_xpath("//input[@type='text']")
    for input in input:
        input.send_keys("Text")
    file = browser.find_element_by_xpath("//input[@type='file']")
    file.send_keys(file_path)
    button = browser.find_element_by_xpath("//button")
    button.click()

finally:
    time.sleep(20)
    browser.quit()