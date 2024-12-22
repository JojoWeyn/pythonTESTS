#saylankin damir 107b
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('https://python.org/')
    downloads_button = driver.find_element(By.LINK_TEXT, "Downloads")
    downloads_button.click()

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("python 3.11")
    search_box.send_keys(Keys.RETURN)
finally:   
    driver.quit()
