import pandas as pd

from IMDB_scraper import imdb_scraper

Filmai = imdb_scraper()
# print(Filmai)

#filmai pagal abecele

Filmai_pgl_abecele = pd.DataFrame(Filmai)
Filmai_pgl_abecele.columns = ['Movie Name', 'Release Year', 'Lenght']

print(Filmai_pgl_abecele)