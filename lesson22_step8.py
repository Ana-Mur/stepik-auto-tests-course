from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

browser.find_element_by_name('firstname').send_keys('Самсон')
browser.find_element_by_name('lastname').send_keys('Самсонов')
browser.find_element_by_name('email').send_keys('sams@bk.ru')
file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.txt')
browser.find_element_by_id('file').send_keys(file_path)

browser.find_element_by_tag_name('button').click()

time.sleep(10)
browser.close()