from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#saylankin damir 107b
driver = webdriver.Chrome()

URL = (r"https://ci.nsu.ru/news")


driver.get(URL)
driver.maximize_window()
print('\n')
time.sleep(3)

inputs = driver.find_elements(By.CSS_SELECTOR, ".form-control")

first_input = next((input for input in inputs if "C" in input.get_attribute('placeholder')), None)
second_input = next((input for input in inputs if "По" == input.get_attribute('placeholder')), None)



first_input.send_keys("01.10.2020")
second_input.send_keys("01.10.2024")
submit = driver.find_element(By.CSS_SELECTOR, ".btn-success")
submit.click()

time.sleep(3)



loadMore = driver.find_element(By.CSS_SELECTOR, ".loadMoreButton")
while True:
	try:
		loadMore = WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.CSS_SELECTOR, ".loadMoreButton"))
		)
		loadMore.click()
		time.sleep(2)
	except Exception as e:
		print(f"Error occurred: {e}")
		break

time.sleep(3)


with open('result.txt', 'w', encoding='utf-8') as file:
	news = driver.find_elements(By.CSS_SELECTOR, '.news-card') 
	for card in news:
		try:
			date = card.find_element(By.CSS_SELECTOR, '.date').text

			title_link = card.find_element(By.CSS_SELECTOR, '.name')
			title = title_link.text
			link = title_link.get_attribute('href')

			image_url = card.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')

			file.write(f'дата: {date}\n')
			file.write(f'Tназвание: {title}\n')
			file.write(f'ссылка на новость: {link}\n')
			file.write(f'ссылка на картинку: {image_url}\n\n')

		except Exception as e:
			print(f"ошибка: {e}")
#saylankin damir 107b
driver.quit()

