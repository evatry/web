from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'To-do' in browser.title
bowser.quit()

