# BeautifulSoup attempt at web scraping

from bs4 import BeautifulSoup
import requests

def scrape(site):
    urls = []
    r = requests.get(site)
    s = BeautifulSoup(r.text, "html.parser")

    # collect all links
    for link in s.find_all('a'):
        urls.append(link.get('href'))

    # remove duplicates
    urls = list(set(urls))

    # collect text data from base site and all linked sites
    text = ''
    for url in urls:
        try:
            r = requests.get(url)
            s = BeautifulSoup(r.text, "html.parser")
            text += s.get_text()
        except:
            pass
    
    # write text data to file
    with open('data.txt', 'w') as f:
        f.write(text)

scrape('https://www.gonzaga.edu')