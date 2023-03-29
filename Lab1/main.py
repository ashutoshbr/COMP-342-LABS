import glfw
from OpenGL.GL import *
import math


def draw_triangle(x1, y1, x2, y2, x3, y3):
    glBegin(GL_TRIANGLES)
    # Plot the vertices
    glVertex2d(x1, y1)
    glVertex2d(x2, y2)
    glVertex2d(x3, y3)
    glEnd()


def draw_circle(x, y, radius, num_segments):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(x, y)
    for i in range(num_segments + 1):
        theta = 2.0 * math.pi * i / num_segments
        cx = radius * math.cos(theta)
        cy = radius * math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()


def draw_semi_circle(x, y, radius, num_segments):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(x, y)  # center point
    for i in range(num_segments + 1):
        angle = math.pi * i / num_segments
        cx = radius * math.cos(angle)
        cy = -radius * math.sin(angle)
        glVertex2f(x + cx, y + cy)
    glEnd()


def main():
    # Initialize the library
    if not glfw.init():
        return

    # Screen resolution
    monitor = glfw.get_primary_monitor()
    display_width, display_height = glfw.get_video_mode(monitor)[0]
    print(f"Screen resolution: {display_width}x{display_height}")

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

        # Sun
        draw_circle(-0.65, -0.5, 0.21, 100)
        # Moon
        draw_semi_circle(-0.65, 0.38, 0.21, 100)

        # Testing
        glColor3f(0, 0.207, 0.580)  # BLUE
        draw_triangle(-0.65, -0.18, -0.6, -0.3, -0.70, -0.3)
        draw_triangle(-0.49, -0.22, -0.6, -0.3, -0.5, -0.35)
        ####

        # Swap front and back buffers
        glfw.swap_buffers(window)
        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
