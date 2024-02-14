# import tkinter as tk
# import random


# class Tile:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# class SnakeGame(tk.Canvas):
#     def __init__(self, master, width, height):
#         super().__init__(master, width=width, height=height, bg="black")
#         self.width = width
#         self.height = height
#         self.tileSize = 20

#         # Snake
#         self.snakeHead = Tile(5, 5)
#         self.snakeBody = []

#         # Food
#         self.food = Tile(5, 5)

#         self.speedx = 0
#         self.speedy = 0

#         self.gameOver = False

#         self.bind("<Key>", self.key_pressed)

#         self.random = random
#         self.place_food()

#         self.gameLoop()

#     def draw(self):
#         self.delete("all")

#         # Food
#         self.create_rectangle(self.food.x * self.tileSize, self.food.y * self.tileSize,
#                               (self.food.x + 1) * self.tileSize, (self.food.y + 1) * self.tileSize, fill="red")

#         # Snake head
#         self.create_rectangle(self.snakeHead.x * self.tileSize, self.snakeHead.y * self.tileSize,
#                               (self.snakeHead.x + 1) * self.tileSize, (self.snakeHead.y + 1) * self.tileSize, fill="green")

#         # Snake body
#         for bodyPart in self.snakeBody:
#             self.create_rectangle(bodyPart.x * self.tileSize, bodyPart.y * self.tileSize,
#                                   (bodyPart.x + 1) * self.tileSize, (bodyPart.y + 1) * self.tileSize, fill="green")

#         # Score
#         score = len(self.snakeBody)
#         if self.gameOver:
#             self.create_text(self.tileSize - 16, self.tileSize,
#                              text="Game Over: " + str(score), fill="red")
#         else:
#             self.create_text(self.tileSize - 16, self.tileSize,
#                              text="Score: " + str(score), fill="white")

#     def place_food(self):
#         self.food.x = self.random.randint(0, self.width // self.tileSize - 1)
#         self.food.y = self.random.randint(0, self.height // self.tileSize - 1)

#     def collision(self, tile1, tile2):
#         return tile1.x == tile2.x and tile1.y == tile2.y

#     def move(self):
#         # Eat food
#         if self.collision(self.snakeHead, self.food):
#             self.snakeBody.append(Tile(self.food.x, self.food.y))
#             self.place_food()

#         # Snake body
#         for i in range(len(self.snakeBody) - 1, 0, -1):
#             self.snakeBody[i].x = self.snakeBody[i - 1].x
#             self.snakeBody[i].y = self.snakeBody[i - 1].y

#         if len(self.snakeBody) > 0:
#             self.snakeBody[0].x = self.snakeHead.x
#             self.snakeBody[0].y = self.snakeHead.y

#         # Snake head
#         self.snakeHead.x += self.speedx
#         self.snakeHead.y += self.speedy

#         # Game over
#         if (self.snakeHead.x < 0 or self.snakeHead.x >= self.width // self.tileSize or
#                 self.snakeHead.y < 0 or self.snakeHead.y >= self.height // self.tileSize):
#             self.gameOver = True
#         for snakePart in self.snakeBody:
#             if self.collision(self.snakeHead, snakePart):
#                 self.gameOver = True

#     def gameLoop(self):
#         if not self.gameOver:
#             self.move()
#             self.draw()
#             self.after(100, self.gameLoop)

#     def key_pressed(self, event):
#         if event.keysym == "Up" and self.speedy != 1:
#             self.speedx = 0
#             self.speedy = -1
#         elif event.keysym == "Down" and self.speedy != -1:
#             self.speedx = 0
#             self.speedy = 1
#         elif event.keysym == "Left" and self.speedx != 1:
#             self.speedx = -1
#             self.speedy = 0
#         elif event.keysym == "Right" and self.speedx != -1:
#             self.speedx = 1
#             self.speedy = 0


# root = tk.Tk()
# root.title("Snake")
# game = SnakeGame(root, 500, 500)
# game.pack()
# root.mainloop()

import pygame
import random

# Global constants and variables
WIDTH = 500
HEIGHT = 500
BLOCK_SIZE = 20
FPS = 10

# Color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)


class Snake:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.dx = BLOCK_SIZE
        self.dy = 0
        self.body = [(self.x, self.y)]

    def draw(self, screen):
        for part in self.body:
            pygame.draw.rect(
                screen, GREEN, (part[0], part[1], BLOCK_SIZE, BLOCK_SIZE))

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.body.insert(0, (self.x, self.y))  # Insert new head position
        self.body.pop()  # Remove tail position

    def grow(self):
        # Append tail position to the body to simulate growth
        self.body.append(self.body[-1])

    def check_collision(self):
        # Check if the head position is in the body or out of bounds
        return self.body[0] in self.body[1:] or \
            self.x < 0 or self.x >= WIDTH or \
            self.y < 0 or self.y >= HEIGHT


class Food:
    def __init__(self):
        self.x = random.randint(
            0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.y = random.randint(
            0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

    def place_new_food(self, snake):
        # Generate new food at a valid location
        while True:
            self.x = random.randint(
                0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            self.y = random.randint(
                0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            if (self.x, self.y) not in snake.body:
                break


def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and snake.dy != BLOCK_SIZE:
                snake.dx, snake.dy = 0, -BLOCK_SIZE
            if keys[pygame.K_DOWN] and snake.dy != -BLOCK_SIZE:
                snake.dx, snake.dy = 0, BLOCK_SIZE
            if keys[pygame.K_LEFT] and snake.dx != BLOCK_SIZE:
                snake.dx, snake.dy = -BLOCK_SIZE, 0
            if keys[pygame.K_RIGHT] and snake.dx != -BLOCK_SIZE:
                snake.dx, snake.dy = BLOCK_SIZE, 0

        snake.move()

        # Check for collision with food:
        if snake.x == food.x and snake.y == food.y:
            score += 1
            food.place_new_food(snake)  # Generate new food at a valid location
            snake.grow()  # Grow the snake

        if snake.check_collision():
            running = False

        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


game_loop()
