# -*- coding: UTF-8 -*-

def buscar_linhas():
#    ler e retornar arquivo
    linhas = []
    with open('vida_loca.txt') as f:
        letras = f.readlines()

    for line in letras:
        linhas.append(line)

    return linhas


def tratando_dados(linhas):
    # contar a quantidade de palavras
    qnt = 0
    maior = []
    cao = []
    vogal = ""
    qntvogal = 0
    for c,i in enumerate(linhas):
      contagem = i.split(" ")
      qnt += len(contagem)
      for palavra in contagem:
        a = 0
        e = 0
        i = 0
        o = 0
        u = 0
        if (len(palavra)) not in maior:
          maior.append(len(palavra))
        if "ção" in palavra:
          cao.append(c+1)
        for letra in palavra:

          if "a" == letra:
            a += 1
          elif "e" == letra:
            e +=1
          elif "i" == letra:
            i += 1
          elif "o" == letra:
            o += 1
          elif "u" == letra:
            u += 1
          if a > e and a > i and a > o and a > u:
            vogal = "A"
            qntvogal += a
          elif e > i and e > o and e > u:
            vogal = "E"
            qntvogal += e
          elif i > o and i > u:
            vogal = "I"
            qntvogal += i
          elif  o > u:
            vogal = "O"
            qntvogal += o
          else: 
            vogal = "U"
            qntvogal += u
          
    maior.sort(reverse=True)
    return qnt, maior[0:5], cao, vogal, qntvogal


def escrever(quantidade, maiores, procurar, vogal, qntvogal):

    print("Quantidade de Palavras: ", quantidade, "\nQuantidade de letra nas maiores palavras: ", *maiores, "\n'ção' aparece nas linhas:", *procurar, "\nA vogal que mais aparece é '", vogal, "' com a quantidade de: ", qntvogal)


def main():
    # programa
    linhas = buscar_linhas()
    quantidade, maiores, procurar, vogal, qntvogal = tratando_dados(linhas)
    escrever(quantidade, maiores, procurar, vogal, qntvogal)