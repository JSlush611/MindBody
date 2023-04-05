trinids = {
    '3': '100000237',
    '4': '100000215',
    '5': '100000216',
    '6': '100000217'
}

proxies = {
  'https': '192.126.154.27:8800',
  'https': '45.72.75.130:8800',
  'https':'193.168.183.32:8800',
  'https':'193.168.180.222:8800',
  'https':'193.168.182.28:8800',
  'https':'192.126.154.210:8800',
  'https':'192.126.206.113:8800',
  'https':'192.126.154.73:8800',
  'https': '192.126.206.241:8800',
  'https': '192.126.154.77:8800'
}

CSRF_LOCATOR = 'input.csrf-token'

valid_timeofday = ['AM', 'PM']
valid_days = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
valid_lanes = ['3','4','5','6']
valid_stimes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

HEADERS = {
  'Content-Length': '201',
  'Sec-Ch-Ua-Mobile': '?0',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'X-Requested-With': 'XMLHttpRequest',
  'Origin': 'https://clients.mindbodyonline.com',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'en-US,en;q=0.9',
}
CSRF_HEADERS = {
  'authority': 'clients.mindbodyonline.com',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'origin': 'https://clients.mindbodyonline.com',
  'referer': 'https://clients.mindbodyonline.com/ASP/su1.asp?studioid=25730&tg=&vt=&lvl=&stype=&view=&trn=0&page=&catid=&prodid=&date=10%2f12%2f2022&classid=0&prodGroupId=&sSU=&optForwardingLink=&qParam=&justloggedin=&nLgIn=&pMode=0&loc=1',
  'sec-ch-ua-mobile': '?0',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'x-requested-with': 'XMLHttpRequest'
}


LOGIN_URL = 'https://clients.mindbodyonline.com/Login?studioID=25730&isLibAsync=true&isJson=true'
LOGIN_PAYLOAD = 'requiredtxtUserName=username%40gmail.com&requiredtxtPassword=password&tg=&vt=&lvl=&stype=&qParam=&view=&trn=0&page=&catid=&prodid=&date=12%2F1%2F2022&classid=0&sSU=&optForwardingLink=&isAsync=false'

