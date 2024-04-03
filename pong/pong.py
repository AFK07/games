import tkinter as tk
import random

class PongGame:
    def __init__(self, master):
        self.master = master                    # stores the reference to the main window(tk instance)
        self.master.title("Pong Game")          # name on the title bar
        self.master.geometry("800x600")         # dimension of the window
        self.master.resizable(False, False)     # prevents change of horizontal and vertical change of the window dimensions

        self.paused = False  # the game starts without the pause function so it is set as false from the start

        # Create the canvas for drawing game elements
        self.canvas = tk.Canvas(self.master, bg="black", width=800, height=600)
        self.canvas.pack()                      # makes the canvas visible within the main window

        # Create paddles and ball on the canvas
        self.paddle_a = self.canvas.create_rectangle(50, 250, 70, 350, fill="white")
        self.paddle_b = self.canvas.create_rectangle(730, 250, 750, 350, fill="white")
        self.ball = self.canvas.create_oval(395, 295, 405, 305, fill="white")

        # Initialize ball speed
        self.ball_speed_x = random.choice([-3, 3])
        self.ball_speed_y = random.choice([-3, 3])
        # the negative value when the ball moves left or upwards(the x coordinates)
        # the positive value when the ball goes right or downwards(y coordinates
        
        # 
        # Initialize scores
        self.score_a = 0
        self.score_b = 0

        # Create score display text on the canvas
        self.score_display = self.canvas.create_text(400, 30, text="Player A: 0  Player B: 0", fill="white", font=("Courier", 14))

        # Create the "Paused" label on the canvas, initially hidden
        self.pause_label = self.canvas.create_text(400, 300, text="Paused", fill="white", font=("Courier", 24))
        # the 400, 30 are the coordinates for the text placement 
        # player names and initial scores
        # the rest are colour, font and size


        self.canvas.itemconfig(self.pause_label, state="hidden") # its responsibility is to hide and display the pause label when triggered

        # Bind keyboard events
        self.master.bind("<Up>", self.paddle_b_up)
        self.master.bind("<Down>", self.paddle_b_down)
        self.master.bind("<w>", self.paddle_a_up)
        self.master.bind("<s>", self.paddle_a_down)
        self.master.bind("<Escape>", self.toggle_pause)  # Bind the Escape key to toggle pause

        # Start the game loop
        self.master.after(10, self.update_game)
        # ensures the game continuously responds to the user input, moves the ball, checks for collisions and updates the display
        # creating the illusion of continuous and dynamic gameplay.

    # Functions to move paddles
    def paddle_a_up(self, event):
        self.canvas.move(self.paddle_a, 0, -20)

    def paddle_a_down(self, event):
        self.canvas.move(self.paddle_a, 0, 20)

    def paddle_b_up(self, event):
        self.canvas.move(self.paddle_b, 0, -20)

    def paddle_b_down(self, event):
        self.canvas.move(self.paddle_b, 0, 20)
    # paddle movements

    # Function to toggle pause
    def toggle_pause(self, event):
        if self.paused:
            self.paused = False
            self.canvas.itemconfig(self.pause_label, state="hidden")  # Hide "Paused" label
        else:
            self.paused = True
            self.canvas.itemconfig(self.pause_label, state="normal")  # Show "Paused" label
    # state of the pause function

    # Function to update game state
    def update_game(self):
        if not self.paused:         # the game is not paused, hence the ball is in motion
            # Move the ball
            self.canvas.move(self.ball, self.ball_speed_x, self.ball_speed_y)

            # Ball collision with top and bottom walls
            if self.canvas.coords(self.ball)[1] <= 0 or self.canvas.coords(self.ball)[3] >= 600:
            # [1] represents y coordinates of the top edge of the ball
            # [3] represents y coordinates of the bottom edge of the ball
            # or we can write  
            
                self.ball_speed_y *= -1     # this is the vertical bounce. the negative represents when the ball bounces off.
                # the self ball speed represents the horizontal speed of the ball which controls te motion of the ball.

            # Ball collision with paddles
            if self.ball_speed_x < 0:       
            # checks whether the ball is moving to the left or it means the ball is approaching paddle_a
                if self.canvas.coords(self.ball)[0] <= self.canvas.coords(self.paddle_a)[2] and \
                        self.canvas.coords(self.paddle_a)[1] <= self.canvas.coords(self.ball)[1] <= self.canvas.coords(self.paddle_a)[3]:
                    self.ball_speed_x *= -1
            else:           # it is moving to paddle_b
                if self.canvas.coords(self.ball)[2] >= self.canvas.coords(self.paddle_b)[0] and \
                        self.canvas.coords(self.paddle_b)[1] <= self.canvas.coords(self.ball)[1] <= self.canvas.coords(self.paddle_b)[3]:
                    self.ball_speed_x *= -1

            # the scoring bit
            if self.canvas.coords(self.ball)[0] <= 0:
                self.score_b += 1
                self.reset_ball()

            elif self.canvas.coords(self.ball)[2] >= 800:
                self.score_a += 1
                self.reset_ball()

            # Updates the score
            self.canvas.itemconfig(self.score_display, text=f"Player A: {self.score_a}  Player B: {self.score_b}")

        
        self.master.after(10, self.update_game)

    # puts the ball back to its starting position
    def reset_ball(self):
        self.canvas.coords(self.ball, 395, 295, 405, 305)
        self.ball_speed_x = random.choice([-2, 2])
        self.ball_speed_y = random.choice([-2, 2])

# runs the program
if __name__ == "__main__":
    root = tk.Tk()
    game = PongGame(root)
    root.mainloop()
