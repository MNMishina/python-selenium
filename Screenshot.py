from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(3)

driver.get("https://jqueryui.com/datepicker")

driver.maximize_window()

driver.save_screenshot('datepicker2.png')
