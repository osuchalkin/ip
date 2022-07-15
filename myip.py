#!/usr/bin/env python3

import requests

print("Simple information from https://api.myip.com about your current ip.\n")
# Создание вызова API и сохранение ответа.
url = 'https://api.myip.com'
try:
    r = requests.get(url)
    print(f"Status code: {r.status_code}\n")

    # Сохранение ответа API в переменной.
    response_dict = r.json()
    # Обработка результатов.
    print(f"[+] Your current IP: {response_dict['ip']}")
    print(f"[+] Your current country: {response_dict['country']}")
    print(f"[+] Your current country code: {response_dict['cc']}")
except requests.exceptions.ConnectionError:
    print(f"[-] Sorry, can not connect to {url}")

input('Press Enter to quit')