import requests
from bs4 import BeautifulSoup as BS

#To get HTML Text
def getHTMLText(url):
    kv = {'user-agent':'Mozilla/5.0'}
    try:
        r = requests.get(url, timeout=30,headers = kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def getPersonList(personList,html):
    soup = BS(html,'html.parser')
    count=0 
    for tr in soup.tbody.find_all('tr'):
        personList.append([tr.td.div.label.input['data-name'],tr.td.div.label.input['data-id']])
        count+=1
    return count

def getPersonURL(personList):
    rootURL='https://cubingchina.com/results/person/'
    for eachPerson in personList:
        eachPerson.append(rootURL+eachPerson[1])
    
def getPersonInfo(personList):
    for eachPerson in personList:
        html = getHTMLText (eachPerson[2])
        soup = BS(html,'html.parser')
        eventsDict={}

        trList = soup.tbody.find_all('tr')
        trList = list(trList)
        for example in trList:
            try:
                '''
                print (example.td.i['title'])
                print (example('a')[1].string,'|',end='')
                print (example('a')[2].string)
                '''
                if len(example('a')) == 3:
                    eventsDict[ example.td.i['title'] ]= [ example('a')[1].string, example('a')[2].string ]
                elif len(example('a')) == 2:
                    eventsDict[ example.td.i['title'] ]= [ example('a')[1].string, ' ' ]
            except:
                continue
        eachPerson.append(eventsDict)
        return 
            