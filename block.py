import pygame

WIDTH_NUM = 9    # number of block in width
HEIGHT_NUM = 9   # number of block in height
BLOCK_SIZE = 80  # size of block

# some colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (125, 0, 125)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)


class Block():

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.location_x = x * BLOCK_SIZE
        self.location_y = y * BLOCK_SIZE

        self.fill_color = WHITE
        self.border_color = BLACK

        # f = g + h
        self.f = 0
        self.g = 0
        self.h = 0

        self.text_size = BLOCK_SIZE // 6
        self.type = 0
        self.father= -1
        self.father_direction = -1

    # 添加文本
    def draw_text(self, text, x, y):
        font = pygame.font.Font('freesansbold.ttf', self.text_size)
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    # 画箭头
    def draw_direction(self):
        # down right
        if self.father_direction == 0:
            pygame.draw.polygon(self.screen, BLACK, (
                (self.location_x + 3 * BLOCK_SIZE // 4,
                 self.location_y + 3 * BLOCK_SIZE // 4),
                (self.location_x + 5 * BLOCK_SIZE // 8,
                 self.location_y + 3 * BLOCK_SIZE // 4),
                (self.location_x + 3 * BLOCK_SIZE // 4,
                 self.location_y + 5 * BLOCK_SIZE // 8),
            ))
            pygame.draw.line(self.screen, BLACK,
                             (self.location_x + BLOCK_SIZE // 4,
                              self.location_y + BLOCK_SIZE // 4),
                             (self.location_x + 3 * BLOCK_SIZE // 4,
                              self.location_y + 3 * BLOCK_SIZE // 4))
        # down
        elif self.father_direction == 1:
            pygame.draw.polygon(self.screen, BLACK, (
                (self.location_x + BLOCK_SIZE // 2,
                 self.location_y + BLOCK_SIZE - BLOCK_SIZE // 8),
                (self.location_x + 3 * BLOCK_SIZE // 8,
                 self.location_y + BLOCK_SIZE - BLOCK_SIZE // 4),
                (self.location_x + 5 * BLOCK_SIZE // 8,
                 self.location_y + BLOCK_SIZE - BLOCK_SIZE // 4),
            ))
            pygame.draw.line(self.screen, BLACK,
                             (self.location_x + BLOCK_SIZE // 2,
                              self.location_y + BLOCK_SIZE // 8+10),
                             (self.location_x + BLOCK_SIZE // 2,
                              self.location_y + 3 * BLOCK_SIZE // 4))
        # down left
        elif self.father_direction == 2:
            pygame.draw.polygon(self.screen, BLACK, (
                (self.location_x + BLOCK_SIZE // 4,
                 self.location_y + 3 * BLOCK_SIZE // 4),
                (self.location_x + BLOCK_SIZE // 4,
                 self.location_y + 5 * BLOCK_SIZE // 8),
                (self.location_x + 3 * BLOCK_SIZE // 8,
                 self.location_y + 3 * BLOCK_SIZE // 4),
            ))
            pygame.draw.line(self.screen, BLACK,
                             (self.location_x + 3 * BLOCK_SIZE // 4,
                              self.location_y + BLOCK_SIZE // 4),
                             (self.location_x + BLOCK_SIZE // 4,
                              self.location_y + 3 * BLOCK_SIZE // 4))
        # right
        elif self.father_direction == 3:
            pygame.draw.polygon(self.screen, BLACK, (
                (self.location_x + 7 * BLOCK_SIZE // 8,
                 self.location_y + BLOCK_SIZE // 2),
                (self.location_x + 3 * BLOCK_SIZE // 4,
                 self.location_y + 3 * BLOCK_SIZE // 8),
                (self.location_x + 3 * BLOCK_SIZE // 4,
                 self.location_y + 5 * BLOCK_SIZE // 8),
            ))
            pygame.draw.line(self.screen, BLACK,
                             (self.location_x + BLOCK_SIZE // 8,
                              self.location_y + BLOCK_SIZE // 2),
                             (self.location_x + 3 * BLOCK_SIZE // 4,
                              self.location_y + BLOCK_SIZE // 2))

        # left
        elif self.father_direction == 4:
            pygame.draw.polygon(self.screen, BLACK, (
                (self.location_x + BLOCK_SIZE // 8,
                 self.location_y + BLOCK_SIZE // 2),
                (self.location_x + BLOCK_SIZE // 4,
                 self.location_y + 3 * BLOCK_SIZE // 8),
                (self.location_x + BLOCK_SIZE // 4,
                 self.location_y + 5 * BLOCK_SIZE // 8),
            ))
            pygame.draw.line(self.screen, BLACK,
                             (self.location_x + BLOCK_SIZE // 4,
                              self.location_y + BLOCK_SIZE // 2),
                             (self.location_x + 7 * BLOCK_SIZE // 8,
                              self.location_y + BLOCK_SIZE // 2))
        # up right
        elif self.father_direction == 5:
            pygame.draw.polygon(self.screen, BLACK, (
                (self.location_x + 3 * BLOCK_SIZE // 4,
                 self.location_y + BLOCK_SIZE // 4),
                (self.location_x + 3 * BLOCK_SIZE // 4,
                 self.location_y + 3 * BLOCK_SIZE // 8),
                (self.location_x + 5 * BLOCK_SIZE // 8,
                 self.location_y + BLOCK_SIZE // 4),
            ))
            pygame.draw.line(self.screen, BLACK,
                             (self.location_x + BLOCK_SIZE // 4,
                              self.location_y + 3 * BLOCK_SIZE // 4),
                             (self.location_x + 3 * BLOCK_SIZE // 4,
                              self.location_y + BLOCK_SIZE // 4))
        # up
        elif self.father_direction == 6:
            pygame.draw.polygon(self.screen, BLACK, (
                (self.location_x + BLOCK_SIZE // 2,
                 self.location_y + BLOCK_SIZE // 8+10),
                (self.location_x + 3 * BLOCK_SIZE // 8,
                 self.location_y + BLOCK_SIZE // 4+10),
                (self.location_x + 5 * BLOCK_SIZE // 8,
                 self.location_y + BLOCK_SIZE // 4+10),
            ))
            pygame.draw.line(self.screen, BLACK,
                             (self.location_x + BLOCK_SIZE // 2,
                              self.location_y + BLOCK_SIZE // 4+10),
                             (self.location_x + BLOCK_SIZE // 2,
                              self.location_y + 7 * BLOCK_SIZE // 8))
        # up left
        elif self.father_direction == 7:
            pygame.draw.polygon(self.screen, BLACK, (
                (self.location_x + BLOCK_SIZE // 4,
                 self.location_y + BLOCK_SIZE // 4),
                (self.location_x + BLOCK_SIZE // 4,
                 self.location_y + 3 * BLOCK_SIZE // 8),
                (self.location_x + 3 * BLOCK_SIZE // 8,
                 self.location_y + BLOCK_SIZE // 4),
            ))
            pygame.draw.line(self.screen, BLACK,
                             (self.location_x + BLOCK_SIZE // 4,
                              self.location_y + BLOCK_SIZE // 4),
                             (self.location_x + 3 * BLOCK_SIZE // 4,
                              self.location_y + 3 * BLOCK_SIZE // 4))

    def draw_rect(self):
        pygame.draw.rect(self.screen, self.fill_color, [
            self.location_x, self.location_y, BLOCK_SIZE, BLOCK_SIZE], 0)

        pygame.draw.rect(self.screen, self.border_color, [
            self.location_x, self.location_y, BLOCK_SIZE, BLOCK_SIZE], 3)

    def draw(self):
        self.draw_rect()

        padding_x = 10
        padding_y = 10
        if self.type != 0:
            self.draw_text(str(self.f), self.location_x +
                           4*padding_x, self.location_y + padding_y)
            self.draw_text(str(self.g), self.location_x + padding_x,
                           self.location_y + BLOCK_SIZE - padding_y)
            self.draw_text(str(self.h), self.location_x + BLOCK_SIZE - padding_x,
                           self.location_y + BLOCK_SIZE - padding_y)

        self.draw_direction()


    def set_start(self):
           self.fill_color = YELLOW
           self.border_color = YELLOW


    def set_obstacle(self):
        if self.fill_color == WHITE:
            self.fill_color = BLUE
            return True
        else:
            return False

    def set_end(self):
        if self.fill_color == WHITE:
            self.fill_color = PURPLE
            self.border_color= PURPLE
            return True
        else:
            return False

    def set_open(self):
        self.type = 1
        self.fill_color = GREEN


    def set_close(self):
        self.fill_color = RED


    def set_road(self):
        self.fill_color = ORANGE

    def set_g(self, g):
        self.g = g
        self.f = self.g + self.h

    def set_h(self, h):
        self.h = h
        self.f = self.g + self.h

    def set_father(self, father, direction):
        self.father = father
        if direction != -1:
            self.father_direction = direction

