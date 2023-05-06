from my_array import Array
import random

class Cube():
    # Metodo constructor del Cube
    def __init__(self, rows, columns, depth, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns)
            for column in range(columns):
                self.data[row][column] = Array(depth, fill_value)

    # Metodo para obtener la altura del Cube = cant de filas:
    def __getheight__(self):
        return len(self.data)
    
    # Metodo para obtener el ancho del Cube = cant de columnas:
    def __getwidth__(self):
        return len(self.data[0])
    
    # Metodo para obtener la profundidad del Cube
    def __getdepth__(self):
        return len(self.data[0][0])
    
    # Metodo para obtener un valor en particular:
    def __getitem__(self, r_index, c_index, d_index):
        return self.data[r_index][c_index][d_index]
    
    # Metodo para cambiar un valor en particular:
    def __setitem__(self, r_index, c_index, d_index, value):
        self.data[r_index][c_index][d_index] = value

    # Metodo para devolver los valores en string:
    def __str__(self):
        result = ""
        for row in range(self.__getheight__()):
            if result != "":
                result += "\n"
            for column in range(self.__getwidth__()):
                if result != "":
                    result += "\n"
                for face in range(self.__getdepth__()):
                    if self.data[row][column][face] == None:
                        result += str(self.data[row][column][face]) + " | "
                    else:
                        if self.data[row][column][face] < 10:
                            result += " " + str(self.data[row][column][face]) + " | "
                        else:
                            result += str(self.data[row][column][face]) + " | "
        return result
    
    # Metodo para rellenar con numeros random mi cubo:
    def __randomdata__(self):
        for row in range(self.__getheight__()):
            for column in range(self.__getwidth__()):
                for face in range(self.__getdepth__()):
                    self.data[row][column][face] = random.randint(0,100)
    
    # Metodo para sumar todos los valores:
    def __sumdata__(self):
        sum = 0
        for row in range(self.__getheight__()):
            for column in range(self.__getwidth__()):
                for face in range(self.__getdepth__()):
                    sum += self.data[row][column][face]
        return sum

