

#encoding=utf-8


import os
import sys
import requests
import re
import random
reload(sys)
sys.setdefaultencoding('utf-8')


base_dir=r"C:\Users\Administrator\Desktop\Picture"
url=r"http://sj.zol.com.cn/bizhi/1080x1920/29.html"

def get_url():
    url=[]
    page=[ i for i in range(1,30) ]
    raw_url="http://sj.zol.com.cn/bizhi/1080x1920/"
    for i in page:
        real_url=raw_url+str(i)+".html"
        url.append(real_url)
    return url

def save_pic(page,pic_name,pic_src):
    path=os.path.join(base_dir,page)
    with open(pic_name+".jpg",'ab') as f:
        image=requests.get(pic_src)
        f.write(image.content)
        f.close()
        
def get_picture_url(url):
    #page=[]
    #pic=[]
    
    req=requests.get(url)
    #pattern=re.compile(r'<li class="photo-list-padding">.*?</li>')
    #pattern_page=re.findall(r'<a class=.*?>',req.text)
    pattern_page=re.findall(r'<img width=.*?>',req.text)
    page=pattern_page
    return page
    

def save_picture(page):
    len_page=len(page)
    for i in len_page:
        for j in page[i]:
            pass
            


if __name__=="__main__":
    a=get_picture_url(url)
    for i in a:
        i=i.decode('utf-8')
	print i.split('"')[9]
