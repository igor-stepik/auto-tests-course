"""
Открыть страницу http://suninjuly.github.io/wait1.html
Нажать на кнопку "Verify"
Проверить, что появилась надпись "Verification was successful!"
"""


from selenium import webdriver

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

if "successful" in message.text:
    print("Good work")
