#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cha-price.py
#

import os, requests, json, pyfiglet

def btc_usd():
    btc_r = requests.get('https://mindicador.cl/api')
    data_b = btc_r.json()
    obj_b = json.dumps(data_b['bitcoin']['valor'])
    btc = float(obj_b)
    return btc

def cha_btc():
    cha_r = requests.get('https://www.southxchange.com/api/prices')
    data_c = cha_r.json()
    obj_c = json.dumps(data_c[35]['Last'])
    cha = float(obj_c)
    return cha

def in_clp():
    u = requests.get('https://mindicador.cl/api')
    data = u.json()
    clp = json.dumps(data['dolar']['valor'])
    clp = float(clp)
    return clp

def main():
    os.system("clear")
    logo = pyfiglet.figlet_format("CriptoPrecios")
    print(logo)
    cha = cha_btc()
    btc = btc_usd()
    clp = in_clp()
    btc_clp = btc * clp # Valor de Bitcoin en USD * valor del USD en CLP
    cha_clp = cha * btc_clp # Valor de Chaucha en BTC * valor de BTC en CLP

    print("El precio actual de la Chaucha (en BTCs) es: {0:.8f}".format(cha))
    print("El precio del BTC (en USD) es: {0:.2f}".format(btc))
    print("El precio del dolar en CLP es: {0:.2f}".format(clp))
    print("El precio actual de la Chaucha en CLP es: {0:.2f}".format(cha_clp))
    print("El precio del Bitcoin en CLP es: {0:.2f}".format(btc_clp))

if __name__ == '__main__':
    import sys
    sys.exit(main())
