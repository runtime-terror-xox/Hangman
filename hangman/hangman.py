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
function to run the game on new window
"""
def game_window():
    category_window.destroy()
    global category

    """
    Game window
    """
    window = Tk()
    window.geometry('1023x750+450+100')
    window.configure(bg="#fff")
    window.title('Hangman_Game')

    photos = [PhotoImage(file='hm01.png'), PhotoImage(file='hm02.png'), PhotoImage(file='hm03.png'),PhotoImage(file='hm06.png'),PhotoImage(file='hm07.png'), PhotoImage(file='hm08.png')]


    """
    function to get random name by the category that user choice
    """
    def random_word():
        global category
        min, max = 0, 9
        l_idx = random.randint(min, max)
        if category == 'country':
            word_list = faker_country_data()
            random_word = word_list[l_idx]
            return random_word.lower()
        elif category == 'name':
            word_list = faker_farst_name_data()
            random_word = word_list[l_idx]
            return random_word.lower()
        elif category == 'color':
            word_list = faker_country_data()
            random_word = word_list[l_idx]
            return random_word.lower()

    """
    function to start the game and count number Of try to Guess
    """
    def if_user_want_to_play():
        global the_word_withSpaces
        global numberOfGuesses
        global word_for_guess
        numberOfGuesses = 0
        # want_play = input('you want to play')
        # want_play = 'y'
        if True:
            word_for_guess=random_word()
            the_word_withSpaces = " ".join(word_for_guess)
            print(the_word_withSpaces)
            label_word.set(" ".join("_" * len(word_for_guess)))



    """
    function to get the user hint or defintion about the word that must be guessed
    """
    def get_help(val):
        try:
            dictionary = PyDictionary(f'{val}').getMeanings()[f'{val}']['Noun'][0]
            messagebox.showwarning('Hint', dictionary)
        except:
            messagebox.showwarning('Hint', 'this one is so easy we will not help you')

    # print(get_help('black'))

    """
    function to check the letter from the user and count the times of try to guess and do some action based on his input
    """
    def if_guess(letter):
        global numberOfGuesses
        if numberOfGuesses < 6:
            text = list(the_word_withSpaces)
            guessed = list(label_word.get())
            if the_word_withSpaces.count(letter) > 0:
                for i in range(len(text)):
                    if text[i] == letter:
                        guessed[i] = letter
                    label_word.set(''.join(guessed))
                    if label_word.get() == the_word_withSpaces:
                        messagebox.showinfo('Hangman', 'Great you guessed it')
                        if_user_want_to_play()
            else:
                numberOfGuesses += 1
                img_label.config(image=photos[numberOfGuesses])
                img_label.config(bg="#fff")
                if numberOfGuesses == 5:
                    messagebox.showwarning('Hangman', 'Game Over')
                    exit()


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