import tkinter as tk
import random

def next_turn():
    pass

def check_winner():
    pass

def empty_spaces():
    pass

def new_name():
    pass

window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o"]
player = random.choice(players)
buttons = [
    [0,0,0],
    [0,0,0],
    [0,0,0]]

label = Label(text=_player + " turn", font=('inder',40))
label.pack(side="top")

reset_button = Button(text="restart", font=('inder',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('inder',40), width=5, height=2)
        command= lambda row=row, column=column: next_turn(row)

        button[row][column].grid(row=row,column=column)


window.mainloop()