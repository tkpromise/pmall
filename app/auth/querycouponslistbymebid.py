import re
import requests

def querycouponslistbymebid(mebid):
    url='http://114.55.172.147:9701/DisountCouponsService.asmx?op=QueryCouponsListByMebID'
    headers = {'Content-Type': 'text/xml'}
    data = '<?xml version="1.0" encoding="utf-8"?>'
    data += '<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">'
    data += '<soap:Body>'
    data += '<QueryCouponsListByMebID xmlns="www.mingyansoft.com">'
    data += '<nMebID>'+mebid+'</nMebID>'
    data += '<objCondition>'
    data += '</objCondition>'
    data += '<nPageSize>100</nPageSize>'
    data += '<nPageNo>1</nPageNo>'
    data += '</QueryCouponsListByMebID>'
    data += '</soap:Body>'
    data += '</soap:Envelope>'
    
    r = requests.post(url, data=data.encode('utf-8'), headers=headers)
    couponcountre = re.compile(r'(<RowCount>)(\d*)')
    couponcount = couponcountre.findall(r.text)[0][1]
    
    return couponcount

if __name__ == '__main__':
    querycouponslistbymebid('43172')
