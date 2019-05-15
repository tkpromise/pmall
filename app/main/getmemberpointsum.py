import re
import requests
from xml.etree.ElementTree import parse

def getmemberpointsum(mebid):
    url = 'http://114.55.172.147:9701/MemberService.asmx?op=GetMemberPointSum'
    data = '<?xml version="1.0" encoding="utf-8"?>'
    data += '<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">'
    data += '<soap:Body>'
    data += '<GetMemberPointSum xmlns="http://www.mingyansoft.com/">'
    data += '<nMebID>'+mebid+'</nMebID>'
    data += '</GetMemberPointSum>'
    data += '</soap:Body>'
    data += '</soap:Envelope>'
    
    headers = {'Content-Type': 'text/xml'}
    req = requests.post(url, data=data, headers=headers)
    pointsre = re.compile(r'(<GetMemberPointSumResult>)(\d*)')
    points = pointsre.findall(req.text)
    return (points[0][1])

if __name__ == '__main__':
    getmemberpointsum('43172')
