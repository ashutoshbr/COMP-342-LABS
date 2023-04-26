import pygame as pg
from pygame import display, event

from pygame.locals import DOUBLEBUF, OPENGL

from OpenGL.GL import *
from OpenGL.GLU import *

# Center
X_C = Y_C = 0.25
# Radius
R_X = 150
R_Y = 200


def plot(x: int, y: int):
    glBegin(GL_POINTS)
    # glVertex2f(x / 600 + X_C, y / 600 + Y_C)
    glVertex2f(X_C + x / 600, Y_C + y / 600)
    glVertex2f(X_C + x / 600, Y_C - y / 600)
    glVertex2f(X_C - x / 600, Y_C + y / 600)
    glVertex2f(X_C - x / 600, Y_C - y / 600)
    glEnd()


def mid_point_ellipse():
    # Region 1
    x = 0
    y = R_Y
    decision_1 = R_Y**2 - (R_X**2 * R_Y) + (1 / 4) * R_X**2

    dx = 2 * R_Y**2 * x
    dy = 2 * R_X**2 * y
    while dx < dy:
        plot(x, y)
        x += 1
        dx = 2 * R_Y**2 * x

        if decision_1 < 0:
            decision_1 += 2 * (R_Y**2 * x) + R_Y**2
        else:
            y -= 1
            dy = 2 * R_X**2 * y
            decision_1 += (dx - dy) + R_Y**2

    # Region 2
    decision_2 = (
        R_Y**2 * (x + 1 / 2) ** 2 + (R_X**2 * (y - 1) ** 2) - (R_X**2 * R_Y**2)
    )
    while y > 0:
        plot(x, y)
        y -= 1
        dy = 2 * R_X**2 * y

        if decision_2 > 0:
            decision_2 += -dy + R_X**2
        else:
            x += 1
            dx = 2 * R_Y**2 * x
            decision_2 += (dx - dy) + R_X**2


def display_ellipse():
    glClear(GL_COLOR_BUFFER_BIT)

    # Set Color RED
    glColor3f(1.0, 0.0, 0.0)
    # Point Size is set to 2px
    glPointSize(2.0)

    mid_point_ellipse()

    # clear buffer
    glFlush()
    # refresh
    pg.display.flip()


def main():
    pg.init()
    display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    display.set_caption("Mid point Ellipse drawing algorithm")

    display_ellipse()
    while True:
        # Quitting PyGame windows
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()


if __name__ == "__main__":
    main()
