import time
import threading
from threading import Lock
import logging

lock = Lock()
CountAGastadora = 0
CountAEsperta = 0
CountAEconomica = 0

class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def validarSaldo(self,saldo, valorSaque):
        if valorSaque > saldo:
            return False
        else:
            return True

    def sacar(self, valorSaque,funcao):
        with lock:
            if self.validarSaldo(self.saldo, valorSaque) == True:
                self.saldo = self.saldo - valorSaque
                print(f"Sacado: R${valorSaque} da função [{funcao}].\nSaldo: R${self.saldo}")
                return True

            else:
                print(f'Saldo insuficiente para: [{funcao}]')
                return False

    def depositar(self, valorDeposito):
        self.saldo = self.saldo + valorDeposito
        print(f'Depositado o valor: R${valorDeposito}')
        print(f'\nSaques efetuados: \nAGastadora: {CountAGastadora} \nAEsperta: {CountAEsperta} \nAEconomica: {CountAEconomica}\n')


conta = Conta(1,"Teste", 100)
    
def AGastadora(Conta):
    global CountAGastadora
    while(True):
        time.sleep(10)
        A = Conta.sacar(10,"AGastadora")
        if A == True:
            CountAGastadora += 1

def AEsperta(Conta):
    global CountAEsperta
    while(True):
        time.sleep(2)
        B = Conta.sacar(50,"AEsperta")
        if B == True:
            CountAEsperta =+ 1


def AEconomica(Conta):
    global CountAEconomica
    while(True):
        time.sleep(3)
        C = Conta.sacar(5,"AEconomica")
        if C == True:
            CountAEconomica += 1
        

def APatrocinadora(Conta):
    while(True):
        if Conta.saldo == 0:
            with lock:
                Conta.depositar(100)


t1 = threading.Thread(target=AGastadora, args=(conta,))

t2 = threading.Thread(target=AEsperta, args=(conta,))

t3 = threading.Thread(target=AEconomica, args=(conta,))

t4 = threading.Thread(target=APatrocinadora, args=(conta,))

t1.start()
t2.start()
t3.start()
t4.start()