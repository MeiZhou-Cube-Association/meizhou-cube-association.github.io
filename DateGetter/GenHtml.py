import re
import pandas as pd
from Spider import *

def LocateTable():
    html_file = open("../index.html", encoding='utf-8')
    html = "".join("".join(html_file.readlines()).split('\n'))
    
    html_parts = re.split("<table.*?.</table>", html)
    return html_parts

def ConvertToHtml(title, data_cols):
    d = {}
    index = 0
    for t in title:
        d[t]=data_cols[index]
        index = index+1
    df = pd.DataFrame(d)
    df = df[title]
    h = df.to_html(index=False)
    return h
def ADDLink(html, name_to_url):
    html_in_line = html.split('\n')
    print(html_in_line[11])
    print(html_in_line[17])
    print(html_in_line[23])
    print(html_in_line[11][10:-5])
    print(html_in_line[17][10:-5])
    print(html_in_line[23][10:-5])
    html_in_line[11] = "<td> <a href=\"%s\">%s</a> </td>"%(name_to_url[html_in_line[11][10:-5]], html_in_line[11][10:-5])
    html_in_line[17] = "<td> <a href=\"%s\">%s</a> </td>"%(name_to_url[html_in_line[17][10:-5]], html_in_line[17][10:-5])
    html_in_line[23] = "<td> <a href=\"%s\">%s</a> </td>"%(name_to_url[html_in_line[23][10:-5]], html_in_line[23][10:-5])
    html = "".join(html_in_line)
    return html

def ApplyCss():
    html_file = open("../index.html", encoding='utf-8')
    html = "".join(html_file)
    regex = re.compile("<table.*")
    return regex.sub('<table border="1" class="dataframe mystyle">', html)

if __name__ == '__main__':
    data_cols = [['张三','李四','王二而'], [666, 666, 666], ['2016-08-25','2016-08-26','2016-08-27'], ['0769', '0976', '0999']]
    title = ['姓名', '成绩', '日期', '详情']
    html = ConvertToHtml(title, data_cols)
    print(ConvertToHtml(title, data_cols))

    name_to_url = {}
    name_to_url['张三'] = 'https://www.baidu.com'
    name_to_url['李四'] = 'https://www.github.com'
    name_to_url['王二而'] = 'https://www.nwpu.edu.cn'
    html = ADDLink(html, name_to_url)

    # html = ApplyCss()
    f = open("../yayaya.html", encoding='utf-8', mode='w')
    f.write(html)

