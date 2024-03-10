from tkinter import *
import random

root = Tk()
root.geometry("300x500")
root.title("TIC TAC TOE")

head = Label(root,text="TIC-TAC-TOE",fg="forestgreen",bg="light cyan",font=("Arial",20,"italic"))
head.pack()

p1_name = ""
p2_name = ""
START = False
AI = False  # Flag to indicate whether playing against AI or not
moves_history = []  # List to keep track of moves for undo

def Start():
    global p1_name, p2_name, START, AI
    P1 = p1.get()
    P2 = p2.get()

    if P1.split() == []:
        text = "Enter Player 1 Name"
        turn.place(x=50,y=455)
        turn['fg'] = "red"
        turn['text'] = text
    elif P2.split() == []:
        text = "Enter Player 2 Name"
        turn.place(x=50,y=455)
        turn['fg'] = "red"
        turn['text'] = text
    elif P1.split() == P2.split():
        text = "Enter Different Player Names"
        turn.place(x=25,y=455)
        turn['fg'] = "red"
        turn['text'] = text
    else:
        p1_name = P1
        p2_name = P2
        p1['font'] = ("Arial",8,"bold")
        p2['font'] = ("Arial",8,"bold")
        p1['state'] = DISABLED
        p2['state'] = DISABLED

        start.place(x=1000,y=1000)
        turn['text'] = "{}{} Turn".format(p1_name,"'s")
        turn['fg'] = "blue"
        turn['font'] = ("Ubuntu",20,"bold")
        turn.place(x=50,y=425)
        START = True

        if P2 == "AI":
            AI = True

def WinCheck():
    # List of winning combinations
    win_combinations = [
        [b1, b2, b3], [b4, b5, b6], [b7, b8, b9],  # Horizontal
        [b1, b4, b7], [b2, b5, b8], [b3, b6, b9],  # Vertical
        [b1, b5, b9], [b3, b5, b7]                 # Diagonal
    ]

    # Check each winning combination
    for combination in win_combinations:
        if all(button['text'] == "O" for button in combination):
            highlight_winning_buttons(combination, "O")
            return "p1"  # Player 1 wins
        elif all(button['text'] == "X" for button in combination):
            highlight_winning_buttons(combination, "X")
            return "p2"  # Player 2 wins

    # Check for tie
    if all(button['text'] != "" for button in [b1, b2, b3, b4, b5, b6, b7, b8, b9]):
        return "tie"

    return False  # No winner yet

def highlight_winning_buttons(buttons, player):
    for button in buttons:
        button['bg'] = "light green" if player == "O" else "light blue"

def DisableButtons(ButtonList):
    for a in range(len(ButtonList)):
        ButtonList[a]['state'] = DISABLED

def EnableButtons(ButtonList):
    for a in range(len(ButtonList)):
        ButtonList[a]['state'] = NORMAL

def BtnClick(button):
    global START, p1_name, p2_name, AI, moves_history
    if START:
        if button['text'] == "":
            moves_history.append(button)
            if turn['text'] == "{}{} Turn".format(p1_name, "'s"):
                button['text'] = "O"
                turn['text'] = "{}{} Turn".format(p2_name, "'s")
                if AI and not WinCheck():
                    AI_Play()  # Call AI's move only if playing against AI and it's AI's turn
            else:
                button['text'] = "X"
                turn['text'] = "{}{} Turn".format(p1_name, "'s")

        check = WinCheck()
        if check != False:
            restart.place(x=105, y=470)
            START = False
            if check == "p1":
                text = "{} Wins".format(p1_name)
            elif check == "p2":
                text = "{} Wins".format(p2_name)
            else:
                text = "It is a tie !"
            turn['fg'] = "forestgreen"
            turn['text'] = text

            if check != "tie":
                DisableButtons([button for button in [b1, b2, b3, b4, b5, b6, b7, b8, b9] if button not in moves_history])
            else:
                DisableButtons([b1, b2, b3, b4, b5, b6, b7, b8, b9])

def Undo():
    global moves_history
    if moves_history:
        button = moves_history.pop()
        button['text'] = ""
        if turn['text'] == "{}{} Turn".format(p1_name, "'s"):
            turn['text'] = "{}{} Turn".format(p2_name, "'s")
        else:
            turn['text'] = "{}{} Turn".format(p1_name, "'s")

def Restart():
    global moves_history
    moves_history = []
    Buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
    EnableButtons([p1,p2])
    EnableButtons(Buttons)
    restart.place(x=1000,y=1000)
    for a in range(len(Buttons)):
        Buttons[a]['text'] = ""
        Buttons[a]['bg'] = "SystemButtonFace"
    turn['text'] = ""
    start.place(x=107,y=410)
    p1['font'] = "TkTextFont"
    p2['font'] = "TkTextFont"

def AI_Play():
    global moves_history
    empty_buttons = [button for button in [b1, b2, b3, b4, b5, b6, b7, b8, b9] if button['text'] == ""]
    if empty_buttons:
        button_to_click = random.choice(empty_buttons)
        button_to_click.invoke()  # Simulate button click

###################################

Label(root,text="Player 1 :",fg="brown",font=("Courier",10,"bold")).place(x=0,y=50)
p1 = Entry(root)
p1.place(x=90,y=52)

Label(root,text="Player 2 (or AI):",fg="brown",font=("Courier",10,"bold")).place(x=0,y=75)
p2 = Entry(root)
p2.place(x=135,y=77)

start = Button(root,text="START",bg="gray90",fg="green",font=("Ubuntu",15,"bold"),command=Start)
start.place(x=107,y=410)

turn = Label(root,text="",font=("Ubuntu",15,"normal"))
turn.place(x=50,y=455)

###################################

b1 = Button(root,width=13,height=6,command=lambda:BtnClick(b1))
b1.place(x=0,y=100)

b2 = Button(root,width=13,height=6,command=lambda:BtnClick(b2))
b2.place(x=100,y=100)

b3 = Button(root,width=13,height=6,command=lambda:BtnClick(b3))
b3.place(x=200,y=100)

b4 = Button(root,width=13,height=6,command=lambda:BtnClick(b4))
b4.place(x=0,y=200)

b5 = Button(root,width=13,height=6,command=lambda:BtnClick(b5))
b5.place(x=100,y=200)

b6 = Button(root,width=13,height=6,command=lambda:BtnClick(b6))
b6.place(x=200,y=200)

b7 = Button(root,width=13,height=6,command=lambda:BtnClick(b7))
b7.place(x=0,y=300)

b8 = Button(root,width=13,height=6,command=lambda:BtnClick(b8))
b8.place(x=100,y=300)

b9 = Button(root,width=13,height=6,command=lambda:BtnClick(b9))
b9.place(x=200,y=300)

###################################

undo = Button(root,text="Undo",fg="blue",bg="light yellow",width=10,height=1,font=("Courier",10,"bold"),command=Undo)
undo.place(x=5,y=470)

restart = Button(root,text="Restart",fg="blue",bg="aquamarine",width=10,height=1,font=("Courier",10,"bold"),command=Restart)
restart.place(x=105,y=470)

root.mainloop()
