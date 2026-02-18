from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'text.txt')

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
browser.implicitly_wait(3)

try:
    a = WebDriverWait(browser,10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    if a:
        button = browser.find_element(By.ID,"book")
        button.click()
        x = browser.find_element(By.ID, "input_value")
        x = int(x.text)
        b = math.log(abs(12 * math.sin(x)))
        inp = browser.find_element(By.ID, "answer")
        inp.send_keys(str(b))
finally:
    browser.quit()