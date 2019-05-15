import re
import requests
from pprint import pprint
from xml.etree.ElementTree import parse

def getpersonmemberbymobile(mobile):
    url = 'http://114.55.172.147:9701/MemberService.asmx?op=GetPersonMemberByMobile'
    data = '<?xml version="1.0" encoding="utf-8"?>'
    data += '<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">'
    data += '<soap:Body>'
    data += '<GetPersonMemberByMobile xmlns="http://www.mingyansoft.com/">'
    data += '<sMobile>'+mobile+'</sMobile>'
    data += '</GetPersonMemberByMobile>'
    data += '</soap:Body>'
    data += '</soap:Envelope>'
    
    headers = {'Content-Type': 'text/xml'}
    req = requests.post(url, data=data, headers=headers)
    getre = re.compile(r'Nick')
    get = getre.findall(req.text)
    if len(get):
        mebidre = re.compile(r'(<MebID>)(\d*)')
        mebid = mebidre.findall(req.text)
        return (mebid[0][1])
        #print (mebid[0][1])
    else:
        return False
        #print(False)

if __name__ == '__main__':
    getpersonmemberbymobile('18758831325')
