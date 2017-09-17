from bs4 import BeautifulSoup
import urllib.request
from requests import get
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

main = 'topten'
url = 'http://www.topten10.co.kr'
path = '/Users/seungyoun/Desktop/ImageFinder/images/'

def link(url):
    lst = []
    html_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_page,'lxml')

    for link in soup.findAll('a'):
        i = link.get('href')
        try:
            if(i.find('facebook')>=0):
                continue
            elif(i.find('instagram')>=0):
                continue
            elif(i.find('naver')>=1):
                continue
            elif(i.find(main)>=0):
                lst.append(i)
            elif(i.find('/')==0):
                lst.append(url+'/'+i[1:])
            elif(i.find('./')==0):
                lst.append(url+i[1:])
            elif(i.find('./')==1):
                lst.append(url+i[2:])
            else:
                continue
        except:
            continue
    """
    for link in soup.findAll('script'):
        s = str(link)
        if(s.find('href')>=0):
            l,start,end = len(s),s.find('href')+6,0
            i = start
            while i<l:
                if(s[i] =='"'):
                    end = i
                    break
                    i += 1
            print(s[start:end])
            lst.append(url+s[start:end])
    """
    return lst

def ImgURL(url):
    lst = []
    html_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_page,'lxml')
    for img in soup.findAll('img'):
        img = img.get('src')
        if(img.find('facebook')>=0):
            continue
        elif(img.find('instagram')>=0):
            continue
        elif(img.find('naver')>=1):
            continue
        elif(img.find('footer')>=0):
            continue
        elif(img.find('banner')>=0):
            continue
        elif(img.find('http')>=0):
            lst.append(img)
        else:
            lst.append(url+img)
    return lst

def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)

def bfs(start):
    f = open(path+'img_and_url.txt', 'w')
    cnt,num_of_nodes,q,check = 0,0,[start],[start]
    while(len(q)>0):
        img_check = []
        node = q.pop(0)
        num_of_nodes +=1
        print("="*40)
        print("[",num_of_nodes,"] ",node)
        print("="*40)
        imgURLs = ImgURL(node)
        if(len(imgURLs)>0):
            for img in imgURLs:
                try:
                    img_check.index(img)
                except:
                    download(img,path+str(cnt)+'.jpg')
                    s = img+'|'+str(cnt)+'\n'
                    f.write(s)
                    print("[",num_of_nodes,"] ","Download img complete ",cnt)
                    cnt +=1
                    img_check.append(img)
        next_list = link(node)
        if(len(next_list)>0):
            for i in next_list:
                try:
                    check.index(i)
                except ValueError:
                    check.append(i)
                    q.append(i)
    f.close()
    return num_of_nodes

#search start
print(bfs(url))
print("FINISH")
