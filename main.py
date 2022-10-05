from gtts import gTTS #google text to speech
from playsound import playsound
from tkinter import *

root = Tk()
root.geometry('600x600')
root.title('TTS Project')
root.config(bg='gray')

Label(root, text = 'TEXT TO SPEECH' , font='arial 20 bold' , bg ='white smoke').pack()
Label(root, text ='Enter Text', font ='arial 15 bold', bg ='white smoke').place(x=20,y=60)

#text variable
Msg = StringVar()
#Entry
input_field = Entry(root, textvariable=Msg, width = '60')
input_field.place(x=20, y=100)

def tts():
    Message = input_field.get()
    speech = gTTS(text = Message)
    speech.save('Output.mp3')
    playsound('Output.mp3')
def Exit():
    root.destroy()
def Reset():
    Msg.set("")
    
Button(root, text = "Play" , font = 'arial 15 bold', command = tts, width =4).place(x=25, y=140)
Button(root,text = 'Exit',font = 'arial 15 bold' , command = Exit, bg = 'Red').place(x=100,y=140)
Button(root, text = 'Reset', font='arial 15 bold', command = Reset).place(x=175 , y =140)

root.mainloop()

