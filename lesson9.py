from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser.get(link)
    elements = browser.find_elements_by_xpath("//input")
    for element in elements:
        element.send_keys("Test")

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
