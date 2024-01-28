#   Get second Candidate name

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()

#driver.implicitly_wait(5)

username = WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.NAME, "username")))

username.send_keys("Admin")

driver.find_element(By.NAME,"password").send_keys("admin123")

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Recruitment']").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, window.scrollY + 400)")
time.sleep(2)
print(driver.find_element(By.XPATH, "(//div[contains(text(),'Charles')])[1]").text)

driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()

driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()

driver.quit()

print("Everything is worked just fine.")
