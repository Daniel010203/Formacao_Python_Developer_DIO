from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(site, 'html.parser')

temperatura = soup.find('span', class_='-text -bold -gray-dark-2 -font-55 _margin-l-15',
                         id='current-weather-temperature')

if temperatura is not None:
    print(temperatura.text)
else:
    print("A temperatura não foi encontrada.")
