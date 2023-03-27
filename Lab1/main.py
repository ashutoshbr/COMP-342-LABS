import glfw
from OpenGL.GL import *
import numpy as np


def draw_triangle(x1, y1, x2, y2, x3, y3):
    glBegin(GL_TRIANGLES)
    # Plot the vertices
    glVertex2d(x1, y1)
    glVertex2d(x2, y2)
    glVertex2d(x3, y3)
    glEnd()


def main():
    # Initialize the library
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 800, "Flag of Nepal", None, None)
    if not window:
        glfw.terminate()
        raise Exception("Error while creating glfw window")

    glfw.set_window_pos(window, 400, 200)
    # Make the window's context current
    glfw.make_context_current(window)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        glColor3f(0, 0.207, 0.580)  # BLUE
        draw_triangle(-1, 1, 0.3, 0.01, -1, 0.01)
        draw_triangle(-1, 0.6, 0.3, -1, -1, -1)

        glColor3f(0.866, 0.047, 0.223)  # RED
        draw_triangle(-0.95, 0.9, 0.15, 0.06, -0.95, 0.06)
        draw_triangle(-0.95, 0.46, 0.15, -0.95, -0.95, -0.95)

        # Swap front and back buffers
        glfw.swap_buffers(window)
        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
