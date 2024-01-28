from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.ru/")
driver.maximize_window()

title = driver.title

print("Title is ", title)

driver.close()
