
print('CAR')
print('***************************')


class Vehicle:
    def __init__(self, maker, model):
        self.maker = maker
        self.model = model

    def printingMessage(self):
        return f"The maker is {self.maker} and the model is {self.model}"

class Car(Vehicle):  # Hereda de Vehicle
    def __init__(self, maker, model, doors):
        super().__init__(maker, model)
        self.doors = doors

    def infoPrinting(self):
        return f"The maker is {self.maker}, the model is {self.model}, and it has {self.doors} doors"

class Trunk(Vehicle):  # También hereda de Vehicle
    def __init__(self, maker, model, weight):
        super().__init__(maker, model)
        self.weight = weight

    def infoPrinting(self):
        return f"The maker is {self.maker}, the model is {self.model}, and it can carry {self.weight} kg"

# Crear objetos
vehicleObject = Vehicle('Generic', 'modelTX')
carObject = Car('Toyota', 'Yaris', 3)
trunkObject = Trunk('Hino', 'GH', 120)

# Imprimir resultados
print(vehicleObject.printingMessage())
print(carObject.infoPrinting())
print(trunkObject.infoPrinting())




