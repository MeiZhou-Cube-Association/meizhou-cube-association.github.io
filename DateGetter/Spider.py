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
            
def printPersonInfo(personList,flag):
    if flag == 1:
        for person in personList:
            print (person[0],'\n',person[1])
            for item in person[3].keys():
                print (item,'  ',person[3][item][0],'|',person[3][item][1])
    else:
        print (len(personList),'items')
        for i in range(4):
            print (i+1,'. ',personList[i][0],'\n',personList[i][1])
        print ('......')
def GenMsg(personList, num):
    msg = ""
    if num == 1:
        for person in personList:
            # print (person[0],'\n',person[1])
            msg += str(person[0])+'\n'+str(person[1])+'\n'
            for item in person[3].keys():
                # print (item,'  ',person[3][item][0],'|',person[3][item][1])
                msg += str(item)+' '+str(person[3][item][0])+'|'+str(person[3][item][1])+'\n'
    else:
        # print (len(personList),'items')
        msg += str(len(personList))+' items'+'\n'
        for i in range(4):
            # print (i+1,'. ',personList[i][0],'\n',personList[i][1])
            msg += str(i+1)+'. '+str(personList[i][0])+'\n'+str(personList[i][1])+'\n'
        # print ('......')
        msg += '......'
    return msg

def main():
    keyWord = input('Please Input')
    rootURL = 'https://cubingchina.com/results/person?region=World&gender=all&name='
    personList=[]
    num = int()
    
    resultHTML = getHTMLText (rootURL+keyWord)
    num = getPersonList (personList, resultHTML)  
    getPersonURL(personList)
    getPersonInfo(personList)
    
    if num == 1:
        printPersonInfo(personList,flag = 1)
    else :
        printPersonInfo(personList,flag = 0)
    return 
def ProcessName(name):
    rootURL = 'https://cubingchina.com/results/person?region=World&gender=all&name='
    personList=[]
    num = int()
    
    resultHTML = getHTMLText (rootURL+name)
    num = getPersonList (personList, resultHTML)  
    getPersonURL(personList)
    getPersonInfo(personList)

    if num == 1:
        msg = GenMsg(personList, 1)
    else:
        msg = GenMsg(personList, 0)
    return msg

if __name__ == "__main__":
    main()
