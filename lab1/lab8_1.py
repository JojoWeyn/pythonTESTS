from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
#Кадочников Александр 107Б
def translate(text):
    driver.switch_to.window(driver.window_handles[0])
    input_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fakeArea")))
    input_box.send_keys(text)
    time.sleep(20)
    translated_text_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.measurer-text.measurer-text_main")))
    translated_text = translated_text_element.get_attribute("textContent")
    print(translated_text)
    return translated_text
options = webdriver.EdgeOptions()
options.add_argument("start-maximized")
service = EdgeService(executable_path=r"C:\Users\love_\Desktop\python\msedgedriver.exe")  
driver = webdriver.Edge(service=service, options=options)

driver.get("https://translate.yandex.ru/")
driver.switch_to.new_window('tab')
driver.get("https://www.culture.ru/literature/poems/author-aleksandr-pushkin")

poems = driver.find_elements(by="css selector", value="a.ICocV")
poem_links = [poem.get_attribute("href") for poem in poems[:8]]
data = {}
print(poem_links)
i = 0
file = open('translated_poems.txt', 'w')

for link in poem_links:
    i += 1
    driver.get(link)
    try:
        but = driver.find_element(by="xpath", value="//button[text()='Развернуть']")
        but.click()
    except:
        continue
    text = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-content='text']")))
    title = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.rrWFt'))).text
    poem_part = [txt.text for txt in text]
    print(f"{i}стих")
    print(title)
    
    itog = ''
    translate_itog = ''
    print(len(poem_part))
    for part in poem_part:
        print(type(part))
        translate_itog += translate(part)
        print(translate_itog)
        itog += str(part)
        itog += '\n'
    driver.switch_to.window(driver.window_handles[1])

driver.quit()
