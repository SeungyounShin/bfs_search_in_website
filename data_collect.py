from bs4 import BeautifulSoup
import urllib.request
import re
path = '/Users/seungyoun/Desktop/ImageFinder/retrieve'
url = 'http://www.thehook.co.kr'
from requests import get

def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)

html_page = urllib.request.urlopen(url)
soup = BeautifulSoup(html_page,'lxml')
lst = []

for img in soup.findAll('img'):
    img = img.get('src')
    if(img.find('footer')>=0 or img.find('banner')>=0):
        continue
    if(img.find('http')>=0):
        lst.append(img)
    else:
        lst.append(url+img)

for i in lst:
    if(i.find('/work/')<0):
        lst.remove(i)


def bfs(graph, root):
    visited, queue = [], [root]
    while queue:
        vertex = queue.pop(0)
        for w in graph[vertex]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
