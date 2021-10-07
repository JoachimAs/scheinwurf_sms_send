import requests, sys
import xml.etree.ElementTree as ET
from datetime import datetime
import time
# check python version: python --version 
#
# when python not instsall requirements install python 
# https://projects.raspberrypi.org/en/projects/generic-python-install-python3
#
# execute file with variable
# example string: python sms_send.py +491622807261 "Hallo Joachim"

phone = sys.argv[1]
msg = sys.argv[2]

print("Phone " + str(phone))
print("msg " + str(msg))

# IP Adress of the Stick
ip = "192.168.8.1" 


# datetime object containing current date and time
now = datetime.now() 
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	
msg = dt_string + " " + msg


# get session
session = requests.Session()
# get token
r = session.get("http://%s/api/webserver/token" % ip)
root = ET.fromstring(r.content)
token = root[0].text
print("token " +str(token))

time.sleep(5)
# send sms
headers = { "__RequestVerificationToken": token, "Content-Type": "text/xml" }
data = "<request><Index>-1</Index><Phones><Phone>%s</Phone></Phones><Sca/><Content>%s</Content><Length>%d</Length><Reserved>1</Reserved><Date>$TIME</Date></request>" % ( phone, msg, len(msg) )
r = session.post( "http://%s/api/sms/send-sms" % ip, data=data, headers=headers )
print( "send-sms", r.headers, r.content)

#error
search_string = "error"
search_issue = r.content.find(search_string)

if search_issue > 0:
    i = 0
    while i < 1:
        headers = { "__RequestVerificationToken": token, "Content-Type": "text/xml" }
        data = "<request><Index>-1</Index><Phones><Phone>%s</Phone></Phones><Sca/><Content>%s</Content><Length>%d</Length><Reserved>1</Reserved><Date>$TIME</Date></request>" % ( phone, msg, len(msg) )
        r = session.post( "http://%s/api/sms/send-sms" % ip, data=data, headers=headers )
        print( "send-sms", r.headers, r.content) 
        search_issue = r.content.find(search_string)
        time.sleep(10)
        if search_issue == -1:
            i += 1

