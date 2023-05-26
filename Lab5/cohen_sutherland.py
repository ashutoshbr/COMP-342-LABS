import pygame
from pygame.locals import *
from OpenGL.GL import *

LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8


def compute_outcode(x, y, xmin, xmax, ymin, ymax):
    code = 0
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code


def cohen_sutherland(x1, y1, x2, y2, xmin, xmax, ymin, ymax):
    outcode1 = compute_outcode(x1, y1, xmin, xmax, ymin, ymax)
    outcode2 = compute_outcode(x2, y2, xmin, xmax, ymin, ymax)
    accept = False

    while True:
        if not (outcode1 | outcode2):
            # Trivially accept the line segment
            accept = True
            break
        elif outcode1 & outcode2:
            # Trivially reject the line segment
            break
        else:
            # Calculate intersection
            x = 0
            y = 0
            outcode = outcode1 or outcode2
            if outcode & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif outcode & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif outcode & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif outcode & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if outcode == outcode1:
                x1, y1 = x, y
                outcode1 = compute_outcode(x1, y1, xmin, xmax, ymin, ymax)
            else:
                x2, y2 = x, y
                outcode2 = compute_outcode(x2, y2, xmin, xmax, ymin, ymax)

    return accept, x1, y1, x2, y2


def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def init(width, height):
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -1, 1)
    glMatrixMode(GL_MODELVIEW)


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0, 0.0, 0.0)
    draw_line(50, 50, 200, 200)

    glColor3f(1.0, 0.0, 0.0)
    accept, x1, y1, x2, y2 = cohen_sutherland(50, 50, 200, 200, 100, 400, 100, 400)
    if accept:
        draw_line(x1, y1, x2, y2)

    pygame.display.flip()


def main():
    width = 500
    height = 500

    init(width, height)
    pygame.display.set_caption("cohen_sutherland.py")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
