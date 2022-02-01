import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = ("http://suninjuly.github.io/explicit_wait2.html")

try:
    browser.get(link)
    button1 = browser.find_element(By.XPATH, "//button[@id='book']")
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "$100")
    )
    button1.click()
    num = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = num.text
    y = calc(x)
    input = browser.find_element(By.XPATH, "//input")
    input.send_keys(y)
    button2 = browser.find_element(By.XPATH, "//button[@type='submit']")
    button2.click()
    print(browser.switch_to.alert.text)

finally:
    time.sleep(20)
    browser.quit()