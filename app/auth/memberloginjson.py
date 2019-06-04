import re
import hashlib
import requests

def memberloginjson(username, password):
    password = hashlib.md5(password.encode('utf-8')).hexdigest()
    url='http://114.55.172.147:9701/MemberService.asmx?op=MemberLoginJson'
    headers = {'Content-Type': 'text/xml'}
    data = '<?xml version="1.0" encoding="utf-8"?>'
    data += '<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">'
    data += '<soap:Body>'
    data += '<MemberLoginJson xmlns="http://www.mingyansoft.com/">'
    data += '<sCondition>'+username+'</sCondition>'
    data += '<sPassword>'+password+'</sPassword>'
    data += '</MemberLoginJson>'
    data += '</soap:Body>'
    data += '</soap:Envelope>'
    
    r = requests.post(url, data=data.encode('utf-8'), headers=headers)
    loginre = re.compile(r'(<MemberLoginJsonResult>)(\w*)')
    login = loginre.findall(r.text)[0][1]
    if login == 'null':
        return False
    else:
        return True

if __name__ == '__main__':
    memberloginjson('18758831325', 'joy1986825')
