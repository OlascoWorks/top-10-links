from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

SERVICE_PATH = "C:\Program Files (x86)\chromedriver.exe"
service = Service(SERVICE_PATH)
driver = webdriver.Chrome(service=service)

keyword = input("Please enter a search key:\t")
keyword_list = keyword.split()
if len(keyword_list) < 2:
    driver.get(f'https://google.co.in/search?q={keyword}')
else:
    url = f'https://google.co.in/search?q={keyword_list[0]}'
    for k in keyword_list[1:]:
        url = f'{url}+{k}'
    driver.get(url)
    

driver.implicitly_wait(15)
links = driver.find_elements(By.XPATH, "//a[@jsname='qOiK6e']")
titles = driver.find_elements(By.XPATH, "//h3[contains(@class, 'LC20lb')]")
sites = driver.find_elements(By.XPATH, "//span[@class='VuuXrf']")

links = links[:10]
titles = titles[:10]
sites = sites[:10]

for k in range(len(links)):
    link = links[k].get_attribute('href')
    title = titles[k].text
    site = sites[k].text
    print(f"{k+1}. Site - {site}\nTitle - {title}\nLink - {link}")