from pieza import Pieza


class Cubo:
    def __init__(self, a, b):
        self.piezas = []
        self.crear_Cubo(a, b)

    # Crear la matriz que representa el cubo
    def crear_Cubo(self, a, b):
        for x in range(a, b):
            for y in range(a, b):
                for z in range(a, b):
                    self.piezas.append(Pieza(x, y, z))

    # Rotar las caras del cubo respecto a un eje
    def girar_X(self, cara, direccion):
        for cubo in self.piezas:
            if cubo.localizacion()[0] == cara:
                cubo.rotar_X(direccion)

    def girar_Y(self, cara, direccion):
        for cubo in self.piezas:
            if cubo.localizacion()[1] == cara:
                cubo.rotar_Y(direccion)

    def girar_Z(self, cara, direccion):
        for cubo in self.piezas:
            if cubo.localizacion()[2] == cara:
                cubo.rotar_Z(direccion)

    # imprimir la piezas 
    def mostar(self):
        for cubo in self.piezas:
            cubo.imprimir_P()

