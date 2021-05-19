import time 
from selenium import webdriver

shop = "https://www.ozon.ru/highlight/69294/"

try:
    browser = webdriver.Chrome()
    browser.get(shop)
    add_to_cart_btns = browser.find_elements_by_css_selector("div.ao3 button._1-6r")
    
    for i in range(0, 9, 3):
        add_to_cart_btns[i].click()
        time.sleep(3)
    
    my_cart_btn = browser.find_element_by_css_selector("svg.c6h2")
    my_cart_btn.click()
        
    goods = browser.find_elements_by_css_selector("input._1V0q")
    assert len(goods) - 1 == 3
   
finally:
    time.sleep(30)
    browser.close()