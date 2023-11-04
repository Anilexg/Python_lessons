import requests
from bs4 import BeautifulSoup

def imdb_scraper():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
    }
    target = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    res = requests.get(target, headers=headers)
    # print(res.status_code)
    soup = BeautifulSoup(res.content, "html.parser")
    movies = soup.find_all('li', class_='ipc-metadata-list-summary-item sc-59b6048d-0 jemTre cli-parent')
    # print(movies)
    new_movies_list = []
    for movie in movies:
        pavadinimas = movie.find('h3', class_='ipc-title__text').text.strip()
        metai = movie.find('span', class_='sc-c7e5f54-8 hgjcbi cli-title-metadata-item').text.strip()
        ilgis =movie.find('div', class_='sc-c7e5f54-7 brlapf cli-title-metadata').text.strip()[4:10]

        new_movies_list.append((pavadinimas,metai, ilgis))
    # print(new_movies_list)

    return new_movies_list

# imdb_scraper()







