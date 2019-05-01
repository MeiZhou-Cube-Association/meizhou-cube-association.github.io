import re
import pandas as pd

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
def ApplyCss():
    html_file = open("../index.html", encoding='utf-8')
    html = "".join(html_file)
    regex = re.compile("<table.*")
    return regex.sub('<table border="1" class="dataframe mystyle">', html)

if __name__ == '__main__':
    data_cols = [['2016-08-25','2016-08-26','2016-08-27'], ['张三','李四','王二'], ['0769', '0976', '0999']]
    title = ['日期', '姓名', '学号']
    print(ConvertToHtml(title, data_cols))
    html = ApplyCss()
    f = open("../index.html", encoding='utf-8', mode='w')
    f.write(html)

