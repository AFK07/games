from tkinter import *
import random

def next_turn(row, column):
    global player                   # to have access to it
    if buttons [row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:
            buttons[row][column]['text'] = player

            if check_winner() is False:             # switches player if the winning condition does not match
                player = players[1]                 
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+ " wins"))

            elif check_winner() == "Tie":
                label.config(text=(players[0]+ " Tie"))
        else:
            buttons[row][column]['text'] = player

            if check_winner() is False:             # switches player if the winning condition does not match
                player = players[0]                 
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+ " wins"))

            elif check_winner() == "Tie":
                label.config(text=(players[1]+ " Tie"))


def check_winner():
    for row in range(3): #horizontal win condition
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
        
    for column in range(3): #vertical win condition
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    
    # diagonal win condition
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    
    #checks remaining empty spaces
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    # the colour changes if the button choices matches the winning condition.
    # if win, its green. if a tie then yellow
    # remember, the format is buttons[row][column]
    # no winner

    else:
        return False

def empty_spaces():
    spaces = 9 

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    
    if spaces == 0:         # 
        return False
    
    else:
        return True
    

def new_game():
    global player
    player = random.choice(players)
    label.config(text = player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

# Initialize Tkinter window
window = Tk()
window.title("Tic-Tac-Toe")


# Calculate the width and height of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the width and height of the window
window_width = 465  
window_height = 638  

# Calculate the x and y coordinates for the window to be centered
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window's geometry
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Initialize game variables
players = ["x", "o"]                # symbols used by players
player = random.choice(players)     # randomly selects the player at the start of the game
buttons = [[0,0,0], 
           [0,0,0], 
           [0,0,0]]                 # creates a 2 dimensional grid layer. The 0's will be replaced by the player symbol

label = Label(text=player + " turn", font=('consolas', 40))     # The very top label which represents the player symbol in each turns
label.pack(side="top")              # the side parameter specifies where exactly the label should be written

reset_button = Button(text= "restart", font = ('consolas', 20), command = new_game)         # 
reset_button.pack(side="top")

frame = Frame(window)           # Frames are used to organise and group other widgets together.
frame.pack()


#nested for loops
for row in range(3):
    for column in range(3):
        buttons[row][column]= Button(frame, text = "", 
                                     font=('consolas', 40), 
                                     width=5, 
                                     height = 2, 
                                     command=lambda row=row,        #specifies the function that should be called when a button is clicked.
                                     column = column: next_turn(row, column))   # uses the lambda function to pass the current row and column indices to the next_turn function.
        buttons[row][column].grid(row=row, column=column)
        # arguements and functions
# Start the Tkinter event loop
window.mainloop()


# # to put it in the centre of the window

# screen_width = window.winfo_screenmmwidth()
# screen_height = window.winfo_screenheight()

# window_width = 470
# window_height = 625
# x = (screen_width - window_width) // 2
# y = (screen_height - window_height) //2

# window.geometry(f"{window_width}x{window_height}+{x}+{y}")
# window.resizable(False, False)
# need to work on this

# gui alterations are possible
