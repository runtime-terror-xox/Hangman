from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PyDictionary import PyDictionary
# import time
import random
from data_from_faker import *


alphabet1=[ 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','a']
alphabet2=[ 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','z']
alphabet3=[ 'x', 'c', 'v', 'b', 'n', 'm']


"""
Category window
"""
category_window = Tk()
category_window.geometry('400x200+761+250')
category_window.configure(bg="#fff")
category_window.title('Hangman')

"""
function to check what is the category and call a new function to open new window (game window) and destroy category window
"""
def what_is_category():
     print(box_value.get())
     if box_value.get():
        global category
        category=box_value.get()
        game_window()


box_value=StringVar()
coltbox = ttk.Combobox(category_window,textvariable=box_value)
coltbox["values"] = ["color", "name","country"]
coltbox.pack()
start_game=Button(category_window,text="start\ngame", command=what_is_category, width=20)
start_game.pack()


"""
function to show the windows it is for tkinter package
"""
def run_tkinter():
    category_window.mainloop()
run_tkinter()