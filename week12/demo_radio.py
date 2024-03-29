from tkinter import *
from tkinter import messagebox as msg
questions = [["What is the capital of France?", "Paris", "London", "Berlin", "Madrid", 1],
             ['Who is the current president of the United States?', 'Donald Trump', 'Barack Obama', 'Joe Biden', 'Bill Clinton', 3],
             ['Which country is the largest in the world?', 'Russia', 'Canada', 'China', 'United States', 3],
             ['When did World War II end?', '1945', '1939', '1941', '1943', 4]]

curr_question = 0

def load_question(question_index):
    lbl_quiz['text'] = questions[question_index][0]
    rd_option1['text'] = questions[question_index][1]
    rd_option2['text'] = questions[question_index][2]
    rd_option3['text'] = questions[question_index][3]
    rd_option4['text'] = questions[question_index][4]

#### EVENT HANDLERS ####
def btn_answer_clicked():
    global curr_question
    if curr_question >= len(questions):
        msg.showinfo("Quiz", "No more questions!")
        return
    
    correct_answer = questions[curr_question][5]
    if correct_answer == answer_choice.get():
        msg.showinfo("Quiz", "Correct answer!")
    else:
        msg.showerror("Quiz", "Wrong answer!")
    
    curr_question += 1
    load_question(curr_question)

#### CREATE WINDOW & WIDGETS ####
window = Tk()
window.title("Radio Demo")
window.geometry("400x200")

lbl_quiz = Label(window, text="What is the capital of France?")
lbl_quiz.grid(row=0, column=0, columnspan=2)

answer_choice = IntVar()

rd_option1 = Radiobutton(window, text="Paris", value=1, variable=answer_choice)
rd_option1.grid(row=1, column=1, sticky=W)

rd_option2 = Radiobutton(window, text="London", value=2, variable=answer_choice)
rd_option2.grid(row=2, column=1, sticky=W)

rd_option3 = Radiobutton(window, text="Berlin", value=3, variable=answer_choice)
rd_option3.grid(row=3, column=1, sticky=W)

rd_option4 = Radiobutton(window, text="Madrid", value=4, variable=answer_choice)
rd_option4.grid(row=4, column=1, sticky=W)

btn_answer = Button(window, text="Answer", command=btn_answer_clicked)
btn_answer.grid(row=5, column=0, sticky=W)

#### MAIN LOOP ####
window.mainloop()
