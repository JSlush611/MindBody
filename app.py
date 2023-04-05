import requests
import time
from datetime import datetime
from data import *
from build import *

month = datetime.now().year
year = datetime.now().year
month = str(month)
year = str(year)

s = requests.Session()
s.proxies.update(proxies)

#Create cookies for requests
COOKIES = gather_Cookies()
print(COOKIES)
r = s.get('https://httpbin.org/ip')
print(r.json())

#Login with correct data
login_request = s.post(LOGIN_URL, cookies=COOKIES, headers=HEADERS, data=LOGIN_PAYLOAD)
print(login_request.content)

#Once logged in pull CSRF Token value for further requests
page_html = s.get('https://clients.mindbodyonline.com/ASP/main_info.asp', headers=CSRF_HEADERS, cookies=COOKIES).text
csrf_token = parse_Csrf(page_html)

#Check validity of all inputs, assign users inputs to values
validity, lane, day, stime, tod = gather_Input()

#Force user to enter inputs until they are true
while True:
    if validity is True:
        break
    else:
        validity, lane, day, stime, tod = gather_Input()

#Once input is valid, build CSRF token for booking the lane, and url to send request too
start = time.time()

POST_URL, CSRF = buildCsrf_URL(month, year, lane, day, stime, tod, csrf_token)

book_request = s.post(POST_URL, cookies=COOKIES, headers=HEADERS, data=CSRF)

booking_content = book_request.text 
matches = check_Success(booking_content)
print(booking_content)

end = time.time()
execution = end-start

if matches is True:
    print('Appointment not booked. Please try again.')  
else:
    print('Booked Lane ' + str(lane) + ' on ' + str(month) + '/' + str(day) + ' at ' + str(stime) + '-' + str(int(stime) + 1) + ' ' + str(tod) + '.')
    print('Completed in ' + str(execution) + ' seconds.')

