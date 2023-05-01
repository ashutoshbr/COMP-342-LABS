# use homogeneous matrix
import pygame as pg
import numpy as np
from pygame import display, event
from pygame.locals import DOUBLEBUF, OPENGL

from OpenGL.GL import *
from OpenGL.GLU import *

START = [-0.5, -0.5]
END = [0.5, 0.5]
TRANSLATE_MATRIX = np.array([[1, 0, 0], [0, 1, 0.2], [0, 0, 1]])


def draw_line(matrix):
    for row in matrix:
        glVertex2d(row[0], row[1])


def main():
    pg.init()
    display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    display.set_caption("Mid point Circle drawing algorithm")
    # Set Color RED
    glColor3f(1.0, 0.0, 0.0)

    glBegin(GL_LINES)
    org = np.array([START, END])
    # Orginal line
    draw_line(org)
    # Transaltion for start point
    start = np.append(org[0], 1)  # append 1 to make it dimension compatible
    result1 = np.matmul(TRANSLATE_MATRIX, start)  # row * translate_matrix
    result1 = np.delete(result1, 2)  # delete appended 1
    # Transaltion for end point
    end = np.append(org[1], 1)
    result2 = np.matmul(TRANSLATE_MATRIX, end)
    result2 = np.delete(result2, 2)
    # Merge translated points for start and end
    result = np.array([result1, result2])
    print(result)
    # Translated line
    draw_line(result)
    glEnd()

    # clear buffer
    glFlush()
    # refresh
    pg.display.flip()
    while True:
        # Quitting PyGame windows
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()


if __name__ == "__main__":
    main()
