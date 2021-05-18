from math import *
def function(x):
    answer = log(abs(12 * sin(x)))
    return answer

from selenium import webdriver
import time
    
link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_tag_name('button').click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x = int(browser.find_element_by_id('input_value').text)
browser.find_element_by_id('answer').send_keys(str(function(x)))
browser.find_element_by_tag_name('button').click()


time.sleep(10)
browser.close()