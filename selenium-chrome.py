from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.google.com')
print(browser.page_source)