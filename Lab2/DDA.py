import pygame as pg
from pygame import display, event

from pygame.locals import DOUBLEBUF, OPENGL

from OpenGL.GL import *
from OpenGL.GLU import *


def DDA(start: tuple[int, int], end: tuple[int, int]):
    x1, y1 = start
    x2, y2 = end

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    steps = max(dx, dy)

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1
    vertices = []
    for _ in range(steps):
        vertices.append((x, y))
        x = x + x_inc
        y = y + y_inc
    return vertices


def main():
    pg.init()
    display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    display.set_caption("Digital Differential Analyzer Line drawing algorithm")

    gluPerspective(60, 1, 10, 1000)
    glTranslatef(0.0, 0.0, -100)

    # Draw a line between two points
    vertices = DDA((2, 3), (50, 20))

    # Red color
    glColor3f(1, 0, 0)
    glBegin(GL_LINE_STRIP)
    for v in vertices:
        x, y = v
        print(v)
        glVertex2f(x, y)
    glEnd()
    display.flip()

    while True:
        # Quitting PyGame windows
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()


if __name__ == "__main__":
    main()
