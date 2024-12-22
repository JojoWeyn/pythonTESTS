from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

#сайланкин дамир 107b
driver = webdriver.Chrome()

driver.get('https://vk.com/video')

time.sleep(0.5)

def get_video_links():
    video_links = []
    

    links = driver.find_elements(By.XPATH, '//a[contains(@href, "/video")]')
    for link in links:
        href = link.get_attribute('href')
        print(href)
        if href and "video" in href:
            video_links.append(href)
    
    return video_links

video_links = get_video_links()
print(f"Количество ссылок на видео: {len(video_links)}")

def get_video_info(video_url):
    try:
        driver.get(video_url)
        time.sleep(2) 

        title = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="video_modal_title"]').text
        views_text = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="video_modal_additional_info"]').text
        views_data = views_text.split('·')
        views = views_data[0].strip()
        creation_date = views_data[1].strip() 
        likes = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="video_modal_like_button"]').text
        channel_name = driver.find_element(By.CSS_SELECTOR, 'a.vkuiLink.vkitLink__link--WXYoI.vkitLink__primary--ZZz2Q.vkuiTappable.vkuiTappable--hasPointer-none.vkuiClickable__resetLinkStyle.vkuiClickable__host.vkuiClickable__realClickable.vkui-focus-visible.vkuiRootComponent').text
        followers = driver.find_element(By.CSS_SELECTOR, 'span.vkuiSimpleCell__text.vkuiSimpleCell__subtitle.vkuiFootnote.vkuiTypography.vkuiRootComponent').text

        return [title, views, creation_date, likes, channel_name, followers]

    except Exception as e:
        print(f"Ошибка при обработке видео {video_url}: {e}")
        return None

video_info = []
for link in video_links:
    info = get_video_info(link)
    print(f"Информация о видео:{link}, {info}")
    if info:
        video_info.append(info)

with open('video_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow([len(video_links)])

    writer.writerow(['title', 'views', 'creation_date', 'likes', 'channel_name', 'followers'])

    for info in video_info:
        writer.writerow(info)

driver.quit()
