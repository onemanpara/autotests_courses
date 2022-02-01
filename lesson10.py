from selenium import webdriver
import time

browser = webdriver.Chrome()
link = ("http://suninjuly.github.io/registration1.html")

try:
    browser.get(link)
    input1 = browser.find_elements_by_xpath("//div[@class='first_block']//input")
    for input1 in input1:
        input1.send_keys("Text")
    button = browser.find_element_by_xpath("//button")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_xpath("//h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
        time.sleep(10)
        browser.quit()

