import time
import threading
import logging

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

    def sacar(self, valorSaque):
        if self.validarSaldo(self.saldo, valorSaque) == True:
            self.saldo = self.saldo - valorSaque
        else:
            print("Saldo insuficiente.")
            return False


    def depositar(self, valorDeposito):
        self.saldo = self.saldo + valorDeposito

conta = Conta(1,"Teste", 100.00)
    
def AGastadora(Conta):
    while(True):
        time.sleep(3)
        Conta.sacar(10)
        print(Conta.saldo)

def AEsperta(Conta):
        time.sleep(3)
        Conta.sacar(50)
        print(Conta.saldo)

def AEconomica(Conta):
        time.sleep(3)
        Conta.sacar(5)
        print(Conta.saldo)

def APatrocinadora(Conta):
    if Conta.saldo == 0:
        Conta.depositar(100)


AGastadora(conta)