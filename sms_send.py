#!/usr/bin/env python3
"""
Example code on how to send a SMS, you can try it by running:
sudo apt install python3 idle3
pip3 install huawei-lte-api
nach einem Neustart muss gewartet werden
es können nicht mehrere SMS hintereinandener versendet werden
python3 sms_send.py http://192.168.8.1/ +491622807261 "Hello world"
"""
from argparse import ArgumentParser
from huawei_lte_api.Connection import Connection
from huawei_lte_api.Client import Client


parser = ArgumentParser()
parser.add_argument('url', type=str)
parser.add_argument('phone_number', type=str)
parser.add_argument('message', type=str)
parser.add_argument('--username', type=str)
parser.add_argument('--password', type=str)
args = parser.parse_args()

with Connection(args.url, username=args.username, password=args.password) as connection:
    client = Client(connection)
    if client.sms.send_sms([args.phone_number], args.message) == 'OK':
        print('SMS was send successfully')
    else:
        print('Error')