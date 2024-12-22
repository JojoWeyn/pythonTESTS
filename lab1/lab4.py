from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Создаем экземпляр драйвера
driver = webdriver.Chrome()

# Переходим на сайт vk.com/video
driver.get("https://vk.com/video")
time.sleep(5) # Ждем, пока страница загрузится

# Получаем ссылки на видео из разделов "Для вас" и "Тренды"
for section in ["Для вас", "Тренды"]:
    driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[{section}]').click()
    links = driver.find_elements(By.CSS_SELECTOR,'div.page_block div a')
    for link in links:
        print(link.get_attribute('href'))

# Сохраняем полученные ссылки в файл
with open('links.txt', 'w') as f:
    for link in links:
        f.write(link.get_attribute('href') + '\n')

# Переходим к каждому видео и получаем информацию
def get_video_info(url):
    driver.get(url)
    time.sleep(2)
    
    video_title = driver.find_elements(By.CSS_SELECTOR,'#page_header > h1').text
    views = driver.find_elements(By.CSS_SELECTOR,'#video_plays > span:nth-child(1)').text
    likes = driver.find_elements(By.CSS_SELECTOR,'#video_plays > span:nth-child(2)').text
    date = driver.find_elements(By.CSS_SELECTOR,'#date').text
    channel_name = driver.find_elements(By.CSS_SELECTOR,'#channel_info > strong').text
    subscribers = driver.find_elements(By.CSS_SELECTOR,'#subscribers').text
    
    return [video_title, views, likes, date, channel_name, subscribers]

# Проходимся по всем ссылкам и собираем данные
results = []
for url in links:
    results.append(get_video_info(url.get_attribute('href')))

# Выводим результаты в консоль
print("\n".join([", ".join(map(str, row)) for row in results]))

# Сохраняем результаты в файл
with open('video_data.csv', 'w') as f:
    f.write('\n'.join([", ".join(map(str, row)) for row in results]) + '\n')

# Закрываем драйвер
driver.quit()