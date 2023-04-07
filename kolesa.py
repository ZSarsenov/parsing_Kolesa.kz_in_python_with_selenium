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

# получаем каждую ссылку объявления на сайте
def take_all_links():
    browser.get(URL)
    links = []
    blocks = browser.find_element(By.CLASS_NAME, 'a-list').find_elements(By.CLASS_NAME, 'a-list__item')
    for block in blocks:
        link = block.find_element(By.TAG_NAME, 'a').get_attribute('href')
        links.insert(0, link)
    return links



# Проходимя по каждому блоку и собираем данные
def take_data_all_blocks(lists):
    for link in lists:
        browser.get(link)
        brand = browser.find_element(By.CLASS_NAME, 'offer__title').text
        price = browser.find_element(By.CLASS_NAME, 'offer__price').text
        city = browser.find_elements(By.TAG_NAME, 'dl')[0].text
        engine = browser.find_elements(By.TAG_NAME, 'dl')[3].text
        print(brand, price, engine, city)




    """    
        data_add = ''
        rastomozhen = ''
        probeg = ''
        color = ''
        photo = ''
    """

