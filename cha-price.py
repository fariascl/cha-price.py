#!/usr/bin/env python
import os, requests, json, pyfiglet

class Criptomoneda(object):
    def __init__(self, ticker):
        self.ticker = ticker

    def obtenerPrecio(self):
        url = "http://stats.orionx.com/ticker" #api
        r = requests.get(url)
        data = r.json()
        obj = json.dumps(data[str(self.ticker) + 'CLP']['lastPrice'])
        return int(obj)

def dolarinclp():
    r = requests.get('https://mindicador.cl/api')
    data = r.json()
    clp = json.dumps(data['dolar']['valor'])
    price = float(clp)
    return price

def main():
    os.system("clear")
    logo = pyfiglet.figlet_format("CriptoPrecios")
    print(logo)
    print(" --------------------------------------")
    print("|El precio actual del dolar es: " + str(dolarinclp()) + " |")
    print(" --------------------------------------")
    print(" 1) Chaucha (CHA)\n 2) Bitcoin (BTC)\n 3) Litecoin\n 4) Todas")

    try:
        opt = input(" Elige: ")
        if (opt == 1):
            moneda = Criptomoneda('CHA')
            print(" El precio de Chaucha en CLP es de: $" + str(moneda.obtenerPrecio()))

        elif (opt == 2):
            moneda = Criptomoneda('BTC')
            print(" El precio del Bitcoin en CLP es de: $" + str(moneda.obtenerPrecio()))

        elif (opt == 3):
            moneda = Criptomoneda('LTC')
            print(" El precio del Litecoin en CLP es de: $" + str(moneda.obtenerPrecio()))
        else:
            cha = Criptomoneda('CHA')
            btc = Criptomoneda('BTC')
            ltc = Criptomoneda('LTC')
            print(" El precio de Chaucha en CLP es de: $" + str(cha.obtenerPrecio()))
            print(" El precio de Bitcoin en CLP es de: $" + str(btc.obtenerPrecio()))
            print(" El precio de Litecoin en CLP es de: $" + str(ltc.obtenerPrecio()))
    except KeyboardInterrupt:
        print("\n Saliendo...")
        exit()

if __name__ == '__main__':
    import sys
    sys.exit(main())
