import math
import time
from selenium import webdriver

site = 'http://suninjuly.github.io/math.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
browser = webdriver.Chrome()
browser.get(site)

x = browser.find_element_by_css_selector('#input_value').text
answer = browser.find_element_by_css_selector('#answer')
answer.send_keys(calc(x))

browser.find_element_by_css_selector('#robotCheckbox').click()
browser.find_element_by_css_selector('#robotsRule').click()
browser.find_element_by_css_selector('[type="submit"]').click()
time.sleep(10)
browser.close()