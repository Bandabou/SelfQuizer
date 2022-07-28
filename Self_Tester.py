import tkinter as tk

from numpy import kaiser
from random import random


## -------------------------------------------------------------------------------
#Gui PART
window = tk.Tk()

title = tk.Label(text="Quiz 0HM150")
title.pack()

#window.mainloop()

start_button = tk.Button(
    text="Start with the question & answers",
    width  = 30,
    height = 20,
    bg = "black",
    fg = "white"  
    )

start_button.pack()

stop_button = tk.Button(
    text="Finish questions",
    width = 30,
    height = 20,
    bg = "black",
    fg = "white" 
    )
stop_button.pack()


## ----------------------------------------------------------------------------




questions = []
answers   = []

#creating a list for the questions, or answers as keys
complete_quest = {}
complete_answ  = {}

def start ():
    start = False
    return start

def quest ():
    question = input("insert your question here:")
    
    questions.append(question)

    print(questions)
    return(questions)


    
def answ ():
    
    answer = input("place your answer here:")
    answers.append(answer)
    print(answers)
    return(answers)



def merger_quest ():
    for i in range(len(questions)):        
        complete_quest[questions[i]] = answers[i] 
        print(complete_quest)
    return complete_quest

def merger_answ ():
    for i in range(len(questions)):        
        complete_answ[answers[i]] = questions[i] 
        print(complete_answ)


def randomizer():
    # q = complete.keys()
    # a = complete.values()
    print(complete_quest[questions[1]])
    print(complete_answ[answers[1]])

    #print(list(a))
    
    
def main():
    start = True            
    while start == True:
        quest()
        answ()
        checker = input("Do you want to add another test question?")
        print(checker)
        if checker in("No", "no") :
            start = False
            print(start)
        print(start)
    

#merger(questions, answers)
main()
merger_quest()
merger_answ()

#randomizer()
#find a fix for the append, need to add te

