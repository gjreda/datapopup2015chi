from bs4 import BeautifulSoup
import requests

url = ('http://www.chicagomag.com/Chicago-Magazine/November-2012/'
        'Best-Sandwiches-in-Chicago-Old-Oak-Tap-BLT/')
r = requests.get(url)
soup = BeautifulSoup(r.text)

sandwich = soup.find('h1', class_='headline').get_text()
desc = soup.find_all('p')[0].get_text()

# ugly code FTW - actually what I wrote
addy = soup.find('p', class_='addy').em.get_text()
foo = addy.split(',')[0].strip()
price = foo.partition(" ")[0].strip()
address = foo.partition(" ")[2].strip()
