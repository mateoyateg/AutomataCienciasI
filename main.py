from Algoritmo.BoyerMoore import BoyerMoore

import math

def verificaPalindromo(palabra):
    medio = int(math.ceil(len(palabra) / 2))
    varPal = True

    if len(palabra) > 0:

        inf = 0
        sup = len(palabra) - 1

        for i in range(0, medio):

            if palabra[inf] == palabra[sup]:
                varPal = True

            elif palabra[inf] != palabra[sup]:
                varPal = False
                return varPal

            inf += 1
            sup -= 1
    return varPal

def voltearCompleto(texto):
    invertido = texto[::-1]
    print("El texto completo invertido es: "+ invertido)

def voltearPalabras(texto):
    texto = texto.split(" ")
    for i in range (len(texto)):
        texto[i] = texto[i][::-1]
    final = ''
    for i in range (len(texto)):
        final += texto[i]
        final += " "
    print("El texto invirtiendo las palabras es: "+ final)

def mostrarPalabra(palabraInicial, palabraBuscada, palabraPalindroma):
    palabraPartida = []

    negrita = "\033[1;30m"
    sinNegrita = "\033[0;37m"

    negritaSub = "\033[4;30m"
    sinNegritaSub = "\033[0;37m"

    palabraPartida = palabraInicial.split(palabraBuscada)

    if palabraPalindroma:
        for i in range(len(palabraPartida)):
            print(sinNegritaSub + palabraPartida[i], end="")
            if i == len(palabraPartida) - 1:
                pass
            else:
                print(negritaSub + palabraBuscada, end="")

    else:
        for i in range(len(palabraPartida)):
            print(sinNegrita + palabraPartida[i], end="")
            if i == len(palabraPartida) - 1:
                pass
            else:
                print(negrita + palabraBuscada, end="")


def main():
    print("ALGORITMO DE BOYER MORE")

    texto = "holacasaholacasahola      casaholaholaholacasacasa"
    patron = "asa"

    BoyerMooreObj = BoyerMoore(texto, patron)

    BoyerMooreObj.encontrarPatron()

    ''''BoyerMoore(texto, patron).encontrarPatron()'''

    estado = BoyerMooreObj.coin()

    voltearCompleto(texto)
    voltearPalabras(texto)

    palabraPalindroma = verificaPalindromo(patron)
    print("¿La palabra es palindroma? " + str(palabraPalindroma))


    if estado == 1:
        mostrarPalabra(texto, patron, palabraPalindroma)
    else:
        print("No hay coincidencias...")
        print("Texto original: " + texto)


    #fabfaabbdabdaab
if __name__ == "__main__":
    main()
