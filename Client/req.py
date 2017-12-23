import requests
from flask import jsonify
import time
import json
# Не забудь проверить значение Verify
ver = '/home/ermac/Client/cert.pem'

def sessionM(address="localhost:5000"):
    s = requests.Session()
    r = s.get('https://'+address+'/login', verify=ver)
    # print(r.text)
    return {'s': s,'a': address}

def auth(f, login, password):
    s = f['s']
    address = f['a']
    data = {'username': login, 'password': password}
    r = s.post('https://'+address+'/login', data)
    print(r.text)
    if r.text == 'True':
        return True
    return False

def sms(f, sms):
    s = f['s']
    address = f['a']
    data = {'sms': sms}
    r = s.post('https://'+address+'/sms_detected', data)
    print(r.text)
    if r.text == 'True':
        return True
    return False

def get_data(f,user):
    s = f['s']
    address = f['a']
    r = s.get('https://'+address+'/index/'+user, verify=ver)
    # '/home/ermac/Client/cert.pem'
    # return jsonify(r.text)
    try:
        return r.json()
    except json.decoder.JSONDecodeError:
        return {"account":"some mistake in Server or Client"}
    
def logout(f):
    s = f['s']
    address = f['a']
    r = s.get('https://'+address+'/logout', verify=ver)
    return True
