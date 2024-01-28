import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://only-testing-blog.blogspot.com/2014/01/textbox.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//*[@id='post-body-4292417847084983089']/div[1]/input").click()
time.sleep(1)
driver.switch_to.alert.accept()   # OK
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="post-body-4292417847084983089"]/div[1]/button[1]').click()
time.sleep(1)
driver.switch_to.alert.dismiss()    #  Cancel
message = driver.find_element(By.ID, "demo").text

print(message)

driver.quit()

print("Everything is worked just fine.")


