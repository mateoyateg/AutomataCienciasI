from Algoritmo.BoyerMoore import BoyerMoore

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

def main():
    texto = "facasabfaabbdcasadkah ihaiodhamaraabdaab"
    BoyerMoore(texto, "mara").encontrarPatron()
    voltearCompleto(texto)
    voltearPalabras(texto)
    #fabfaabbdabdaab
if __name__ == "__main__":
    main()
