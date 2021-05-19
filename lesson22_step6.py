from selenium import webdriver
import time
from math import *

def func(x):
    return log(abs(12 * sin(x)))

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = int(browser.find_element_by_id('input_value').text)
submit_btn = browser.find_element_by_css_selector('button')
browser.execute_script('window.scrollBy(0,100);')
browser.find_element_by_id('answer').send_keys(str(func(x)))

browser.find_element_by_id('robotCheckbox').click()
browser.find_element_by_id('robotsRule').click()
submit_btn.click()

time.sleep(10)
browser.close()