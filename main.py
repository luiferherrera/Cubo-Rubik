import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from tkinter import *
from tkinter import messagebox as MessageBox
from cubo import Cubo

# creamos la ventana
ancho = 800
alto = 750
ventana = pygame.display.set_mode \
            ((ancho, alto), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Cubo Rubik')           

class Ver:
    def __init__(self):
        self.cubo = Cubo(-1, 2)
        self.controles()
        self.ver_Cubo()

    # ventana de controles    
    def controles(self):
        root = Tk()
        root.withdraw()
        MessageBox.showinfo("Controles", '''Para rotar el cubo use las flechas\n
Para rotar las caras use los nuemros de 1 al 6\nO las teclas: R, L, U, D, F, B\n
para rotar al revez use la tecla shift''')
        
    # visualizar en cubo
    def ver_Cubo(self):
        pygame.init()

        # creamos la "camara"
        glMatrixMode(GL_PROJECTION)
        gluPerspective(40, (ancho / alto ), 0.1, 50)
        glTranslatef(0.0, 0.0, -15)
        glRotatef(45, 1, 1, 0)
            
        # le damos color a la ventana    
        glClearColor(150/255, 255, 255, 0.89)

        x = 0
        y = 0
        while True:

            # detecta la tecla o bonton pulsado y realiza la accion

            # cerrar el programa
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # rotar las caras    
                if e.type == pygame.KEYDOWN:
                    k = pygame.key.get_pressed()
                    if k[pygame.K_RSHIFT] or k[pygame.K_LSHIFT]:
                        if e.key == pygame.K_r or e.key == pygame.K_1:
                            self.cubo.girar_X(1, 1)
                        elif e.key == pygame.K_l or e.key == pygame.K_2:
                            self.cubo.girar_X(-1, 1)
                        elif e.key == pygame.K_u or e.key == pygame.K_3:
                            self.cubo.girar_Y(1, 1)
                        elif e.key == pygame.K_d or e.key == pygame.K_4:
                            self.cubo.girar_Y(-1, 1)
                        elif e.key == pygame.K_f or e.key == pygame.K_5:
                            self.cubo.girar_Z(1, 1)
                        elif e.key == pygame.K_b or e.key == pygame.K_6:
                            self.cubo.girar_Z(-1, 1)
                    else:
                        if e.key == pygame.K_r or e.key == pygame.K_1:
                            self.cubo.girar_X(1, -1)
                        elif e.key == pygame.K_l or e.key == pygame.K_2:
                            self.cubo.girar_X(-1, -1)
                        elif e.key == pygame.K_u or e.key == pygame.K_3:
                            self.cubo.girar_Y(1, -1)
                        elif e.key == pygame.K_d or e.key == pygame.K_4:
                            self.cubo.girar_Y(-1, -1)
                        elif e.key == pygame.K_f or e.key == pygame.K_5:
                            self.cubo.girar_Z(1, -1)
                        elif e.key == pygame.K_b or e.key == pygame.K_6:
                            self.cubo.girar_Z(-1, -1)
                        

            # rotar el cubo completo
            k = pygame.key.get_pressed()
            if k[pygame.K_UP]:
                y += 5
            if k[pygame.K_DOWN]:
                y -= 5
            if k[pygame.K_RIGHT]:
                x -= 5
            if k[pygame.K_LEFT]:
                x += 5

           # renderizar de nuevo
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

            glRotatef(y, -1, 0, 0)
            glRotatef(x, 0, 1, 0)
            
            self.cubo.mostar()
            pygame.display.flip()

if __name__ == '__main__':
    rubiks_cube = Ver()
