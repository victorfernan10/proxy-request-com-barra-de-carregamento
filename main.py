import requests
import random
import time
import os
import sys
import threading

proxylist = 'path'

intervalo = 30



with open(proxylist) as o:
    proxies = [line.strip() for line in o.readlines()]

def barracharge():
        for i in range(intervalo):
            progresso = (i+1)/intervalo
            porc = int(progresso*100)
            barra = '•' * porc + '○' * (100 - porc)
            sys.stdout.write(f'\r[{barra}] {porc}%')
            sys.stdout.flush()
            time.sleep(1)


while True:
    proxy = random.choice(proxies)
    try:
        os.system('cls')
        resposta = requests.get('http://www.example.com', proxies={'http': proxy, 'https': proxy})
        print('Status da resposta:', resposta.status_code)
        ip = proxy.split(':')[0]
        r = requests.get(f"http://ipapi.co/{ip}/json/").json()
        cidade = r.get('city')
        pais = r.get('country')
        print(f'({ip}): Conectado em {cidade}, {pais}.')
        thread_barra = threading.Thread(target=barracharge)
        thread_barra.start()
        time.sleep(intervalo)


    except requests.exceptions.RequestException as e:
        print('Erro na solicitação, tentando nova proxy.')
        time.sleep(1)
        os.system('cls')
        print('Erro na solicitação, tentando nova proxy..')
        time.sleep(1)
        os.system('cls')
        print('Erro na solicitação, tentando nova proxy...')
        time.sleep(1)
    