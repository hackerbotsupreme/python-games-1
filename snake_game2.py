#from tkinter(library) import *
# is from tkinter import * means import the full tkinter module 
# Yes, from tkinter import * imports the entire tkinter module, including all 
# of its classes, functions, and variables, into the current namespace. This is called a
# wildcard import and can be a convenient way to quickly access all the functionality of a
# module. However, it is generally not recommended to use wildcard imports because they can
# lead to naming conflicts and make it harder to understand where functions and variables 
# are coming from. It is better to use explicit imports, such as import tkinter or from tkinter
# import Button, Label, to only import the specific parts of a module that you need.
# most common uses of tkinter module ? 
# The tkinter module is a popular Python GUI (Graphical User Interface) toolkit that allows developers to create desktop applications with graphical interfaces. Some of the most common uses of tkinter include:

# Creating simple GUI applications: tkinter provides various GUI widgets such as buttons, labels, entry fields, etc. that can be used to create simple graphical user interfaces for applications.

# Developing complex GUI applications: tkinter can also be used to create complex GUI applications that require more advanced features such as dialog boxes, menus, toolbars, etc.

# Data visualization: tkinter can be used to create graphical representations of data using tools such as graphs, charts, and histograms.

# Game development: tkinter can be used to create simple games that require graphical user interfaces, such as puzzles, card games, and other casual games.

# Educational tools: tkinter can be used to create educational tools such as interactive quizzes and tutorials that can be used to teach various subjects.

# Prototyping: tkinter can be used to quickly prototype graphical user interfaces for applications, allowing developers to test the user interface design before committing to a particular implementation.

# Overall, tkinter is a powerful toolkit that can be used to develop a wide range of desktop applications with graphical user interfaces.
import tkinter as tk
import random

WIDTH = 500
HEIGHT = 500
DOT_SIZE = 10
DELAY = 100

snake = [(0, 0), (0, DOT_SIZE), (0, 2 * DOT_SIZE)]
direction = "Down"
score = 0
food_pos = None

def create_food():
    global food_pos
    food_pos = (DOT_SIZE * random.randint(0, (WIDTH - DOT_SIZE) // DOT_SIZE),
                DOT_SIZE * random.randint(0, (HEIGHT - DOT_SIZE) // DOT_SIZE))
    canvas.create_oval(*food_pos, food_pos[0] + DOT_SIZE, food_pos[1] + DOT_SIZE, fill="red", tags="food")

def update_snake():
    global direction, snake, score
    x, y = snake[-1]
    if direction == "Down":
        snake.append((x, y + DOT_SIZE))
    elif direction == "Up":
        snake.append((x, y - DOT_SIZE))
    elif direction == "Left":
        snake.append((x - DOT_SIZE, y))
    elif direction == "Right":
        snake.append((x + DOT_SIZE, y))
    if snake[-1] == food_pos:
        score += 1
        create_food()
    else:
        snake.pop(0)
    canvas.delete("snake")
    canvas.create_line(*[pos for segment in snake for pos in segment], width=DOT_SIZE, tags="snake")
    canvas.itemconfig(score_text, text=f"Score: {score}")

def game_loop():
    update_snake()
    head_x, head_y = snake[-1]
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or snake[-1] in snake[:-1]:
        canvas.itemconfig(game_over_text, state="normal")
        return
    canvas.after(DELAY, game_loop)

def on_key_press(event):
    global direction
    if event.keysym == "Up":
        direction = "Up"
    elif event.keysym == "Down":
        direction = "Down"
    elif event.keysym == "Left":
        direction = "Left"
    elif event.keysym == "Right":
        direction = "Right"

# create window and canvas
root = tk.Tk()
root.title("Snake Game")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# create score text and game over text
score_text = canvas.create_text(10, 10, anchor="nw", text="Score: 0")
game_over_text = canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over!", state="hidden", font=("Arial", 20))

# bind arrow keys to move snake
root.bind("<Up>", on_key_press)
root.bind("<Down>", on_key_press)
root.bind("<Left>", on_key_press)
root.bind("<Right>", on_key_press)

# create initial snake and food
create_food()
canvas.create_line(*[pos for segment in snake for pos in segment], width=DOT_SIZE, tags="snake")

# start game loop
game_loop()

root.mainloop()


