'''
Alunos:
Ricardo Faria da Costa RA: 02110199
Luiz Henrique Pinto Marques RA: 02110085

Turma: 3UMA - FEAU
'''

import csv
import numpy as np
import matplotlib.pyplot as plt

def graph_morte_casos_BR():
    casosAcumulados = np.array([])
    mortesAcumulados = np.array([])
    with open("owid-covid-data.csv", 'r') as f:
        arq = csv.reader(f, delimiter=",")
        for row in arq:
            if row[2] == "Brazil":
                casosAcumulados = np.append(casosAcumulados, row[4])
                if row[7] == '':
                    mortesAcumulados = np.append(mortesAcumulados, 0)
                else:
                    mortesAcumulados = np.append(mortesAcumulados, row[7])

        fig = plt.figure()

        plt.plot(mortesAcumulados, casosAcumulados, '--')
        limiteX = mortesAcumulados
        ticks = limiteX
        k = 50
        limiteX = limiteX[::k]
        labels = ticks[::k]
        plt.xticks(limiteX, labels, rotation='vertical')

        limiteY = casosAcumulados
        ticks = limiteY
        k = 50
        limiteY = limiteY[::k]
        labels = ticks[::k]
        plt.yticks(limiteY, labels, rotation='horizontal')

        plt.savefig('grafico_brasil_casosvsmortes.png')

        plt.show()

def graph_brasil_x_argentina():
    mortesBrasil = np.array([])
    mortesArgentina = np.array([])
    with open('owid-covid-data.csv') as f:
        arq = csv.reader(f, delimiter=',')
        dayArray = np.arange(1, 31)
        monthArray = np.array([4, 5])
        listDate = []
        for i in range(0, 1):
            for j in range(0, 30):

                date = f"2020-0{monthArray[i]}-{dayArray[j]}" if dayArray[j] >= 10 else f"2020-0" \
                f"{monthArray[i]}-0{dayArray[j]}"
                listDate.append(date)

        for row in arq:
            for i in range(0, 30):
                if row[2] == "Brazil" and listDate[i] in row[3]:
                    if row[7] == '':
                        mortesBrasil = np.append(mortesBrasil, 0)
                    else:
                        mortesBrasil = np.append(mortesBrasil, row[7])
                if row[2] == "Argentina" and listDate[i] in row[3]:
                    if row[7] == '':
                        mortesArgentina = np.append(mortesArgentina, 0)
                    else:
                        mortesArgentina = np.append(mortesArgentina, row[7])


        fig = plt.figure()
        plt.subplot(121)
        plt.plot(mortesBrasil, listDate, 'g')
        plt.title("Mortes no Brasil em Abril de 2020")

        plt.xticks(rotation="vertical")

        plt.subplot(122)
        plt.plot(mortesArgentina, listDate, 'b')
        plt.title("Mortes na Argentina em Abril de 2020")

        plt.xticks(rotation="vertical")

        plt.savefig("grafico_brasil_x_argentina.png")

        plt.show()

key_input = 0

while key_input != 3:
    print("--Menu interativo da covid-19--")
    print("1) Gráfico: Morte vs. Casos no Brasil")
    print("2) Gráfico: Comparação entre Brasil e Argentina em relação às mortes em Abril de 2020")
    print("3) Sair")
    key_input = int(input("Escolha um item do menu. (1-3)\n>>> "))
    if key_input == 1:
        print("-------")
        print("Iniciando gráfico...")
        print("-------")
        graph_morte_casos_BR()
        print("Salvando imagem...")
        print("-------")

    elif key_input == 2:
        print("-------")
        print("Iniciando gráfico...")
        print("-------")
        graph_brasil_x_argentina()
        print("Salvando imagem...")
        print("-------")

    elif key_input == 3:
        print("Finalizando...")
        break

    else:
        print("-- Opção inválida --")




