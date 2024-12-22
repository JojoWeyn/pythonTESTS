#saylankin damir 107b
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.python.org/')

# 1. Найти изображение img в заголовке страницы h1 с использованием XPath и вывести ссылку на изображение
header_image = driver.find_element(By.XPATH, '//h1//img')
print("Ссылка на изображение заголовка:", header_image.get_attribute('src'))

# 2. Найти и вывести ссылки всех элементов «a» в разделе "About" с помощью XPath
about_links = driver.find_elements(By.XPATH, '//li[@id="about"]//a')
print("\nСсылки в разделе 'About':")
for link in about_links:
    print(link.get_attribute('href'))

# 3. Найти и вывести текст всех заголовков h2 на странице с помощью CSS-селектора
h2_headers = driver.find_elements(By.CSS_SELECTOR, 'h2')
print("\nЗаголовки h2 на странице:")
for header in h2_headers:
    print(header.text)

# 4. Найти и вывести ссылки всех элементов «a» в родительском контейнере Navigation Menu с использованием CSS-селектора
nav_links = driver.find_elements(By.CSS_SELECTOR, '#mainnav ul.menu li a')
print("\nНавигационные ссылки:")
for link in nav_links:
    print(link.get_attribute('href'))

# Закрыть браузер
driver.quit()
