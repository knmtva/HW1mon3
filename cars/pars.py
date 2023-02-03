import requests
from bs4 import BeautifulSoup as BS
from cars.db_cars import populate_cars

URL = 'https://www.mashina.kg/search/all/'

def par_car():
    response = requests.get(URL)
    if response.status_code == 200:
        soup = BS(response.text, 'html.parser')
        machine = soup.find_all('div', class_='list-item list-label')

        spisok = []
        for car in machine:
            diction = {
                'name': car.find('h2', class_='name').string.replace('\n', '').strip(),
                'price': car.find('p').find('strong').string.replace('\n', '').strip(),
                'description': car.find('div', class_='block info-wrapper item-info-wrapper'). \
                    find('p', class_='body-type').string.replace('\n', '').strip(),
                'link': 'https://www.mashina.kg' + car.find('a').get('href')
            }
            spisok.append(diction)
        populate_cars(spisok)

