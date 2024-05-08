from bs4 import BeautifulSoup 
import requests 
   
# lists 
urls=[] 
   
# function created 
def scrape(site): 
       
    # getting the request from url 
    r = requests.get(site) 
       
    # converting the text 
    s = BeautifulSoup(r.text,"html.parser") 
       
    for i in s.find_all("a"): 
          
        href = i.attrs['href'] 
           
        if href.startswith("/"): 
            site = site+href 
               
            if site not in  urls: 
                urls.append(site)  
                print(site) 
                # calling it self 
                scrape(site) 
   
# main function 
if __name__ =="__main__": 
   
    # website to be scrape 
    site="http://www.gonzaga.edu/"
   
    # calling function 
    scrape(site)

'''
url = 'https://www.gonzaga.edu'
page = requests.get(url)

# soup = BeautifulSoup(page.content, 'html.parser')

# # extract all text from the base page
# text = soup.get_text()
# text_lst = text.split('\n')
# cleaned_text = []
# for text in text_lst:
#   if len(text) > 0:
#     cleaned_text.append(text)

# print()

# # find all links to other pages
# links = []
# for link in soup.find_all('a', href=True):
#   links.append(link['href'])

html = str(page.content, 'utf-8')

soup = BeautifulSoup(html, 'html.parser')

# scraping
links = []
for link in soup.find_all('a', href=True):
  links.append(link['href'])

# look at text on each link
for link in links:
  if 'http' in link:
    continue

  url = 'https://www.gonzaga.edu' + link
  page = requests.get(url)
  html = str(page.content, 'utf-8')
  soup = BeautifulSoup(html, 'html.parser')
  text = soup.get_text()
  text_lst = text.split('\n')
  cleaned_text = []
  for text in text_lst:
    if len(text) > 0:
      cleaned_text.append(text)
  print(cleaned_text)
'''