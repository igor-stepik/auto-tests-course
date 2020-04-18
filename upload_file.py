"""
1) Открыть страницу http://suninjuly.github.io/file_input.html
2) Заполнить текстовые поля: имя, фамилия, email
3) Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
4) Нажать кнопку "Submit"
"""

from selenium import webdriver
import math
import os


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

nameField = browser.find_element_by_css_selector("[name='firstname']")
nameField.send_keys("username")

lastName = browser.find_element_by_css_selector("[name='lastname']")
lastName.send_keys("lastname")

email = browser.find_element_by_css_selector("[name='email']")
email.send_keys("email")

fileUpload = browser.find_element_by_id('file')

current_dir = os.path.abspath(os.path.dirname('/Users/owner/environments/'))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'myNotes.txt')           # добавляем к этому пути имя файла
fileUpload.send_keys(file_path)

button = browser.find_element_by_class_name("btn")
button.click()
