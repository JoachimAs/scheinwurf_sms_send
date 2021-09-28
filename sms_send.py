import requests, sys
import xml.etree.ElementTree as ET

msg = "From python for Chef"
phone = "+4916228" #To fill
ip = "192.168.8.1" #Dongle ip

# get session
session = requests.Session()
# get token
r = session.get("http://%s/api/webserver/token" % ip)
root = ET.fromstring(r.content)
token = root[0].text
print("token " +str(token))

# send sms
headers = { "__RequestVerificationToken": token, "Content-Type": "text/xml" }
data = "<request><Index>-1</Index><Phones><Phone>%s</Phone></Phones><Sca/><Content>%s</Content><Length>%d</Length><Reserved>1</Reserved><Date>$TIME</Date></request>" % ( phone, msg, len(msg) )
r = session.post( "http://%s/api/sms/send-sms" % ip, data=data, headers=headers )
print( "send-sms", r.headers, r.content)