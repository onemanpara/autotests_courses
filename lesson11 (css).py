from selenium import webdriver
import time

browser = webdriver.Chrome()
link = ("http://suninjuly.github.io/registration1.html")

try:
    browser.get(link)
    input1 = browser.find_element_by_css_selector(".first_block .form-group.first_class input")
    input1.send_keys("Text")
    input2 = browser.find_element_by_css_selector(".first_block .form-group.second_class input")
    input2.send_keys("Text")
    input3 = browser.find_element_by_css_selector(".first_block .form-group.third_class input")
    input3.send_keys("Text")
    button = browser.find_element_by_xpath("//button")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_xpath("//h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

