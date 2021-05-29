import pygame
import constants

class Snake:

    rectangle_size = 20

    def __init__(self, x, y):
        self.rectangle_list = []

        first_rectangle = pygame.Rect(
            x,
            y,
            Snake.rectangle_size,
            Snake.rectangle_size,
        )
        self.rectangle_list.append(first_rectangle)

        self.length = 1
        self.x_change = 0
        self.y_change = 0


    def get_first_rectangle(self):
        return self.rectangle_list[-1]

    def draw_snake(self, window):

        for rectange in self.rectangle_list[:-1]:
            pygame.draw.rect(window, constants.GREEN, rectange)

        first_rectangle = self.get_first_rectangle()
        pygame.draw.rect(window, constants.LIGHT_GREEN, first_rectangle)


    def move_snake(self):

        first_rectangle = self.get_first_rectangle()

        new_x = first_rectangle.left + self.x_change
        new_y = first_rectangle.top + self.y_change

        new_rectangle = pygame.Rect(
            new_x,
            new_y,
            Snake.rectangle_size,
            Snake.rectangle_size,
        )
        self.rectangle_list.append(new_rectangle)

        if len(self.rectangle_list) > self.length:
            self.rectangle_list.pop(0)

    def is_outside_screen(self, window):
        first_rectangle = self.get_first_rectangle()
        window_rectangle = window.get_rect()

        return not window_rectangle.contains(first_rectangle)

    def is_crossing_itself(self):

        first_rectangle = self.get_first_rectangle()
        list_wo_first_rect = self.rectangle_list[:-1]

        collides_with = first_rectangle.collidelist(list_wo_first_rect)

        if collides_with == -1:
            return False

        return True


class Apple:

    rectangle_size = 20

    def __init__(self, x, y):
        self.rectangle = pygame.Rect(
            x,
            y,
            Apple.rectangle_size,
            Apple.rectangle_size
        )
        
    def draw_apple(self, window):
        pygame.draw.rect(window, constants.RED, self.rectangle)

    def is_eaten(self, head_rectangle):

        return self.rectangle.colliderect(head_rectangle)