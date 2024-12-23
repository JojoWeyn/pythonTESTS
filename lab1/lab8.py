from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def translate(driver, text):
    """Translate text using Google Translate."""

    driver.switch_to.window(driver.window_handles[0])


    input_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[aria-label='Исходный текст']"))
    )
    input_box.clear()
    input_box.send_keys(text)
    time.sleep(3)

    translated_text_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.lRu31"))
    )
    
    translated_text = translated_text_element.text
    input_box.clear()
    
    driver.switch_to.window(driver.window_handles[1])
    
    return translated_text
    
driver = webdriver.Chrome()

try:

    driver.get("https://translate.google.com/?hl=ru&sl=auto&tl=en&op=translate")


    driver.switch_to.new_window('tab')
    driver.get("https://www.culture.ru/literature/poems/author-aleksandr-pushkin")

    poems = driver.find_elements(by="css selector", value="a.ICocV")
    poem_links = [poem.get_attribute("href") for poem in poems[:5]]

    with open('translated_poems.txt', 'w', encoding='utf-8') as file:
        for link in poem_links:

            driver.switch_to.new_window('tab')
            driver.get(link)

   
            try:
                expand_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[text()='Развернуть']"))
                )
                expand_button.click()
            except TimeoutException:
                pass  


            title = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.rrWFt'))
            ).text

            poem_parts = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-content='text']"))
            )
            poem_text = "\n".join(part.text for part in poem_parts)

            translated_text = translate(driver, poem_text)

            file.write(f"Title: {title}\n")
            file.write("Original:\n")
            file.write(poem_text + "\n\n")
            file.write("Translation:\n")
            file.write(translated_text + "\n\n")
            file.write("=" * 50 + "\n\n")

            driver.close()
            driver.switch_to.window(driver.window_handles[-1])

finally:

    driver.quit()
