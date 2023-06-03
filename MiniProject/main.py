import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import time


# CONSTANSTS
CLOCK_RADIUS = 0.75  # Radius of the clock
HOUR_HAND_LENGTH = 0.4  # Length of the hour hand
MINUTE_HAND_LENGTH = 0.5  # Length of the minute hand
SECOND_HAND_LENGTH = 0.55  # Length of the second hand
FONT_SIZE = 64  # Font size for the digits of the clock


def draw_circle(x, y, radius, num_segments=100):
    glColor3f(0.1, 0.1, 0.1)  # Grey outer border
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(num_segments + 1):
        theta = 2.0 * math.pi * i / num_segments
        cx = radius * math.cos(theta)
        cy = radius * math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()


def draw_hour_hand(hour, minute, second):
    # Draw the hour hand
    glPushMatrix()
    glRotatef(-30 * (hour % 12) - 0.5 * minute - 0.0083333 * second, 0, 0, 1)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)  # Blue color
    glVertex2f(-0.02, 0)
    glVertex2f(0.02, 0)
    glVertex2f(0.02, HOUR_HAND_LENGTH)
    glVertex2f(-0.02, HOUR_HAND_LENGTH)
    glEnd()
    glPopMatrix()


def draw_minute_hand(minute, second):
    # Draw the minute hand
    glPushMatrix()
    glRotatef(-6 * minute - 0.1 * second, 0, 0, 1)
    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 0.0)  # Green color
    glVertex2f(-0.015, 0)
    glVertex2f(0.015, 0)
    glVertex2f(0.015, MINUTE_HAND_LENGTH)
    glVertex2f(-0.015, MINUTE_HAND_LENGTH)
    glEnd()
    glPopMatrix()


def draw_second_hand(second):
    # Draw the second hand
    glPushMatrix()
    glRotatef(-6 * second, 0, 0, 1)
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)  # Red color
    glVertex2f(-0.01, 0)
    glVertex2f(0.01, 0)
    glVertex2f(0.01, SECOND_HAND_LENGTH)
    glVertex2f(-0.01, SECOND_HAND_LENGTH)
    glEnd()
    glPopMatrix()


def drawText(x, y, text):
    font = pygame.font.SysFont("Inter Bold", FONT_SIZE)
    textSurface = font.render(text, True, (255, 255, 255)).convert_alpha()
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glWindowPos2d(x, y)
    glDrawPixels(
        textSurface.get_width(),
        textSurface.get_height(),
        GL_RGBA,
        GL_UNSIGNED_BYTE,
        textData,
    )


def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    width, height = 800, 800
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Mini Project: Analog Clock")

    # Main game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Get the current time
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        second = current_time.tm_sec

        # Function calls for drawing
        draw_circle(0, 0, CLOCK_RADIUS)
        draw_hour_hand(hour, minute, second)
        draw_minute_hand(minute, second)
        draw_second_hand(second)

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        drawText(380, 640, "12")  # Top
        drawText(395, 105, "6")  # Bottom
        drawText(120, 375, "9")  # Left
        drawText(650, 375, "3")  # Right

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
