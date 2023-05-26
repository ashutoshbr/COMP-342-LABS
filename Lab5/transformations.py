import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def init(width, height):
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (width / height), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)


def draw_cube():
    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1),
    )
    edges = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (0, 4),
        (4, 5),
        (4, 6),
        (5, 7),
        (6, 7),
        (3, 6),
        (3, 6),
        (2, 7),
        (1, 5),
    )

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def translate(x, y, z):
    glTranslatef(x, y, z)


def rotate(angle, x, y, z):
    glRotatef(angle, x, y, z)


def scale(x, y, z):
    glScalef(x, y, z)


def display(translate_vector, rotation_angle, rotation_axis, scale_vector):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    translate(*translate_vector)
    rotate(rotation_angle, *rotation_axis)
    scale(*scale_vector)

    glColor3f(0.0, 0.0, 0.0)
    draw_cube()

    glPopMatrix()

    pygame.display.flip()


def main():
    width = 800
    height = 600

    init(width, height)
    pygame.display.set_caption("3D Transformations")
    translate_vector = [0.5, 0.5, 0.5]
    rotation_angle = 45.0
    rotation_axis = [0.0, 1.0, 0.0]
    scale_vector = [0.5, 0.5, 0.5]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        translate_vector = [x + 0.0001 for x in translate_vector]
        rotation_angle += 1.0
        scale_vector = [x + 0.001 for x in scale_vector]
        display(translate_vector, rotation_angle, rotation_axis, scale_vector)
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
