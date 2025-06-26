import pygame
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 400, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minimalist Toxic Green Pong")

# Colors
BG_COLOR = (10, 10, 10)
TOXIC_GREEN = (57, 255, 20)

# Game objects
PADDLE_W, PADDLE_H = 7, 50
BALL_SIZE = 7
PADDLE_SPEED = 3
BALL_SPEED_X, BALL_SPEED_Y = 2, 2

# Positions
left_paddle = pygame.Rect(10, HEIGHT // 2 - PADDLE_H // 2, PADDLE_W, PADDLE_H)
right_paddle = pygame.Rect(WIDTH - 10 - PADDLE_W, HEIGHT // 2 - PADDLE_H // 2, PADDLE_W, PADDLE_H)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

clock = pygame.time.Clock()

def draw():
    WIN.fill(BG_COLOR)
    pygame.draw.rect(WIN, TOXIC_GREEN, left_paddle)
    pygame.draw.rect(WIN, TOXIC_GREEN, right_paddle)
    pygame.draw.ellipse(WIN, TOXIC_GREEN, ball)
    pygame.display.flip()

def move_ball():
    global BALL_SPEED_X, BALL_SPEED_Y
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y *= -1
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        BALL_SPEED_X *= -1

    if ball.left <= 0 or ball.right >= WIDTH:
        ball.center = (WIDTH // 2, HEIGHT // 2)

def handle_input():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        handle_input()
        move_ball()
        draw()
        clock.tick(120)

if __name__ == "__main__":
    main()
