from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time
#saylankin damir 107b

driver = webdriver.Chrome()

URL1 = (r"https://the-internet.herokuapp.com/context_menu")
URL2 = (r"https://the-internet.herokuapp.com/upload")

driver.get(URL1)
driver.maximize_window()

time.sleep(3)

context_menu_element = driver.find_element(By.ID, "hot-spot")
actions = ActionChains(driver)
actions.context_click(context_menu_element).perform()

alert = Alert(driver)
time.sleep(3)

alert.accept()

time.sleep(3)
#saylankin damir 107b

driver.get(URL2)

file_path = (r"C:\Users\jojow\Documents\python\lab1\emty.txt")

with open(file_path, 'w') as file:
    pass

upload_input = driver.find_element(By.ID, "file-upload")
upload_input.send_keys(file_path)

upload_btn = driver.find_element(By.ID, "file-submit")
upload_btn.click()

time.sleep(3)

success_message = driver.find_element(By.TAG_NAME, "h3").text
assert success_message == "FILE UPLOADED!", "FILE WAS NOT UPLOADED"

time.sleep(2)

driver.quit()
