# Importing necessary modules
import tkinter
from tkinter import *
from gtts import gTTS
from playsound import playsound

# Initializing Window
root = Tk()
root.geometry("500x300")
root.configure(bg = 'ghost white')
root.title("TTS")

Label(root, text = "TEXT_TO_SPEECH_Converter", font = "arial 20 bold", bg = "white smoke").pack()

Msg = StringVar()
Label(root, text = "Enter Text", font = 'arial 15 bold', bg = 'white smoke').place(x= 20, y=60)
entry_field = Entry(root, textvariable = Msg , width = '50')
entry_field.place(x = 20, y = 100)

# Function to Convert Text To Speech To Python
def Text_to_Speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('/home/asif/Python/Small Projects/Asif.mp3')
    playsound('/home/asif/Python/Small Projects/Asif.mp3')

# Function to Exit
def Exit():
    root.destroy()

# Function to Reset
def Reset():
    Msg.set("")

# Define Buttons
Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_Speech, width = '5',fg = 'white', bg = 'Green').place(x = 25, y = 140)
Button(root , font = 'arial 15 bold', text = 'EXIT', width = '5', command = Exit ,fg = 'white', bg = 'Red').place(x = 100, y = 140)
Button(root, font = 'arial 15 bold', text = 'RESET', width = '5', command = Reset,fg = 'white', bg = 'Orange').place(x = 175, y = 140)

root.mainloop()