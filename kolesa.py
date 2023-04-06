import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://kolesa.kz/cars/toyota/camry/avtokredit/aktau/?year[from]=2015&year[to]=2022'
data = {}

browser = webdriver.Chrome()

# берем последнию страницу пагинатора
def take_last_page_paginator():
    try:
        browser.get(URL)
        paginator_last_paginator = browser.find_element(By.CLASS_NAME, 'pager').find_elements(By.TAG_NAME, 'Li')[-1].text
        return int(paginator_last_paginator)
    except selenium.common.exceptions.NoSuchElementException:
        return 0

# парсим каджое объявление на сайте
def take_elements():
    browser.get(URL)
    blocks = browser.find_element(By.CLASS_NAME, 'a-list').find_elements(By.CLASS_NAME, 'a-list__item')

    for block in blocks:
        brend = block.find_element(By.CLASS_NAME, 'a-card__header').find_element(By.CLASS_NAME, 'a-card__title').text
        links = block.find_element(By.CLASS_NAME, 'a-card__picture').find_element(By.TAG_NAME, 'a').get_attribute('href')
        data = {
            'brend': brend,
            'url': links
        }

    """
    for link in links:
        browser.get(link)

        #city = browser.find_elements(By.CLASS_NAME, 'value-title')[0].text
        year = ''
        engine = ''
        data_add = ''
        rastomozhen = ''
        probeg = ''
        color = ''
        photo = ''
        #print(city)
    """
    print(data)
