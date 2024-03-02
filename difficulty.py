import tkinter as tk

def difficulty_page(back_callback):
    difficulty_window = tk.Tk()  # Use Toplevel for additional windows
    difficulty_window.title("Ping-Pong")
    difficulty_window.geometry("800x600")
    difficulty_window.resizable(False, False)
    difficulty_window.configure(bg="black")

    # the button_style needs to be ammended for cleaner code on increase and decrease
    button_style = {"width": 15, "height": 3, "bg": "black", "fg": "white"}

    for widget in difficulty_window.winfo_children():
        widget.destroy()

    difficulty_label = tk.Label(difficulty_window, text="Difficulty", font=("Orbitron", 16), **button_style)
    difficulty_label.grid(row=1, column=1, padx=100, pady=20)  

    back_ = tk.Button(difficulty_window, text="Back",font=("Orbitron", 26), command=back_callback, bg="black", fg="white", height=1, width = 5)
    back_.grid(row=0, column=0, padx=20, pady=20)

    difficulty_label.grid_rowconfigure(0, weight=1)
    difficulty_label.grid_columnconfigure(4, weight=1)

    # each buttons on display, the functions of the buttons will soon be implemented
    decrease = tk.Button(difficulty_window, text="-", font=("Orbitron", 26), bg="black", fg="white", height=1, width = 5)
    decrease.grid(row=2, column=0, padx=5, pady=10)

    number_label = tk.Label(difficulty_window, text="Number", font=("Orbitron", 16), bg="black", fg="white")
    number_label.grid(row=2, column=1, padx=5, pady=10)

    increase = tk.Button(difficulty_window, text="+", font=("Orbitron", 26), bg="black", fg="white", height=1, width = 5)
    increase.grid(row=2, column=2, padx=5, pady=10)

    play = tk.Button(difficulty_window, text="play", font=("Orbitron", 20), bg="black", fg="white")
    play.grid(row=3, column=1, padx=20, pady=20)


    difficulty_window.mainloop()

def placeholder_callback():
    print("Back button clicked")

if __name__ == "__main__":
    difficulty_page(placeholder_callback)
