import pygame as pg
from pygame import display, event

from pygame.locals import DOUBLEBUF, OPENGL

from OpenGL.GL import *
from OpenGL.GLU import *

X_CENTER = Y_CENTER = 0.5
RADIUS = 100


def plot(x: int, y: int):
    glBegin(GL_POINTS)
    glVertex2f(x / 600 + X_CENTER, y / 600 + Y_CENTER)
    glEnd()


def mid_point_circle():
    x = 0
    y = RADIUS
    decision = 1 - RADIUS
    plot(x, y)

    while y > x:
        if decision < 0:
            x += 1
            decision += 2 * x + 1
        else:
            y -= 1
            x += 1
            decision += 2 * (x - y) + 1
        plot(x, y)
        plot(x, -y)
        plot(-x, y)
        plot(-x, -y)
        plot(y, x)
        plot(-y, x)
        plot(y, -x)
        plot(-y, -x)


def display_circle():
    glClear(GL_COLOR_BUFFER_BIT)

    # Set Color RED
    glColor3f(1.0, 0.0, 0.0)
    # Point Size is set to 2px
    glPointSize(2.0)

    mid_point_circle()

    # clear buffer
    glFlush()
    # refresh
    pg.display.flip()


def main():
    pg.init()
    display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    display.set_caption("Mid point Circle drawing algorithm")

    display_circle()
    while True:
        # Quitting PyGame windows
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()


if __name__ == "__main__":
    main()
