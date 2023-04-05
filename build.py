from http.cookies import SimpleCookie
from data import *
import re
from bs4 import BeautifulSoup
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver as wd


wd = wd.Chrome(ChromeDriverManager().install())

def cookies_to_dict(rawdata):
    cookie = SimpleCookie()
    cookie.load(rawdata)
    cookies = {k: v.value for k, v in cookie.items()}
    return cookies

def gather_Cookies():
    wd.get('https://clients.mindbodyonline.com/ASP/su1.asp?studioid=25730&tg=&vt=&lvl=&stype=&view=&trn=0&page=&catid=&prodid=&date=11%2f24%2f2022&classid=0&prodGroupId=&sSU=&optForwardingLink=&qParam=&justloggedin=&nLgIn=&pMode=0&loc=1')
    cookies_list = wd.get_cookies()
    wd.close()

    cookies = {}
    for cookie in cookies_list:
        cookies[cookie['name']] = cookie['value']

    return cookies

def gather_Input():
    lane_input = input('Lane you want: ').strip()
    if (lane_input.isdigit()) and (lane_input in valid_lanes):
        lane_validity = True
    else:
        lane_validity = False
    
    day = input('Day you want lane (1 - 31 of month): ').strip()
    if (day.isdigit()) and (day in valid_days):
        day_validity = True
    else:
        day_validity = False  

    stime = input('Lane Start Time (4 am - 9 pm): ').strip()
    if (stime.isdigit()) and (stime in valid_stimes):
        stime_validity = True
    else:
        stime_validity = False

    timeofday = input('AM or PM: ').strip().upper()
    if (timeofday in valid_timeofday):
        timeofday_validity = True
    else:
        timeofday_validity = False

    if lane_validity is True and day_validity is True and stime_validity is True and timeofday_validity is True:
        return True, lane_input, day, stime, timeofday
    else:
        return False, lane_input, day, stime, timeofday


def parse_Csrf(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    csrf_value = soup.select_one(CSRF_LOCATOR).attrs['value']
    
    return csrf_value


def buildCsrf_URL(month, year, lane, day, stime, tod, csrf_token):
    trinid = trinids[lane]
    etime = int(stime) + 1
    etime = str(etime)
    csrf = 'CSRFToken='+(csrf_token)+'&frmApptDate='+(month)+'%2F'+(day)+'%2F'+(year)+'&frmPmtRefNo=245128&reSchedule=&origId=&frmRtnAction=appt_con.asp%3Floc%3D1%26tgid%3D11%26trnid%3D'+(trinid)+'%26rtrnid%3D'+(trinid)+'%26date%3D'+(month)+'%2F'+(day)+'%2F'+(year)+'%26clientid%3D%26Stime%3D'+(stime)+'%3A00%3A00+'+(tod)+'%26Etime%3D'+(etime)+'%3A00%3A00+'+(tod)+'%26rstime%3D%26retime%3D%26mask%3DFalse%26optResfor%3D&frmRtnScreen=appt_con&frmProdVTID=136&frmUseXRegDB=0&frmXStudioID=&optReservedFor=&optPaidForOther=&OptSelf=&optLocation=1&optInstructor='+(trinid)+'&optVisitType=136&frmClientID=100004287&frmTrainerID='+(trinid)+'&tgCapacity=1&optStartTime='+(stime)+'%3A00%3A00+'+(tod)+'&optEndTime='+(etime)+'%3A00%3A00+'+(tod)+'&txtNotes=&Submit=Book+Appointment&name=https%3A%2F%2Fclients.mindbodyonline.com%2Fclassic%2Fws%3Fstudioid%3D25730'
    post_url = 'https://clients.mindbodyonline.com/asp/adm/adm_appt_ap.asp?trnid='+(trinid)+'&rtrnid=&Date='+(month)+'%2F'+(day)+'%2F'+(year)+'&tgid=11&tgBlockLength=60&reSchedule=&origTrn=&origDate=&origId=&cType='

    return post_url, csrf

def check_Success(book_content):
    expression = 'The (appointment was not booked.)'
    expression1 = 'Scheduling (is currently closed )'
    matches = re.findall(expression, book_content)
    matches1 = re.findall(expression1, book_content)
    
    if matches or matches1:
        return True
    else:
        return False








