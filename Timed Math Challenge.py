import tkinter as tk
from BasicMathsQuestionMaker import question_maker
import pandas as pd

root = tk.Tk()
root.geometry("700x400")
root.title("Math Game")

pause_game = False
score = 0
total_seconds = 30
timer = total_seconds

def update_timer():
    global timer, pause_game, total_seconds
    if not pause_game and timer > 0:
        timer -= 1
        label1.config(text=f"Time : {timer}")
        root.after(1000, update_timer)
        
def check1() :
    global question_list, score
    if question_list[2] == question_list[1][0] :
        score += 1
    new_question()
def check2() :
    global question_list, score
    if question_list[2] == question_list[1][1] :
        score += 1
    new_question()
def check3() :
    global question_list, score
    if question_list[2] == question_list[1][2] :
        score += 1
    new_question()
        
def new_question() :
    global question_list
    question_list = question_maker()
    question_label.config(text=question_list[0])
    option1.config(text=question_list[1][0])
    option2.config(text=question_list[1][1])
    option3.config(text=question_list[1][2])

def finish() :
    global score
    option1.config(state="disabled")
    option2.config(state="disabled")
    option3.config(state="disabled")
    open_input_window()
    
def open_input_window():
    def savescore(name, s) : 
        df = pd.read_csv("scores.csv")
        newdf = pd.DataFrame({"username":[name], "score":[s]})
        df = pd.concat([df, newdf], ignore_index=True)
        df.to_csv("scores.csv", index=False)
    win = tk.Toplevel(root)
    win.geometry("400x100")
    win.title("Time's Up")
    win.resizable(False, False)

    def submit():
        username = entry1.get()
        savescore(username, score)
        win.destroy()
        scoreboard(username, score)

    label3 = tk.Label(win, text="Username :", font="Arial 13")
    entry1 = tk.Entry(win, font="Arial 13 bold", width=20)
    button1 = tk.Button(win, text="Submit", font="Arial 13 bold", bg="lightblue", command=submit)

    label3.place(x=10, y=10)
    entry1.place(x=110, y=10)
    button1.place(x=10, y=50)

def scoreboard(name, score) :
    root2 = tk.Toplevel(root)
    root2.title("Top Scores")
    root2.geometry("400x500")

    title1 = tk.Label(root2, text="Username", font="arial 15 bold underline")
    title2 = tk.Label(root2, text="Score", font="arial 15 bold underline")
    title3 = tk.Label(root2, text="Position", font="arial 15 bold underline")
    title1.place(x=150, y=10)
    title2.place(x=300, y=10)
    title3.place(x=10, y=10)
    
    df = pd.read_csv("scores.csv")
    df = df.sort_values(by=["score"], ascending=False)
    df = df.reset_index(drop=True)
    position = df.query(f"username=='{name}' & score=={score}")
    ydiff = 30
    try :
        for i in range(10) :
            score_list = list(df.values)[i]
            pos = tk.Label(root2, text=i+1, font="arial 14", justify="center")
            user = tk.Label(root2, text=score_list[0], font="arial 14", justify="center")
            score_label = tk.Label(root2, text=score_list[1], font="arial 14", justify="center")
            pos.place(x=30, y=50+(ydiff*i))
            user.place(x=160, y=50+(ydiff*i))
            score_label.place(x=310, y=50+(ydiff*i))
    except : 
        pass

    current_pos = tk.Label(root2, text=position.index[0]+1, font="arial 14", justify="center", fg="white", bg="black")
    current_user = tk.Label(root2, text=name, font="arial 14", justify="center", fg="white", bg="black")
    current_score = tk.Label(root2, text=score, font="arial 14", justify="center", fg="white", bg="black")
    current_pos.place(x=30, y=50+ydiff+(ydiff*i))
    current_user.place(x=160, y=50+ydiff+(ydiff*i))
    current_score.place(x=310, y=50+ydiff+(ydiff*i))
    
    root2.mainloop()
    

label1 = tk.Label(root, text=f"Time : {total_seconds}", font="Verdana 16")
question_list = question_maker()
question_label = tk.Label(root, text=question_list[0], font="Garamond 40 bold")
option1 = tk.Button(root, text=question_list[1][0], font="Verdana 22", width=10, bg="lightblue", border=7, command=check1)
option2 = tk.Button(root, text=question_list[1][1], font="Verdana 22", width=10, bg="lightblue", border=7, command=check2)
option3 = tk.Button(root, text=question_list[1][2], font="Verdana 22", width=10, bg="lightblue", border=7, command=check3)

label1.place(x=290, y=10)  
question_label.place(x=280, y=70)
option1.place(x=20, y=170)
option2.place(x=250, y=170)
option3.place(x=480, y=170)
root.after(1000, update_timer)
root.after(total_seconds*1000, finish)



root.mainloop()


# Make an AI player too.