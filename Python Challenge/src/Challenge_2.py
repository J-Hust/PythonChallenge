'''
Created on Mar 3, 2018

@author: Justin
'''

#2

import re
import requests
from bs4 import BeautifulSoup
from bs4 import Comment


#get comments string
r = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
soup = BeautifulSoup(r.text, "html.parser")

#find alpha characters in comments
for comments in soup.findAll(text=lambda text:isinstance(text, Comment)):
    ocr = re.findall('[abcdefghijklmnopqrstuvwxyz]', comments)
    
print (ocr)