import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

site = 'http://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
browser.get(site)

num1 = int(browser.find_element_by_id('num1').text)
num2 = int(browser.find_element_by_id('num2').text)
answer = num1 + num2

answer_list = Select(browser.find_element_by_id('dropdown'))
answer_list.select_by_visible_text(str(answer))

browser.find_element_by_css_selector('button[type="submit"]').click()
time.sleep(10)
browser.close()