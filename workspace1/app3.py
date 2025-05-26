
# def computeAreaSquare(side):
#     return side * side

# def computeAreaCircle(radius):
#     pi = 3.1415
#     return pi * radius ** 2

# print(f"The area of a square with side 3cm is {computeAreaSquare(3)}")
# print(f"The area of a circle with radius 3cm is {computeAreaCircle(3):.2f}")

# class Geometry:
#     print('Variable de clase')
#     print('****************************')

#     pi = 3.1415

#     def __init__(self, side, radius):
#         self.side = side
#         self.radius = radius
#         print("The object was created successfully!")

#     def area(self):
#         squareArea = self.side * self.side
#         circleArea = Geometry.pi * self.radius ** 2
#         return [squareArea, circleArea]

# areaSquareCircle = Geometry(3, 3)
# result = areaSquareCircle.area()
# print(f"The area of the square and circle are: {result[0]:.2f} and {result[1]:.2f}")


print('Ejercico #1 CREATE RECTANGLE')
print('***************************')

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Crear un objeto de la clase Rectangle
rect = Rectangle(5, 3)

# Llamar al método area para obtener el área del rectángulo
print(f"The area of the rectangle is: {rect.area()}")  # Output: 15



print("**STUDENT CLASS****")

import statistics

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        score = statistics.mean(self.grades)
        return score
        
# Crear instancias de la clase Student con listas (no conjuntos)
wilmerStudent = Student('wilmer', [6, 5, 4, 5, 10])
karenStudent = Student('karen', [8, 9, 8, 9, 10])
luisStudent = Student('luis', [6, 10, 10, 9, 7])

# Imprimir los promedios de cada estudiante
print(f"THE SCORE OF WILMER IS {wilmerStudent.average_grade():.2f}")
print(f"THE SCORE OF KAREN IS {karenStudent.average_grade():.2f}")
print(f"THE SCORE OF LUIS IS {luisStudent.average_grade():.2f}")

# Imprimir un mensaje de éxito
print("OK")


