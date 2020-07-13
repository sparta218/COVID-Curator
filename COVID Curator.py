import datetime
import time
from bs4 import BeautifulSoup
import requests
from win10toast import ToastNotifier

pref_time = input('What time would you like to be notified? (HH:MM)')
TupleTime = (pref_time, ':00')
TupleTime = ''.join(TupleTime)
state = input('What state are you in?')

if ' ' in state:
    state = state.replace(' ', '-')

url = 'https://usafacts.org/visualizations/coronavirus-covid-19-spread-map/state/' + state
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

known = str(soup.find('p', attrs={"class":"jss19"}).get_text())
known = (known + ' Known Cases in ' + state.title())
print(known)

new_cases = str(soup.find('p', attrs={"class":"jss20"}).get_text())
new_cases = new_cases.replace('(', '')
new_cases = new_cases.replace(')', '')

toaster = ToastNotifier()

#Simplifies and compares system time to preferred time
#and notifies

s = ''

while True:
    ltime = (str(datetime.datetime.now()).split(' ', 1))
    del ltime[0]
    ltime = s.join(ltime).split('.', 1)
    del ltime[1]
    ltime = s.join(ltime)
    if ltime[-1] and ltime[-2] == '0':
        if ltime == (TupleTime):
            toaster.show_toast(known, new_cases, duration = 60)
            time.sleep(60)
    else: 
        time.sleep(1)
    
