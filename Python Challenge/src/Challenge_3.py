'''
Created on Mar 3, 2018

@author: Justin
'''


#3
#http://www.pythonchallenge.com/pc/def/equality.html

import re
import requests
from bs4 import BeautifulSoup
from bs4 import Comment

r = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
soup = BeautifulSoup(r.text, "html.parser")
cmt = soup.findAll(text=lambda text:isinstance(text, Comment))

for comments in soup.findAll(text=lambda text:isinstance(text, Comment)):
    equality = re.findall('(?<![A-Z]{1})[A-Z]{3}[a-z]{1}[A-Z]{3}(?![A-Z]{1})', comments)
    
print (equality)

for stuff in equality:
    equality2 = re.search('[a-z]', stuff).group()
    print(equality2)