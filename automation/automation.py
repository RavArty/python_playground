from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

button = chrome_browser.find_element_by_class_name('btn-default')

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('asdf')
button.click()

out_message = chrome_browser.find_element_by_id('display')

assert 'asdf' in out_message.text

chrome_browser.quit()