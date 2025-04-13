import pygame
import time
import random
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

# Initialize pygame
pygame.init()

# Window size
width = 800
height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Game window
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Super long term - short distance - mid commitment - casual situationship Snake 🐍')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("louize display", 25)
score_font = pygame.font.SysFont("helvetica rounded", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0, 0])

def show_popup_gif():
    root = tk.Tk()
    root.title("🥰 Situationship Confirmed")
    root.geometry("500x400")

    msg = tk.Label(root, text="Congrats for the first year 💖\nDoes it mean you're my official situationship now? 😏", font=("Helvetica", 12), wraplength=400, justify="center")
    msg.pack(pady=10)

    canvas = tk.Canvas(root, width=480, height=300)
    canvas.pack()

    gif = Image.open("bromance.gif")
    frames = [ImageTk.PhotoImage(frame.copy().resize((480, 300))) for frame in ImageSequence.Iterator(gif)]

    def animate(index=0):
        canvas.create_image(0, 0, anchor=tk.NW, image=frames[index])
        root.after(100, animate, (index + 1) % len(frames))

    animate()
    root.mainloop()

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(white)
            message("You lost! Press C-Play Again or Q-Quit", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            show_popup_gif()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
