import pygame

class Grid:
    def __init__(self):

        # Set up columns, rows and cell sizes
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30

        # Create the grid list of lists full of 0's
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]

        # Get cell colours
        self.colors = self.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    def get_cell_colors(self):

        # Set color values
        dark_grey = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)
        white = (255, 255, 255)
        dark_blue = (44, 44, 127)
        light_blue = (59, 85, 162)

        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]

    def draw(self, screen):
        # Iterate over the list to draw it
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]

                # Create a grid of invisible rectangles for the grid
                cell_rect = pygame.Rect(column * self.cell_size + 1, row * self.cell_size + 1,
                                        self.cell_size - 1, self.cell_size - 1)
                # Draw the grid
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
