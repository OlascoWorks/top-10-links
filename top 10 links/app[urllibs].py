from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

keyword = input("Please enter a search key:\t")
keyword_list = keyword.split()
if len(keyword_list) < 2:
    req = Request(
        url=f'https://google.co.in/search?q={keyword}', 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    html = urlopen(req).read()
else:
    url = f'https://google.co.in/search?q={keyword_list[0]}'
    for k in keyword_list[1:]:
        url = f'{url}+{k}'
    req = Request(
        url=url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    html = urlopen(req).read()

soup = BeautifulSoup(html, 'html.parser')
links = soup('a')[:10]
for index, link in enumerate(links):
    print(f'{index+1}. Tag - {link}\nLink - {link.get("href", None)}')