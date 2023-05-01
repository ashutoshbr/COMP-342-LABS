import pygame as pg
import numpy as np
from math import sin, cos, radians
from pygame import display, event
from pygame.locals import DOUBLEBUF, OPENGL

from OpenGL.GL import *
from OpenGL.GLU import *

START = [0, 0]
END = [0.5, 0.3]

# Matrices
ORG = np.array([START, END])  # orginal matrix
TRANSLATE_MATRIX = np.array([[1, 0, 0], [0, 1, 0.2], [0, 0, 1]])
ANGLE = radians(30)
ROTATE_MATRIX = np.array(
    [[cos(ANGLE), -sin(ANGLE), 0], [sin(ANGLE), cos(ANGLE), 0.2], [0, 0, 1]]
)
SCALE_MATRIX = np.array([[0.5, 0, 0], [0, 0.5, 0], [0, 0, 1]])
REFLECITON_MATRIX = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
SHEAR_MATRIX = np.array([[1, 1.5, 0], [1, 1, 0], [0, 0, 1]])


def draw_line(matrix):
    for row in matrix:
        glVertex2d(row[0], row[1])


def operation(OP_MATRIX):
    glBegin(GL_LINES)
    # Transaltion for start point
    start = np.append(ORG[0], 1)  # append 1 to make it dimension compatible
    result1 = np.matmul(OP_MATRIX, start)  # OP_MATRIX * ROW
    result1 = np.delete(result1, 2)  # delete appended 1
    # Transaltion for end point
    end = np.append(ORG[1], 1)
    result2 = np.matmul(OP_MATRIX, end)
    result2 = np.delete(result2, 2)
    # Merge translated points for start and end
    result = np.array([result1, result2])
    # Translated line
    draw_line(result)
    glEnd()


def translate():
    # Set Color RED
    glColor3f(1.0, 0.0, 0.0)
    operation(TRANSLATE_MATRIX)


def rotate():
    # Set Color GREEN
    glColor3f(0.0, 1.0, 0.0)
    operation(ROTATE_MATRIX)


def scale():
    # Set Color Blue
    glColor3f(0.0, 0.0, 1.0)
    operation(SCALE_MATRIX)


def reflection():
    # Ref against X axis
    glColor3f(0.5, 0.5, 0.5)
    operation(REFLECITON_MATRIX)


def shear():
    glColor3f(0.7, 0.8, 0.9)
    operation(SHEAR_MATRIX)


def main():
    pg.init()
    display.set_mode((800, 800), DOUBLEBUF | OPENGL)
    display.set_caption("Mid point Circle drawing algorithm")

    # Draw orginal line
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    draw_line(ORG)
    glEnd()

    # Transformations
    translate()
    rotate()
    scale()
    reflection()
    shear()

    glFlush()  # clear buffer
    pg.display.flip()  # refresh
    while True:
        # Quitting PyGame windows
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()


if __name__ == "__main__":
    main()
