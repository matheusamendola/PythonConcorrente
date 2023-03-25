import os
import threading

def threadArquivo(arquivoNome):
#  for arquivo in temp:
    with open(arquivoNome, 'r') as fp:
        line = fp.readline()
        while line != '':
          #Tratamento de string...
          #Printa a linha apenas se o aluno concluiu o curso.
          x = line.find("Concluído")
          if x != -1:
            print(line, end='')
          line = fp.readline()
        #print()

pasta = "cursos/"
temp = [pasta + arquivo for arquivo in os.listdir(pasta) if arquivo.endswith('.txt')]

threads = []
for arquivo in temp:
    t = threading.Thread(target=threadArquivo, args=[arquivo])
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()