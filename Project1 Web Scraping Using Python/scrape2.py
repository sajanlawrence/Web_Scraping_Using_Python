import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import sqlite3
conn = sqlite3.connect('links.sqlite')
cur = conn.cursor()

cur.executescript(
'''
DROP TABLE IF EXISTS Links;
CREATE TABLE Links(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	link TEXT UNIQUE
	);
'''
)
url = input("Enter url: ")
htm = urllib.request.urlopen(url).read()
soup = BeautifulSoup(htm,'html.parser')
#Retreive all anchor tags
tags = soup('a')
for tag in tags:
	#print(tag)
	link = tag.get('href',None)
	print(link)
	cur.execute('INSERT OR IGNORE INTO Links(link)VALUES(?)',(link,))
	conn.commit()	

# INPUT : https://www.wikipedia.com
