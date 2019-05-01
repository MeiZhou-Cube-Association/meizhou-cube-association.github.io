import re
import pandas as pd

def LocateTable():
    html_file = open("../index.html", encoding='utf-8')
    html = "".join("".join(html_file.readlines()).split('\n'))
    
    html_parts = re.split("<table.*?.</table>", html)
    return html_parts

def convertToHtml(title, result):
    d = {}
    index = 0
    for t in title:
        d[t]=result[index]
        index = index+1
    df = pd.DataFrame(d)
    df = df[title]
    h = df.to_html(index=False)
    return h

if __name__ == '__main__':
    result = [['2016-08-25','2016-08-26','2016-08-27'], ['张三','李四','王二'], ['0769', '0976', '0999']]
    title = ['日期', '姓名', '学号']
    print(convertToHtml(title, result))

