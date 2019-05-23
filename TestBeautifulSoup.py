from bs4 import BeautifulSoup
import requests

data = requests.get("https://www.google.com").content

soup = BeautifulSoup(data,"html.parser")
#print(soup.title)
#print(soup.title.text)
#print(soup.body)
#print(soup.body.div)
print(soup.body.div.attrs)
