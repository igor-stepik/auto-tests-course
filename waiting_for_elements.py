"""
1) Открыть страницу http://suninjuly.github.io/explicit_wait2.html
2) Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
3) Нажать на кнопку "Book"
4) Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
"""

from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

button = browser.find_element_by_id("book")
button.click()
#browser.execute_script("window.scrollBy(0, 300);")
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

a = browser.find_element_by_id("input_value")
num = a.text

y = calc(num)

field = browser.find_element_by_class_name("form-control")
field.send_keys(y)



submit = browser.find_element_by_id("solve")
submit.click()
