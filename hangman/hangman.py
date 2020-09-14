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






