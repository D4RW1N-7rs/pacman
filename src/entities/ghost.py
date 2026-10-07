"""Define ghost entities and their movement state.

This module contains the ghost's position, direction, identity, and movement
logic. Collision outcomes and score changes are left to the game rules layer
rather than being mixed into sprite rendering.
"""

import pygame


color_ghosts = {
    "cyan-D": pygame.image.load("img/ghosts/D/cyan-D.png"),
    "cyan-L": pygame.image.load("img/ghosts/L/cyan-L.png"),
    "cyan-R": pygame.image.load("img/ghosts/R/cyan-R.png"),
    "cyan-U": pygame.image.load("img/ghosts/U/cyan-U.png"),
    
    "orange-D": pygame.image.load("img/ghosts/D/orange-D.png"),
    "orange-L": pygame.image.load("img/ghosts/L/orange-L.png"),
    "orange-R": pygame.image.load("img/ghosts/R/orange-R.png"),
    "orange-U": pygame.image.load("img/ghosts/U/orange-U.png"),
    
    
}
import pygame
import random

U, D, R, L = 1, 4, 2, 8

class Ghost():
    def __init__(self, start_grid_x, start_grid_y, tile_size, color):

        self.pixel_x = start_grid_x * tile_size
        self.pixel_y = start_grid_y * tile_size
        self.start_x = start_grid_x
        self.start_y = start_grid_y
        self.color = color
        self.direction = "LEFT"
        self.speed = 4
        self.load_images()

    def load_images(self):

        self.images = {
            "LEFT": pygame.image.load(f"img/ghosts/L/{self.color}-L.png"),
            "RIGHT": pygame.image.load(f"img/ghosts/R/{self.color}-R.png"),
            "UP": pygame.image.load(f"img/ghosts/U/{self.color}-U.png"),
            "DOWN": pygame.image.load(f"img/ghosts/D/{self.color}-D.png")
        }

    def draw(self, window, padding, hud_height, tile_size):
        image = self.images[self.direction]

        offset_x = (tile_size - image.get_width()) // 2
        offset_y = (tile_size - image.get_height()) // 2

        draw_x = self.pixel_x + padding + offset_x
        draw_y = self.pixel_y + padding + hud_height + offset_y

        window.blit(image, (draw_x, draw_y))

    def update(self, maze, tile_size):
        
        options = []

        opposite = {
            "DOWN": "UP",
            "UP": "DOWN",
            "LEFT":"RIGHT",
            "RIGHT":"LEFT"
            }
        if self.pixel_x % tile_size == 0 and self.pixel_y % tile_size == 0 :
            grid_x = self.pixel_x // tile_size
            grid_y = self.pixel_y // tile_size
            
            cell = maze[grid_y][grid_x]

            if not (cell & U):
                options.append("UP") 
            if  not(cell & D):
                options.append("DOWN")
            if not(cell & R):
                options.append("RIGHT")
            if not(cell & L):
                options.append("LEFT")

            if len(options) > 1:
                opposite_direction = opposite[self.direction]
                if opposite_direction in options:
                    options.remove(opposite_direction)


            self.direction = random.choice(options)
        
        #move    
        if self.direction == "UP":
            self.pixel_y -= self.speed
        elif self.direction == "DOWN":
            self.pixel_y += self.speed
        elif self.direction == "LEFT":
            self.pixel_x -= self.speed
        elif self.direction == "RIGHT":
            self.pixel_x += self.speed
        

        # can_turn = False

        # if self.direction == "UP" and not (cell & U):
        #     can_turn = True
        # elif self.direction == "DOWN" and not(cell & D):
        #     can_turn = True
        # elif self.direction == "RIGHT" and not(cell & R):
        #     can_turn = True
        # elif self.direction == "LEFT" and not(cell & L):
        #     can_turn = True


# OK SF BARAK 3LIYA ANA DB DART INITIOLISATION DYAL GHOSTS CLASS
# GHADA INCHA ALLAH GHIAD NASLIHA HITACH SF 3AY9T 3LIHA OK
