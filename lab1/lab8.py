from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Инициализация веб-драйвера
driver = webdriver.Chrome()

try:
    # Открыть Яндекс Переводчик
    driver.get("https://translate.google.com/")
    translator_tab = driver.current_window_handle  # Сохраняем вкладку переводчика

    # Открыть новую вкладку для стихов Пушкина
    driver.switch_to.new_window('tab')
    driver.get("https://www.culture.ru/literature/poems/author-aleksandr-pushkin")
    poems_tab = driver.current_window_handle  # Сохраняем вкладку со стихами

    # Извлечение ссылок на первые 2 стихотворения
    poem_links = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.ICocV"))
    )
    poem_links = [poem.get_attribute("href") for poem in poem_links[:2]]  # Берем только первые 2 стихотворения

    # Словарь для хранения результатов
    results = {}

    for i, link in enumerate(poem_links, start=1):
        # Переход к ссылке стихотворения
        driver.get(link)

        # Попытка развернуть текст, если есть кнопка "Развернуть"
        try:
            expand_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Развернуть']"))
            )
            expand_button.click()
        except TimeoutException:
            pass  # Если кнопки нет, продолжаем

        # Извлечение текста стихотворения
        title = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.rrWFt"))
        ).text

        poem_parts = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-content='text']"))
        )
        original_text = "\n".join([part.text for part in poem_parts])

        # Переключение на вкладку переводчика
        driver.switch_to.window(translator_tab)

        # Перевод текста
        input_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".er8xn"))
        )
        input_box.clear()
        input_box.send_keys(original_text)

        # Делаем ожидание перевода чуть дольше, чтобы полностью загрузился текст
        try:
            translated_text_element = WebDriverWait(driver, 5000).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[jsname='W297wb']"))
            )
            translated_text = translated_text_element.text
        except TimeoutException:
            translated_text = "Перевод не был получен."

        # Сохранение результата
        results[i] = {
            "title": title,
            "original": original_text,
            "translated": translated_text
        }

        # Возвращение на вкладку со стихами
        driver.switch_to.window(poems_tab)

    # Запись в текстовый файл
    with open("translated_poems.txt", "w", encoding="utf-8") as file:
        for i, data in results.items():
            file.write(f"Стихотворение {i}: {data['title']}\n")
            file.write("Оригинал:\n")
            file.write(data['original'] + "\n\n")
            file.write("Перевод:\n")
            file.write(data['translated'] + "\n\n")

finally:
    # Закрытие браузера
    driver.quit()
