import math
import colorsys

import pygame

#initialising the window
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
hue = 0

#User Accepted inputs to create the desired Window
BG = input("Enter Background colour: ")
width = int(input("Enter Width: "))
height = int(input("Enter Height: "))
X_coord_Speed = float(input("Enter X-coordinate speed: "))
Y_coord_Speed = float(input("Enter Y-Coordinate Speed: "))
Hue_Speed = float(input("Enter Donut's colour changing speed: "))
print("Enjoy the Donut!")

#creating the window
window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
window_display = pygame.display.set_mode((width, height), pygame.RESIZABLE)

x_start, y_start = 0, 0
x_separator = 10
y_separator = 20

rows = height // y_separator
columns = width // x_separator
window_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2

Y, Z = 0, 0

a_space = 10
b_space = 1

#Chaarcters that will be in the donut
Characters = ".,?@!#$%&*~`//,21245>=][\|"

#Title of the window
pygame.display.set_caption("The Moving Donut")
font = pygame.font.SysFont('Arial', 24, bold=True)

#Colours of the donut
def color(r, g, b):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(r, g, b))


def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, color(hue, 1, 1))
    window.blit(text, (x_start, y_start))

#Running of the Donut
run = True
while run:
    window.fill(BG)

    z = [0] * window_size
    b = [' '] * window_size

    for j in range(0, 628, a_space):
        for i in range(0, 628, b_space):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(Y)
            f = math.sin(j)
            g = math.cos(Y)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(Z)
            n = math.sin(Z)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n))  # 3D x coordinate after rotation
            y = int(y_offset + 20 * D * (l * h * n + t * m))  # 3D y coordinate after rotation
            o = int(x + columns * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))  # luminance index
            if rows > y > 0 and 0 < x < columns and D > z[o]:
                z[o] = D
                b[o] = Characters[N if N > 0 else 0]
    if y_start == rows * y_separator - y_separator:
        y_start = 0
    for i in range(len(b)):
        Y += X_coord_Speed
        Z += Y_coord_Speed
        if i == 0 or i % columns:
            text_display(b[i], x_start, y_start)
            x_start += x_separator
        else:
            y_start += y_separator
            x_start = 0
            text_display((b[i]), x_start, y_start)
            x_start += x_separator

    pygame.display.update()

    hue += 0.01

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
