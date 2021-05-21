from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest

class TestFields(unittest.TestCase):
    def test_fields1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.implicity_wait(5)
        browser.get(link)
        
        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector('.first_block .first').send_keys("Ivan")
        browser.find_element_by_css_selector('.first_block .second').send_keys("Mutko")
        browser.find_element_by_css_selector('.first_block .third').send_keys("noreply@list.ru")
        
        # Отправляем заполненную форму
        browser.find_element_by_css_selector("button.btn").click()
        
        # Проверяем, что смогли зарегистрироваться
        # находим элемент, содержащий текст
        welcome_text = browser.find_element_by_tag_name("h1").text
        
        # проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text,  "Congratulations! You have successfully registered!", "Registration failed")
        browser.close()
        
    def test_fields2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.implicity_wait(5)
        browser.get(link)
        
        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector('.first_block .first').send_keys("Ivan")
        browser.find_element_by_css_selector('.first_block .second').send_keys("Mutko")
        browser.find_element_by_css_selector('.first_block .third').send_keys("noreply@list.ru")
        
        # Отправляем заполненную форму
        browser.find_element_by_css_selector("button.btn").click()
        
        # Проверяем, что смогли зарегистрироваться
        # находим элемент, содержащий текст
        welcome_text = browser.find_element_by_tag_name("h1").text
        
        # проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text,  "Congratulations! You have successfully registered!", "Registration failed")
        browser.close()

if __name__ == "__main__":
    unittest.main()
