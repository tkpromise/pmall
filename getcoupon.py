import requests
url = 'http://114.55.172.147:9701/DisountCouponsService.asmx?op=QueryCouponsListByMebID'

data = '<?xml version="1.0" encoding="utf-8"?>'
data += '<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">'
data += '<soap:Body>'
data += '<QueryCouponsListByMebID xmlns="www.mingyansoft.com">'
data += '<nMebID>'+'1986825'+'</nMebID>'
data += '<objCondition>'
data += '</objCondition>'
data += '<nPageSize>100</nPageSize>'
data += '<nPageNo>1</nPageNo>'
data += '</QueryCouponsListByMebID>'
data += '</soap:Body>'
data += '</soap:Envelope>'

headers = {'Content-Type': 'text/xml'}

re = requests.post(url, data=data, headers=headers)
print(re.text)

'''
    req = request.Request(url, data=data.encode('utf-8'), headers=headers)
    x = request.urlopen(req)

    xmlparse = xmltodict.parse(x)
'''
