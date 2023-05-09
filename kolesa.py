import csv
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://kolesa.kz/cars/toyota/camry/avtokredit/aktau/?year[from]=2015&year[to]=2022'
browser = webdriver.Chrome()

# берем последнию страницу пагинатора
def take_last_page_paginator():
    try:
        browser.get(URL)
        paginator_last_paginator = browser.find_element(By.CLASS_NAME, 'pager').find_elements(By.TAG_NAME, 'Li')[-1].text
        print(F'Вернул {paginator_last_paginator} страниц')
        return int(paginator_last_paginator)
    except selenium.common.exceptions.NoSuchElementException:
        return 1

# получаем каждую ссылку объявления на сайте
def take_all_links(pages):
    for page in range(1, 3):
        browser.get(f'{URL}&page={page}')
        links = []
        blocks = browser.find_element(By.CLASS_NAME, 'a-list').find_elements(By.CLASS_NAME, 'a-list__item')
        for block in blocks:
            link = block.find_element(By.TAG_NAME, 'a').get_attribute('href')
            links.append(link)
    return links


# Проходимя по каждому блоку и собираем данные
def take_all_data_blocks(take_all_links):
    data = {}
    for link in take_all_links:
        browser.get(link)
        brand = browser.find_element(By.CLASS_NAME, 'offer__title').text
        price = browser.find_element(By.CLASS_NAME, 'offer__price').text
        city = browser.find_elements(By.TAG_NAME, 'dl')[0].text.replace('\n', ' ')
        engine = browser.find_elements(By.TAG_NAME, 'dl')[3].text.replace('\n', '')
        milage = browser.find_element(By.CLASS_NAME, 'offer__parameters').find_elements(By.TAG_NAME, 'dl')[
            4].find_element(By.CLASS_NAME, 'value').text
        transmission = browser.find_element(By.CLASS_NAME, 'offer__parameters').find_elements(By.TAG_NAME, 'dl')[
            5].find_element(By.CLASS_NAME, 'value').text
        color = browser.find_element(By.CLASS_NAME, 'offer__parameters').find_elements(By.TAG_NAME, 'dl')[
            8].find_element(By.CLASS_NAME, 'value').text
        try:
            customs = browser.find_element(By.CLASS_NAME, 'offer__parameters').find_elements(By.TAG_NAME, 'dl')[9].find_element(By.CLASS_NAME, 'value').text
        except IndexError:
            customs = '___'
        data[link] = {'brand': brand, 'price': price, 'city': city, 'engine': engine, 'milage': milage, 'transmission': transmission, 'color': color, 'customs': customs}
    return data


# сохраняем в CSV
def save_to_CSV(take_all_data_blocks):
    # Создайте DataFrame из словаря
    with open('kolesa.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow((['URL', 'Brand', 'Price', 'City', 'Engine', 'Mileage', 'Transmission', 'Color', 'Customs']))
        for url, car_data in take_all_data_blocks.items():
            writer.writerow([url, car_data['brand'], car_data['price'], car_data['city'], car_data['engine'], car_data['milage'], car_data['transmission'], car_data['color'], car_data['customs']])



