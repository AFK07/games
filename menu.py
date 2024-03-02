import tkinter as tk
def button_click(button_number):
    print(f"Button {button_number} clicked!")
    # button_number as an arguement and prints a message indicating which button was clicked
    # not necessarily required
    if button_number == 1:
        difficulty_page()

def difficulty_page():
    for widget in root.winfo_children():
        widget.destroy()
    game_label = tk.Label(root, text="Diffuculty", font=("Orbitron", 24), bg="black", fg="white")
    game_label.pack(pady=80)

root = tk.Tk()
root.title("Ping-Pong")
root.geometry("800x600")    # and its x not *
root.resizable(False, False)
root.configure(bg="black") # bg for background colour


title_label = tk.Label(root, text="Ping-Pong", font=("Orbitron", 24), bg="black", fg="white")
title_label.grid(row=0, column=0, pady=80)
# grid helps you to organise widgets in a table like structure

button_style = {"width":15, "height": 3, "bg": "black", "fg": "white"}

start = tk.Button(root, text="Start", command=lambda: button_click(1), **button_style)
option = tk.Button(root, text="Option", command=lambda: button_click(2), **button_style)
leaderboard = tk.Button(root, text="Leaderboard", command=lambda: button_click(3), **button_style)
exit = tk.Button(root, text="Exit", command=lambda: button_click(4), **button_style)

# the lambda func is used to pass arguements to the button_click function

start.grid(row=1, column=0, pady=10)
option.grid(row=2, column=0, pady=10)
leaderboard.grid(row=3, column=0, pady=10)
exit.grid(row=4, column=0, pady=10)


root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop() # lol dont forget the parentheses