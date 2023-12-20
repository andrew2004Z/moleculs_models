# Импорт библиотек
import pygame
import OpenGL
from pygame import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# Константы
global quadricItem
quadricItem = gluNewQuadric()
global alfa
alfa = 0.0
n = 1

def draw(n, r, k):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    for _ in range(n):
        
        # 1 молекула
        glTranslated(0.75,-4,-0.75)
        glColor3d(1,1,1)
        gluSphere(quadricItem, 0.75, 25, 25)

        glTranslated(0.5,0,0)
        glRotatef(90,0,1,0)
        glColor3d(1,0,0)
        gluCylinder(quadricItem,0.2,0.2,1.75,4,4)

        glColor3d(1,1,1)
        glTranslated(0,0,1.5)
        gluSphere(quadricItem, 0.5, 25, 25)

        glTranslated(0.5,0,-2)
        glRotatef(90,0,1,0)
        glColor3d(1,0,0)
        gluCylinder(quadricItem,0.2,0.2,1.75,4,4)

        glColor3d(1,1,1)
        glTranslated(0,0,1.5)
        gluSphere(quadricItem, 0.5, 25, 25)

        # Соединение

        glTranslated(0,0,-2.5)
        glRotatef(150,0,1,0)
        glColor3d(1,0,0)
        gluCylinder(quadricItem,0.2,0.2,1.75,4,4)

        # 2 молекула

        glTranslated(0,0,1.75)
        glColor3d(1,1,1)
        gluSphere(quadricItem, 0.75, 25, 25)

        glTranslated(0.5,0,0)
        glRotatef(90,0,1,0)
        glColor3d(1,0,0)
        gluCylinder(quadricItem,0.2,0.2,1.75,4,4)

        glColor3d(1,1,1)
        glTranslated(0,0,1.5)
        gluSphere(quadricItem, 0.5, 25, 25)

        glTranslated(-0.5,0,-1.75)
        glRotatef(-90,0,1,0)
        glColor3d(1,0,0)
        gluCylinder(quadricItem,0.2,0.2,1.75,4,4)

        glColor3d(1,1,1)
        glTranslated(0,0,1.5)
        gluSphere(quadricItem, 0.5, 25, 25)

        # Соединение
        glTranslated(-1,0,-2.25)
        glRotatef(240,0,1,0)
        glColor3d(1,0,0)
        gluCylinder(quadricItem,0.2,0.2,1.75,4,4)
        
        # 3 молекула
        glTranslated(0,0,1.75)
        glColor3d(1,1,1)
        gluSphere(quadricItem, 0.75, 25, 25)

        glTranslated(0.5,0,0)
        glRotatef(90,0,1,0)
        glColor3d(1,0,0)
        gluCylinder(quadricItem,0.2,0.2,1.75,4,4)

        glColor3d(1,1,1)
        glTranslated(0,0,1.5)
        gluSphere(quadricItem, 0.5, 25, 25)

        glTranslated(-0.5,0,-1.75)
        glRotatef(-90,0,1,0)
        glColor3d(1,0,0)
        gluCylinder(quadricItem,0.2,0.2,1.75,4,4)

        glColor3d(1,1,1)
        glTranslated(0,0,1.5)
        gluSphere(quadricItem, 0.5, 25, 25)

        glTranslated(-0.75,0,-2)
        glRotatef(-120,0,1,0)
        glColor3d(1,0,0)
        gluCylinder(quadricItem,0.2,0.2,1.75,4,4)  

        
        glTranslated(-0.5,6,0)
        glRotatef(60,0,1,0)

    glPopMatrix()    

    # Управление
    if r:
        glRotatef(1,0,1,0)
    if k == 'L':
        glRotatef(-1,0,1,0)
    if k == 'R':
        glRotatef(1,0,1,0)
    if k == 'U':
        glRotatef(-1,1,0,1)
    if k == 'D':
        glRotatef(1,1,0,1)



def main():
    # Позиции освещения
    pos = (3,3,3,1)
    pos1 = (3,3,3,1)
    direc = (-1,-1,-1)

    # Окно
    pygame.init()
    display = (1200,900)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | GL_RGB | GL_DEPTH)
    gluPerspective(45, display[0]/display[1],2,50.0)

    glTranslatef(0.0,0.0,-20)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    # Цикл отрисовки
    n = 1
    r = True
    k = 'T'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                # Обработка кнопок
                if event.key == pygame.K_KP_PLUS:
                    n += 1
                elif event.key == pygame.K_KP_MINUS:
                    if n > 1:
                        n -= 1
                elif event.key == pygame.K_r:
                    if r:
                        r = False
                    else:
                        r = True
                elif event.key == pygame.K_RIGHT:
                    k = 'R'
                elif event.key == pygame.K_LEFT:
                    k = 'L'
                elif event.key == pygame.K_UP:
                    k = 'U'
                elif event.key == pygame.K_DOWN:
                    k = 'D'
                elif event.key == pygame.K_PAGEUP:
                    glEnable(GL_LIGHT0)
                elif event.key == pygame.K_PAGEDOWN:
                    glDisable(GL_LIGHT0)
                    glDisable(GL_LIGHTING)
        glEnable(GL_LIGHTING)
        glLightfv(GL_LIGHT2,GL_POSITION,pos1)
        glLightfv(GL_LIGHT2,GL_SPOT_DIRECTION,direc)
        glLightfv(GL_LIGHT0,GL_POSITION,pos)
        glLightfv(GL_LIGHT0,GL_SPOT_DIRECTION,direc)
        # Отрисовка
        draw(n, r, k)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()