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