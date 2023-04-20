import pygame as pg
from pygame import display, event

from pygame.locals import DOUBLEBUF, OPENGL

from OpenGL.GL import *
from OpenGL.GLU import *


def BSA(start: tuple[int, int], end: tuple[int, int]):
    x1, y1 = start
    x2, y2 = end

    slope = abs((y2 - y1) / (x2 - x1))
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x, y = x1, y1

    vertices = []

    if slope < 1:
        for _ in range(dx):
            p = 2 * dy - dx
            x = x + 1
            if p < 0:
                vertices.append((x, y))
                p = p + 2 * dy
            else:
                y = y + 1
                vertices.append((x, y))
                p = p + 2 * (dy - dx)
    else:
        for _ in range(dy):
            p = 2 * dx - dy
            y = y + 1
            if p < 0:
                vertices.append((x, y))
                p = p + 2 * dx
            else:
                x = x + 1
                vertices.append((x, y))
                p = p + 2 * (dx - dy)

    return vertices


def main():
    pg.init()
    display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    display.set_caption("Bresenham Line Drawing algorithm")

    gluPerspective(60, 1, 10, 1000)
    glTranslatef(0.0, 0.0, -100)

    # Draw a line between two points
    vertices = BSA((0, 0), (25, 40))

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_STRIP)
    for v in vertices:
        x, y = v
        glVertex2f(x, y)
    glEnd()
    display.flip()

    while True:
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()


if __name__ == "__main__":
    main()
