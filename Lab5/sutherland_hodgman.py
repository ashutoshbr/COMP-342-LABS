import pygame
from pygame.locals import *
from OpenGL.GL import *


def clip(subject_polygon, clip_polygon):
    def inside(p, cp1, cp2):
        return (cp2[0] - cp1[0]) * (p[1] - cp1[1]) > (cp2[1] - cp1[1]) * (p[0] - cp1[0])

    def intersect(cp1, cp2, s, e):
        dcx = cp1[0] - cp2[0]
        dcy = cp1[1] - cp2[1]
        dpx = s[0] - e[0]
        dpy = s[1] - e[1]
        n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
        n2 = s[0] * e[1] - s[1] * e[0]
        n3 = 1.0 / (dcx * dpy - dcy * dpx)
        return [(n1 * dpx - dcx * n2) * n3, (n1 * dpy - dcy * n2) * n3]

    output_polygon = subject_polygon.copy()
    cp1 = clip_polygon[-1]

    for cp2 in clip_polygon:
        input_polygon = output_polygon.copy()
        output_polygon = []

        s = input_polygon[-1]

        for e in input_polygon:
            if inside(e, cp1, cp2):
                if not inside(s, cp1, cp2):
                    output_polygon.append(intersect(cp1, cp2, s, e))
                output_polygon.append(e)
            elif inside(s, cp1, cp2):
                output_polygon.append(intersect(cp1, cp2, s, e))
            s = e

        cp1 = cp2

    return output_polygon


def draw_polygon(polygon):
    glBegin(GL_POLYGON)
    for point in polygon:
        glVertex2fv(point)
    glEnd()


def init(width, height):
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(0, width, 0, height, -1, 1)


def display(subject_polygon, clip_polygon):
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0, 0.0, 0.0)
    draw_polygon(subject_polygon)

    glColor3f(1.0, 0.0, 0.0)
    draw_polygon(clip_polygon)

    glColor3f(0.0, 0.0, 1.0)
    result_polygon = clip(subject_polygon, clip_polygon)
    draw_polygon(result_polygon)

    pygame.display.flip()


def main():
    width = 500
    height = 500

    subject_polygon = [(100, 100), (200, 100), (200, 200), (100, 200)]
    clip_polygon = [(150, 150), (250, 150), (250, 250), (150, 250)]

    init(width, height)
    pygame.display.set_caption("sutherland_hodgman.py")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display(subject_polygon, clip_polygon)
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
