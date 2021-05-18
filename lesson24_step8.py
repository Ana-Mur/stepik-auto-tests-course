from math import *
def function(x):
    answer = log(abs(12 * sin(x)))
    return answer

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
    
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)

wait = WebDriverWait(browser, 12)
wait.until(EC.text_to_be_present_in_element((By.ID, 'price'),'$100'))

browser.find_element_by_id('book').click()
x = int(browser.find_element_by_id('input_value').text)
browser.find_element_by_id('answer').send_keys(str(function(x)))
browser.find_element_by_id('solve').click()

time.sleep(10)
browser.close()