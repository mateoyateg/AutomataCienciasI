
class BoyerMoore():

    def __init__(self, cadena, palabra):
        self.__cadena = cadena
        self.__palabra = palabra

    def encontrarPatron(self):
        puntoInicio = len(self.__palabra)-1
        coincidencia = True


        for i in range(puntoInicio, -1, -1):
            if coincidencia:
                if self.__cadena[i] != self.__palabra[i]:
                    self.romperCadena((puntoInicio+1)-i)
                    coincidencia = False

        if coincidencia:
            print("Se encontro la palabra")

        else:
            self.encontrarPatron()

    def romperCadena(self, indice):
        self.__cadena = self.__cadena[indice:]
