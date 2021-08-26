from bs4 import BeautifulSoup
import requests

url = 'https://toppornsites.com/'

link = 'sites'

sites = []

jw = requests.get(url)
jw_soup = BeautifulSoup(jw.content, 'html.parser')
news_refactor = jw_soup.find_all('li', class_ = '')
# dummy = news_refactor.select('ol')

# print(dummy)

for news in news_refactor:
  print(news.select('a'))
#   sites.append(news.get('href'))

# print(sites)yyy


# with open(link, "r+") as file:
#   i = 0
#   while i < len(sites):
#     file.write(sites[i])
#     file.write("\n")
#     i += 1