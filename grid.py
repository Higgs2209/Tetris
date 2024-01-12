import pygame
from colors import Colors


class Grid:
    def __init__(self):

        # Set up columns, rows and cell sizes
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30

        # Create the grid list of lists full of 0's
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]

        # Get cell colours
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False


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
