from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import base64
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless') 
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-blink-features=AutomationControlled') 

driver = webdriver.Chrome(options=options)

driver.get("https://www.base64encode.org/")

driver.execute_script("window.open('https://ru.wikipedia.org', '_blank');")  # Русская вики
driver.execute_script("window.open('https://en.wikipedia.org', '_blank');")  # Английская вики

driver.switch_to.window(driver.window_handles[1])

# Ожидаем загрузки страницы
time.sleep(3)

for _ in range(5):
    try:
        # Находим и кликаем по ссылке "Случайная статья" через XPath
        random_article_link = driver.find_element(By.XPATH, "//a[contains(text(),'Случайная статья')]")
        random_article_link.click()
        time.sleep(3)  # Ждем загрузки новой страницы
    except Exception as e:
        print(f"Ошибка при открытии случайной статьи на русской Википедии: {e}")
        break

# Скриншот русских вкладок
driver.save_screenshot("russian_wiki_tabs.png")

# Переключаемся на английскую Википедию (вкладка 2)
driver.switch_to.window(driver.window_handles[2])

# Ожидаем загрузки страницы
time.sleep(3)

# Открываем 5 случайных статей на английской Википедии
for _ in range(5):
    try:
        # Находим и кликаем по ссылке "Random article" через XPath
        random_article_link = driver.find_element(By.XPATH, "//a[contains(text(),'Random article')]")
        random_article_link.click()
        time.sleep(3)  # Ждем загрузки новой страницы
    except Exception as e:
        print(f"Ошибка при открытии случайной статьи на английской Википедии: {e}")
        break

# Скриншот английских вкладок
driver.save_screenshot("english_wiki_tabs.png")

# Получаем заголовки статей из открытых вкладок
titles = []
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    try:
        # Находим заголовок страницы
        title = driver.find_element(By.TAG_NAME, "h1").text
        titles.append(title)
    except Exception as e:
        print(f"Не удалось получить заголовок: {e}")

# Закрываем все вкладки с статьями
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    driver.close()

# Переключаемся на вкладку с конвертером (первая вкладка)
driver.switch_to.window(driver.window_handles[0])

# Вводим заголовки в поле конвертера для преобразования в base64
input_field = driver.find_element(By.ID, "encode")
input_field.clear()
input_field.send_keys("\n".join(titles))  # Вставляем все заголовки в поле
input_field.send_keys(Keys.RETURN)

# Получаем преобразованный текст в base64
encoded_text = driver.find_element(By.ID, "output").text

# Выводим заголовки и их base64 представление
for title in titles:
    encoded_title = base64.b64encode(title.encode("utf-8")).decode("utf-8")
    print(f"Title: {title} -> Base64: {encoded_title}")

# Скриншот консоли
driver.save_screenshot("console_output.png")

# Закрываем драйвер
driver.quit()
