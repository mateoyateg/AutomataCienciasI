class BoyerMoore():

    def __init__(self, cadena, palabra):
        self.__cadena = cadena
        self.__palabra = palabra
        self.__texto = cadena
        self.__posicion = 0
        self.__listaCoincidencias = [0]
        self.__coincidencia = 0

    def encontrarPatron(self):
        puntoInicio = len(self.__palabra)-1
        coincidencia = True
        '''print(self.__cadena, "CADENA ENTRANTE")'''
        for i in range(puntoInicio, -1, -1):
            if coincidencia and len(self.__cadena)>=len(self.__palabra):
                if self.__cadena[i] != self.__palabra[i]:
                    self.romperCadena((puntoInicio+1)-i)
                    self.__posicion += ((puntoInicio+1)-i)
                    coincidencia = False

        if coincidencia and len(self.__cadena)>0:
            '''print(self.__posicion)
            print(self.__texto[self.__posicion:self.__posicion+len(self.__palabra)])
            print(len(self.__texto[:self.__posicion]))'''
            self.__listaCoincidencias.append(self.__posicion)
            self.__posicion=0
            if len(self.__listaCoincidencias) > 2:
                self.__listaCoincidencias[len(self.__listaCoincidencias)-1] = self.__listaCoincidencias[len(self.__listaCoincidencias)-1]+(self.__listaCoincidencias[len(self.__listaCoincidencias)-2]+len(self.__palabra))
            print("Se encontro la palabra en: ", self.__listaCoincidencias)
            self.romperCadena(len(self.__palabra))
            self.encontrarPatron()

        elif len(self.__cadena)>=len(self.__palabra):
            self.encontrarPatron()

        else:
            print("TERMINADO")
            self.verificar()

    def romperCadena(self, indice):
        '''print(indice)'''
        self.__cadena = self.__cadena[indice:]

    def verificar(self):

        for i in range(1, len(self.__listaCoincidencias)):
            '''print(self.__texto[self.__listaCoincidencias[i]:self.__listaCoincidencias[i]+len(self.__palabra)])'''

    def coin(self):

        if len(self.__listaCoincidencias)>1:
            return 1
        else:
            return 0

