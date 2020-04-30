from selenium import webdriver
import math

"""
1) Открыть страницу http://suninjuly.github.io/redirect_accept.html
2) Нажать на кнопку
3) Переключиться на новую вкладку
4) Пройти капчу для робота и получить число-ответ
"""


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element_by_class_name("btn")
button.click()

new_tab = browser.window_handles[1]

browser.switch_to.window(new_tab)

a = browser.find_element_by_id("input_value")
num = a.text

y = calc(num)

field = browser.find_element_by_class_name("form-control")
field.send_keys(y)

submit = browser.find_element_by_class_name("btn")
submit.click()
