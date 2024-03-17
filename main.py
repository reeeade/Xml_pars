import json

from bs4 import BeautifulSoup
from datetime import datetime

file = open('posts.xml')
soup = BeautifulSoup(file, 'lxml-xml')
data = {}
count = 1

for post in soup.find_all('entry'):
    title = post.find('title').get_text(strip=True).replace('\n', '')
    link = post.link['href']
    date_object = post.find('updated').text
    date = datetime.strptime(date_object, '%Y-%m-%dT%H:%M:%S%z')
    date = date.strftime('%Y-%m-%d')
    key = str(count) + ' post'
    data[key] = {'title': title, 'link': link, 'date': date}
    count += 1

    with open('posts.json', 'w') as f:
        json.dump(data, f, indent=4)
