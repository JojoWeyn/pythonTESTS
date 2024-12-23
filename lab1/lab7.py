from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import base64
import os

# сайланкин дамир 107b
def setup_driver():
    """Настройка драйвера Chrome"""
    return webdriver.Chrome()

def create_screenshots_folder():
    """Создание папки для скриншотов"""
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    folder_name = f"screenshots_{timestamp}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name

def take_tabs_screenshot(driver, name, folder):
    """Сделать скриншот текущей вкладки"""
    full_screenshot_path = os.path.join(folder, f'{name}.png')
    driver.save_screenshot(full_screenshot_path)
    print(f"Сохранен скриншот: {full_screenshot_path}")

def open_new_tab(driver, url):
    """Открытие новой вкладки с указанным URL"""
    driver.execute_script(f"window.open('{url}', '_blank')")
    time.sleep(3)

def click_random_article(driver, is_russian=True):
    """Открытие случайной статьи"""
    try:
        if is_russian:
            driver.get("https://ru.wikipedia.org/wiki/Special:Random")
        else:
            driver.get("https://en.wikipedia.org/wiki/Special:Random")
        time.sleep(2)
    except Exception as e:
        print(f"Ошибка при открытии случайной статьи: {e}")

def get_random_articles(driver, wiki_window, screenshots_folder, num_articles=5):
    """Открытие случайных статей на википедии"""
    driver.switch_to.window(wiki_window)
    time.sleep(3)
    is_russian = 'ru.wikipedia' in driver.current_url
    wiki_type = "ru" if is_russian else "en"
    print(f"Работаем с {wiki_type} википедией")

    initial_handles = set(driver.window_handles)

    for i in range(num_articles):
        click_random_article(driver, is_russian)
        take_tabs_screenshot(driver, f'wiki_{wiki_type}_article_{i + 1}', screenshots_folder)

        if i < num_articles - 1:
            open_new_tab(driver, "https://ru.wikipedia.org" if is_russian else "https://en.wikipedia.org")
            driver.switch_to.window(driver.window_handles[-1])

def get_article_titles(driver):
    """Получение заголовков всех открытых статей"""
    titles = []
    main_windows = []

    for handle in driver.window_handles:
        try:
            driver.switch_to.window(handle)
            if 'wikipedia.org' in driver.current_url:
                try:
                    title_element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "h1.firstHeading, #firstHeading"))
                    )
                    title = title_element.text
                    if title:
                        titles.append(title)
                        print(f"Найден заголовок: {title}")
                except Exception as e:
                    print(f"Ошибка при получении заголовка: {e}")
            elif 'base64encode.org' in driver.current_url:
                main_windows.append(handle)
        except Exception as e:
            print(f"Ошибка при переключении окна: {e}")
            continue

    # Закрываем вкладки википедии
    for handle in driver.window_handles:
        if handle not in main_windows:
            driver.switch_to.window(handle)
            driver.close()

    # Возвращаемся на вкладку конвертера
    if main_windows:
        driver.switch_to.window(main_windows[0])

    return titles

def convert_to_base64(titles):
    """Конвертация заголовков в формат base64"""
    return [base64.b64encode(title.encode('utf-8')).decode('utf-8') for title in titles]

def main():
    screenshots_folder = create_screenshots_folder()
    driver = setup_driver()

    try:
        # 1. Открываем начальные вкладки
        driver.get("https://www.base64encode.org/")
        base64_window = driver.current_window_handle

        # Открываем википедии в новых вкладках
        open_new_tab(driver, "https://ru.wikipedia.org")
        open_new_tab(driver, "https://en.wikipedia.org")
        time.sleep(3)

        # Находим окна википедий
        wiki_windows = [handle for handle in driver.window_handles if handle != base64_window]
        ru_wiki_window = wiki_windows[0]
        en_wiki_window = wiki_windows[1]

        # 2. Открываем случайные статьи на русской википедии
        print("Открываем случайные статьи на русской википедии...")
        get_random_articles(driver, ru_wiki_window, screenshots_folder)

        # 3. Открываем случайные статьи на английской википедии
        print("Открываем случайные статьи на английской википедии...")
        get_random_articles(driver, en_wiki_window, screenshots_folder)

        # 4. Получаем заголовки статей
        print("Собираем заголовки статей...")
        titles = get_article_titles(driver)

        # 5. Конвертируем заголовки в base64
        base64_titles = convert_to_base64(titles)

        # Выводим результаты в консоль
        print("\nНайденные заголовки статей:")
        for i, title in enumerate(titles, 1):
            print(f"{i}. {title}")

        print("\nЗаголовки в формате base64:")
        for i, b64_title in enumerate(base64_titles, 1):
            print(f"{i}. {b64_title}")

        # Делаем скриншот консоли
        take_tabs_screenshot(driver, 'console_output', screenshots_folder)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    main()
