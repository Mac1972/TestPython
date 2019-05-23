from bs4 import BeautifulSoup
import requests

#baidu = requests.get("https://www.baidu.com")
baidu = requests.get("https://www.baidu.com").content
#print(baidu)
soup = BeautifulSoup(baidu,"html.parser")
#print(soup)
links = soup.findAll("a")
#print(links)
for link in links:
    #print(link)
    print(link.string)
