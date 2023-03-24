import time
import threading
from threading import Lock

def getPipoca():
    print(f'Pipoca pronta.')
    return "Pipoca pronta"

def getRefrigerante():
    print(f'Refrigerante pronto.')
    return "Refrigerante pronto"

def lanchePronto():
    print(f'Lanche pronto\n\n')
    return "Lanche pronto"



def main():
     while(True):
        t1 = threading.Thread(target=getPipoca)
        t2 = threading.Thread(target=getRefrigerante)

        #Inicia as Threads
        t1.start()
        t2.start()

        #Aguarda finalizar as Threads
        t1.join()
        t2.join()


        lanchePronto()
        time.sleep(5)


if __name__ == "__main__":
    main()