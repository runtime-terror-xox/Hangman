<<<<<<< HEAD
# from tkinter import *
# from tkinter import messagebox,ttk,Text,filedialog
# from string import ascii_lowercase
# from faker import Faker
# import random
# from tkinter.ttk import


# window = Tk()
# window.title('Hangman')
# fake = Faker('en_US')
# colors_to_guess = [fake.color_name()]
# photos = [PhotoImage(file='images/hang0.png'), PhotoImage(file='images/hang1.png'), PhotoImage(file='images/hang2.png'), PhotoImage(file='images/hang3.png'),
#           PhotoImage(file='images/hang4.png'), PhotoImage(file='images/hang5.png'), PhotoImage(file='images/hang6.png'),PhotoImage(file='images/hang7.png'),
#           PhotoImage(file='images/hang8.png'), PhotoImage(file='images/hang9.png'), PhotoImage(file='images/hang10.png'), PhotoImage(file='images/hang11.png')]
#
#
# def new_game():
#     window.destroy()
#     window2 = Tk()
#     window2.title('Hangman2')
#     Button(window2, text='play', command=lambda: new_game(), font=('Helvetica 10 bold'),
#            activeforeground="darkblue", bg="#3e646c", fg="white", bd=1).grid(row=3, column=8, sticky='NSWE')
#
#
# def guess(letter):
#     global numberOfGuesses
#     if numberOfGuesses < 11:
#         text = list(the_word_withSpaces)
#         guessed = list(lblWord.get())
#         if the_word_withSpaces.count(letter) > 0:
#             for i in range(len(text)):
#                 if text[i] == letter:
#                     guessed[i] = letter
#                 lblWord.set(''.join(guessed))
#                 if lblWord.get() == the_word_withSpaces:
#                     messagebox.showinfo('Hangman', 'Great you guessed it')
#                     new_game()
#         else:
#             numberOfGuesses +=1
#             img_label.config(image=photos[numberOfGuesses])
#             if numberOfGuesses == 11:
#                 messagebox.showwarning('Hangman', 'Game Over')
#
# img_label = Label(window)
# img_label.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
# img_label.config(image=photos[0])
# lblWord = StringVar()
# Label(window, textvariable=lblWord, font=('Consolas 24 bold')).grid(row=0, column=3, columnspan=6, padx=10)
# # underline=0
# n = 0
# for i in ascii_lowercase:
#     Button(window, text=i, command=lambda i=i: guess(i), font=('Helvetica 18'), width=5,height=3 ,bg="#263d42",fg="white",bd=1,activebackground="#3e646c",activeforeground="pink").grid(row=1+n//9, column=n%9)
#     n += 1
# Button(window, text='New\nGame', command=lambda: new_game(), font=('Helvetica 10 bold'),activeforeground="darkblue",bg="#3e646c",fg="white",bd=1).grid(row=3, column=8, sticky='NSWE')
# Button(window, text='Hunt', command=lambda: new_game(), font=('Helvetica 10 bold'),width=80,activeforeground="darkblue",bg="darkblue",fg="white",bd=1).grid(row=4, column=0, sticky='NSWE')

# new_game()
# window.mainloop()

# from random_word import RandomWords
# r = RandomWords()

# Return a single random word
# Return list of Random words
# Return Word of the day
# print(r.('car'))
# print(r.DictionaryDef('car'))

# from PyDictionary import PyDictionary
# def get_help(val):
#     try:
#         dictionary=PyDictionary(f'{val}').getMeanings()[f'{val}']['Noun'][0]
#         return dictionary
#     except:
#         return 'this one is so easy we will not help you'
# print(get_help('black'))


# import speech_recognition as sr
# import time
# filename = "s.wav"
# r = sr.Recognizer()
# with sr.AudioFile(filename) as source:
#     # listen for the data (load audio to memory)
#     audio_data = r.record(source)
#     # recognize (convert from speech to text)
#     text = r.recognize_google(audio_data)
#     print(text)

# import speech_recognition as sr
# r=sr.Recognizer()
# with sr.Microphone() as source:
#     print('speack any th')
#     audio=r.listen(source)
#
#     text=r.recognize_google(audio)
#     print(text)

import audiomath; audiomath.RequireAudiomathVersion( '1.12.0' )
import speech_recognition  # NB: python -m pip install SpeechRecognition
class DuckTypedMicrophone( speech_recognition.AudioSource ): # descent from AudioSource is required purely to pass an assertion in Recognizer.listen()
    def __init__( self, device=None, chunkSeconds=1024/44100.0 ):  # 1024 samples at 44100 Hz is about 23 ms
        self.recorder = None
        self.device = device
        self.chunkSeconds = chunkSeconds
    def __enter__( self ):
        self.nSamplesRead = 0
        self.recorder = audiomath.Recorder( audiomath.Sound( 5, nChannels=1 ), loop=True, device=self.device )
        # Attributes required by Recognizer.listen():
        self.CHUNK = audiomath.SecondsToSamples( self.chunkSeconds, self.recorder.fs, int )
        self.SAMPLE_RATE = int( self.recorder.fs )
        self.SAMPLE_WIDTH = self.recorder.sound.nbytes

        return self
    def __exit__( self, *blx ):
        self.recorder.Stop()
        self.recorder = None
    # x=0
    # Note stoped here
    def read( self, nSamples ):
        # DuckTypedMicrophone.x+=1
        # print(DuckTypedMicrophone.x)
        # if DuckTypedMicrophone.x>180:
        #     return
        sampleArray = self.recorder.ReadSamples( self.nSamplesRead, nSamples )
        self.nSamplesRead += nSamples
        return self.recorder.sound.dat2str( sampleArray )
    @property
    def stream( self ): # attribute must be present to pass an assertion in Recognizer.listen(), and its value must have a .read() method
        return self if self.recorder else None

if __name__ == '__main__':
    import speech_recognition as sr
    r = sr.Recognizer()
    try:
        with DuckTypedMicrophone() as source:
            print('\nSay something to the ...')
            audio = r.listen(source)
        print('Got it.\n')
        print('you say : "%s"\n' % r.recognize_google(audio))
    except:
        print('sorry saleh do it again ')
    if True: # plot and/or play back captured audio
        s = audiomath.Sound(audio.get_wav_data(), fs=audio.sample_rate, nChannels=1)






=======
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

    label_word = StringVar()

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


    img_label = Label(window)
    img_label.grid(row=1, column=3, columnspan=3, padx=10, pady=40)
    img_label.config(image=photos[0])
    img_label.config(bg="#fff")

    Label(window, textvariable=label_word, font=('Consolas 24 bold'), bg="#fff").grid(row=1, column=7, columnspan=6,
                                                                                   padx=10)

    n = 2
    Label(window, textvariable='', font=('Helvetica 18'), width=3, height=3, bg="#fff").grid(row=3 + n // 13,
                                                                                             column=n % 13)
    Label(window, textvariable='', font=('Helvetica 18'), width=3, height=3, bg="#fff").grid(row=3 + n // 13,
                                                                                             column=n % 13)
    for i in alphabet1:
        Button(window, text=i, command=lambda i=i: if_guess(i), font=('Helvetica 18'), width=5, height=3, bg="#263d42",
               fg="white", bd=1, activebackground="#3e646c", activeforeground="pink").grid(row=3 + n // 13,
                                                                                           column=n % 13)
        n += 1

    n = 3
    Label(window, textvariable='', font=('Helvetica 18'), width=3, height=3, bg="#fff").grid(row=4 + n // 12,
                                                                                             column=n % 12)
    Label(window, textvariable='', font=('Helvetica 18'), width=3, height=3, bg="#fff").grid(row=4 + n // 12,
                                                                                             column=n % 12)
    Label(window, textvariable='', font=('Helvetica 18'), width=3, height=3, bg="#fff").grid(row=4 + n // 12,
                                                                                             column=n % 12)
    Label(window, text=' ', font=('Helvetica 18'), width=5, height=3, bg="#fff", fg="white", bd=1).grid(row=2 + n // 10,
                                                                                                        column=n % 10)
    for i in alphabet2:
        Button(window, text=i, command=lambda i=i: if_guess(i), font=('Helvetica 18'), width=5, height=3, bg="#263d42",
               fg="white", bd=1, activebackground="#3e646c", activeforeground="pink").grid(row=4 + n // 12,
                                                                                           column=n % 12)
        n += 1

    n = 4
    Label(window, textvariable='', font=('Helvetica 18'), width=3, height=3, bg="#fff").grid(row=5 + n // 10,
                                                                                             column=n % 10)
    Label(window, textvariable='', font=('Helvetica 18'), width=3, height=3, bg="#fff").grid(row=5 + n // 10,
                                                                                             column=n % 10)
    Label(window, textvariable='', font=('Helvetica 18'), width=3, height=3, bg="#fff").grid(row=5 + n // 10,
                                                                                             column=n % 10)
    Label(window, textvariable='', font=('Helvetica 18'), width=3, height=3, bg="#fff").grid(row=5 + n // 10,
                                                                                             column=n % 10)
    for i in alphabet3:
        Button(window, text=i, command=lambda i=i: if_guess(i), font=('Helvetica 18'), width=5, height=3, bg="#263d42",
               fg="white", bd=1, activebackground="#3e646c", activeforeground="pink").grid(row=5 + n // 11,
                                                                                           column=n % 11)
        n += 1

    """
    button for call get_help function and give hint to the user 
    """
    Button(window, text='hint', command=lambda: get_help(word_for_guess), font=('Helvetica 18'), width=5,
           height=3, bg="#263d42", fg="white", bd=1, activebackground="#3e646c", activeforeground="pink").grid(row=5,
                                                                                                               column=10,
                                                                                                               sticky='NSWE')
    if_user_want_to_play()






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
>>>>>>> adaa388ab74afb1fd60c75f91361769e58b6d7ec
