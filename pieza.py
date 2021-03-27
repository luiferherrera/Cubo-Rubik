import numpy as np
from OpenGL.GL import *

# Datos
vertices = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
            (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)]
esquinas = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6),
         (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
caras = [(0, 1, 2, 3), (5, 4, 7, 6), (4, 0, 3, 7), (1, 5, 6, 2),
            (4, 5, 1, 0), (3, 2, 6, 7)]
colores = [
    (0, 0, 255),  # azul
    (0, 255, 0),  # verde
    (255, 0.5, 0),  # anaranjado
    (255, 0, 0),  # rojo
    (255, 255, 0),  # amarillo
    (255, 255, 255)]  # blanco


class Pieza:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.tam = 0.5
        self.posicion = np.identity(3, int)

    # rotar las piezas multiplicando por la matriz de posicion
    def rotar_X(self, direccion):
        rotacion = np.matrix([[1, 0, 0], [0, 0, direccion], [0, -direccion, 0]])
        self.posicion = self.posicion * rotacion

    def rotar_Y(self, direccion):
        rotacion = np.matrix([[0, 0, -direccion], [0, 1, 0], [direccion, 0, 0]])
        self.posicion = self.posicion * rotacion

    def rotar_Z(self, direccion):
        rotacion = np.matrix([[0, direccion, 0], [-direccion, 0, 0], [0, 0, 1]])
        self.posicion = self.posicion * rotacion

    # obtiene la posicion actual de la pieza   
    def localizacion(self):
        act = np.matrix([self.x, self.y, self.z]) * self.posicion
        return act.item(0), act.item(1), act.item(2)

    # crea una matriz con las rotaciones para ser pasadas al OpenGL
    def matriz_P(self):
        a = np.size(self.posicion, 1)
        matriz = np.array(self.posicion)
        matriz = matriz.flatten()
        matriz_Opg = []
        for i in range(np.size(matriz)):
            matriz_Opg.append(matriz[i])
            if i % a == 2:
                matriz_Opg.append(0)
        matriz_Opg.extend([0, 0, 0, 1])
        return matriz_Opg

    # Imprimir las piezas
    def imprimir_P(self):
        glEnable(GL_DEPTH_TEST)

        glEnable(GL_POLYGON_OFFSET_FILL)
        glPolygonOffset(1.0, 1.0)

        # ver la pieza rotada
        glPushMatrix()
        glMultMatrixf(self.matriz_P())

        glTranslatef(self.x, self.y, self.z)
        glScalef(self.tam, self.tam, self.tam)

        # imprimir los esquinas
        glLineWidth(5)
        glColor3fv((0.2, 0.2, 0.2))
        glBegin(GL_LINES)
        for e in esquinas:
            glVertex3fv(vertices[e[0]])
            glVertex3fv(vertices[e[1]])
        glEnd()

        # imprimir las caras
        glBegin(GL_QUADS)
        for i in range(len(caras)):
            glColor3fv(colores[i])
            for j in caras[i]:
                glVertex3fv(vertices[j])
        glEnd()

        glPopMatrix()
