from bs4 import BeautifulSoup
import requests
import pandas as pd

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
    
    # convert text string to dataframe
    text = text.split('\n')
    text = pd.DataFrame(text, columns=['text'])

    # return text data
    return text

print(scrape('https://www.gonzaga.edu'))