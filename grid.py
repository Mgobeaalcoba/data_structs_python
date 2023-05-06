# Grid es un array de dos dimensiones o Matriz tal como lo aprendí
# en UADE. 

from my_array import Array
import random

class Grid():
    # Metodo constructor del Grid
    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    # Metodo para obtener la altura del Grid = cant de filas:
    def __getheight__(self):
        return len(self.data)
    
    # Metodo para obtener el ancho del Grid = cant de columnas:
    def __getwidth__(self):
        return len(self.data[0])
    
    # Metodo para obtener un valor en particular:
    def __getitem__(self, r_index, c_index):
        return self.data[r_index][c_index]
    
    # Metodo para cambiar un valor en particular:
    def __setitem__(self, r_index, c_index, value):
        self.data[r_index][c_index] = value

    # Metodo para devolver los valores en string:
    def __str__(self):
        result = ""
        for row in range(self.__getheight__()):
            if result != "":
                result += "\n"
            for column in range(self.__getwidth__()):
                if self.data[row][column] == None:
                    result += str(self.data[row][column]) + " | "
                else:
                    if self.data[row][column] < 10:
                        result += " " + str(self.data[row][column]) + " | "
                    else:
                        result += str(self.data[row][column]) + " | "
        return result
    
    # Primer reto: 
    # Metodo para rellenar con numeros random:
    def __randomdata__(self):
        for row in range(self.__getheight__()):
            for column in range(self.__getwidth__()):
                self.data[row][column] = random.randint(0,100)

    # Metodo para sumar todos los valores:
    def __sumdata__(self):
        sum = 0
        for row in range(self.__getheight__()):
            for column in range(self.__getwidth__()):
                sum += self.data[row][column]
        return sum

