import pygame as pg
import numpy as np
import math

pg.init()
SIZE = WIDTH, HEIGHT = 800, 800
win = pg.display.set_mode(SIZE)

draw_points = []
heart_points = []
dif_step = []

down = False
drawn = False

count = 0
running = True
while running:
    pg.time.delay(10)
    win.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            down = True
        if event.type == pg.MOUSEBUTTONUP:
            down = False
            if not drawn:
                for t in np.linspace(0, 2 * math.pi, num=len(draw_points)):
                    x = (16 * math.sin(t)**3) * - 20
                    y = (13 * math.cos(t) - 5*math.cos(2*t) - 2*math.cos(3*t) - math.cos(4*t)) * - 20
                    # converted x and y to be at the right origin and integers
                    cx = int(x + WIDTH * 0.5)
                    cy = int(y + HEIGHT * 0.5)
                    p = cx, cy
                    heart_points.append(p)
                # print(heart_points, draw_points)
                dif_step = [((j[0] - draw_points[i][0])/300, (j[1] - draw_points[i][1])/300) for i, j in enumerate(heart_points)]
                print(dif_step)
            drawn = True
        if event.type == pg.MOUSEMOTION and down and not drawn:
            pos = pg.mouse.get_pos()
            print(pos)
            draw_points.append(pos)
    if len(draw_points) >= 2:
            pg.draw.aalines(win, (255, 0, 0), False, draw_points)
    if drawn:
        count += 1
        if count <= 300:
            draw_points = [(j[0] + dif_step[i][0], j[1] + dif_step[i][1]) for i, j in enumerate(draw_points)]
        
    pg.display.update()