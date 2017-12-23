import requests
import json

def send_sms(phone,code):
    s = requests.Session()
    r = s.get('https://sms.ru/sms/send?api_id=840F808A-2F0F-C4A7-A550-EFE303B2D557&to='+phone+'&msg=your code is '+code)
    print(r.text)


# send_sms('79050203259','12122AAS')