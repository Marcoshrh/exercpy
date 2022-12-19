"""
Escreva um procedimento que receba um número arábico inteiro e imprima o
corresponde número em romano. Por exemplo, para 5 a saída desejada é “V”. A função deve ser
capaz de gerar o número romano para os 50 primeiros inteiros. Uma mensagem de erro deve ser mostrada caso um número fora
dessa faixa seja recebido. Crie também um algoritmo que leia um valor inteiro e chame
o procedimento criadoacima para a impressão do número romano.
"""


def printRoman(numero):
    num = [1, 4, 5, 9, 10, 40, 50]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L"]
    i = 6

    while numero:
        div = numero // num[i]
        numero %= num[i]

        while div:
            print(sym[i], end="")
            div -= 1
        i -= 1


if __name__ == '__main__':
    numero = int(input("Digite um número:"))
    print("Em romano:", end=" ")
    printRoman(numero)

