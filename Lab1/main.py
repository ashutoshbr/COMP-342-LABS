import glfw
from OpenGL.GL import *


def main():
    # Initialize the library
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 800, "Triangle", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL

        glBegin(GL_TRIANGLES)
        glColor3f(1, 0, 0)
        glVertex2d(-0.5, -0.5)
        glVertex2d(0.5, 0)
        glVertex2d(0, 0.5)
        glEnd()

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
