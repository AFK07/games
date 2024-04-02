import tkinter
import random  

ROWS = 25
COLS = 25
TILE_SIZE = 10

WINDOW_WIDTH = TILE_SIZE * COLS #25*25 = 625
WINDOW_HEIGHT = TILE_SIZE * ROWS 
# constructs a 625 x 625 pixel screen environment

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#game window
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tkinter.Canvas(window, 
                        bg = "black", 
                        width = WINDOW_WIDTH, 
                        height = WINDOW_HEIGHT, 
                        borderwidth = 0, # if you remove this, it will create a white border
                        highlightthickness = 0)
canvas.pack()
window.update()

#center the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# the math to cenrte the window to the centre of the screen

#initialize game
snake = Tile(TILE_SIZE * 5, 
             TILE_SIZE * 5) #single tile, snake's head
food = Tile(TILE_SIZE * 10, 
            TILE_SIZE * 10) # same concept for food
velocityX = 0
velocityY = 0   # both for speed in the change_direction
snake_body = [] #multiple snake tiles
game_over = False
score = 0
# all the default values

#game loop
def change_direction(e): #e = event
    # print(e)
    # print(e.keysym)

    global velocityX, velocityY, game_over
    if (game_over):
        return #edit this code to reset game variables to play again

    if (e.keysym == "Up" and velocityY != 1):
        velocityX = 0
        velocityY = -1
        
    elif (e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1

    elif (e.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0

    elif (e.keysym == "Right" and velocityX != -1):
        velocityX = 1
        velocityY = 0
        
    # The != conditions exist to prevent the snake to move backwards from the direction it faces. 


def move():
    global snake, food, snake_body, game_over, score
    if (game_over):
        return
    
    if (snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT):
        game_over = True
        return
    # game over if the snake collides against the borders
    
    for tile in snake_body:
        if (snake.x == tile.x and snake.y == tile.y):
            game_over = True
            return
    # tiles represent its body where the snake is the head, therefore this is the condition for when the snake collides with its body
    
    #collision
    if (snake.x == food.x and snake.y == food.y): 
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS-1) * TILE_SIZE
        food.y = random.randint(0, ROWS-1) * TILE_SIZE
        score += 1
    # random.randint ensures the food is auto generated to any part of the space. 

    #update snake body
    for i in range(len(snake_body)-1, -1, -1):
        tile = snake_body[i]
        if (i == 0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y
    
    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE


def draw():
    global snake, food, snake_body, game_over, score
    move()

    canvas.delete("all")

    #draw food
    canvas.create_rectangle(food.x, 
                            food.y, 
                            food.x + TILE_SIZE, 
                            food.y + TILE_SIZE, 
                            fill = 'red')

    #draw snake
    canvas.create_rectangle(snake.x, 
                            snake.y, 
                            snake.x + TILE_SIZE, 
                            snake.y + TILE_SIZE, 
                            fill = 'lime green')

    for tile in snake_body:
        canvas.create_rectangle(tile.x, 
                                tile.y, 
                                tile.x + TILE_SIZE, 
                                tile.y + TILE_SIZE, 
                                fill = 'lime green')

    if (game_over):
        canvas.create_text(WINDOW_WIDTH/2, 
                           WINDOW_HEIGHT/2, 
                           font = "Arial 20", 
                           text = f"Game Over: {score}", 
                           fill = "white")
    else:
        canvas.create_text(30, 20, 
                           font = "Arial 10", 
                           text = f"Score: {score}", 
                           fill = "white")
    # updates the score on the top of the created window or else the centre if game is over.
    
    window.after(100, draw) 
    #call draw again every 100ms (1/10 of a second) = 10 frames per second

draw()
window.bind("<KeyRelease>", change_direction) 
#when you press on any key and then let go
window.mainloop() 
#used for listening to window events like key presses
