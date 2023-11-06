import pandas as pd

from IMDB_scraper import imdb_scraper

Filmai = imdb_scraper()
# print(Filmai)

#filmai Pandos lenteleje

Filmai_sar= pd.DataFrame(Filmai)
Filmai_sar.columns = ['Movie Name', 'Year', 'Lenght']
# print(Filmai_sar)
# print(Filmai_sar.sort_values(by='Year', ascending=True))
print(Filmai_sar.sort_values(by='Lenght', ascending=True))
