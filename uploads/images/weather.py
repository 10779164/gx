# coding : UTF-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import csv
import requests
import re


def get_html(url):
    html = requests.get(url)
    #print html
    return html.text

def get_data(html):
    final = []
    #pattern = re.compile('<div id="7d" class="c7d">.*?<div>')
    ##ul = pattern.findall('<li .*?>.*?</li>')
    #ul =re.findall('<div id="7d" class="c7d">.*?</div>',html)
    ul = re.findall(r'<div class="i-weather">.*?</div>',html)
    return ul


def write_data(data, name):
    file_name = name
    with  open(file_name, 'a') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(data)

if __name__ == '__main__':
    html = get_html('http://weather.news.qq.com/index.shtml?icity=01011502')
    result = get_data(html)
    #write_data(result, 'weather.csv')
    print result
