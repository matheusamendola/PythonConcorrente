import random
from threading import Lock
from multiprocessing.pool import ThreadPool

#Variaveis para gerar o Array
min = 0
max = 1000
cols = 100
rows = 1000

totalArray = 0

lock = Lock()

#função que gera varios Array 
def genArray():
    Array = [random.choices(range(min,max), k=cols) for _ in range(rows)]
    return Array

#Soma o valor da Vetor 
def somaThread(valor):
    global totalArray
    with lock:
        totalArray = totalArray + valor

def main():
    ArraysList = genArray()

    #Inicia uma pool de Threads
    with ThreadPool() as pool:
        for count, value in enumerate(ArraysList):
            pool.map(somaThread, value)
            
            
    print(f'Total do Array: {totalArray}')

if __name__ == "__main__":
    main()



