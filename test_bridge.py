
import Tkinter as tk
from Tkinter import *
from PIL import Image, ImageTk
import os
import time
from HX711 import HX711
from HX711 import *


READING = FALSE
hx = HX711()
offset = hx.getValue()
global Max
Max = 0

#Original offset
#offset = hx.getValue()-2.8
	
#Defining Functions
def Read():				# Include the Value of the weight here by calling the Load Cell Programs
	global reading 
	global scaledValue
	global Max
	value = hx.getValue()
	scaledValue = (value - offset)*(0.0022)*(0.035528)
	scaledValue = round(scaledValue,1)
	if scaledValue > Max:
		Max = scaledValue
	weightText.config(text = (str(scaledValue)))
	reading = MainWindow.after(1000,Read)

#Original function
#scaledValue = (value - offset)*(0.0022)*(0.0155957) #(sample-count)(grams to pounds)(Scale factor Per LoadCell)

def StopReading(): 
	global reading 
	global scaledValue
	global Max
	weightTextMax.config(text = (str(Max)))
	MainWindow.after_cancel(reading)
	MessageMax.lift()
	weightTextMax.lift()
	LbsMax.lift()
	
def Reset():
	global scaledValue
	global Max
	scaledValue = 0
	Max = 0
	scaledValue = round(scaledValue,2)
	weightText.config(text = (str(scaledValue)))
	MessageMax.lower()
	weightTextMax.lower()
	LbsMax.lower()

MainWindow = Tk()

MainWindow.configure(background='orange')


#Buttons
StartButton = Button(MainWindow, text = "START", command = Read , height= 10, width =20, font=("Times New Roman", 30), bg = "blue",  fg = "orange")
StopButton = Button(MainWindow, text = "STOP", command = StopReading, height = 10, width = 20, font=("Times New Roman", 30), bg = "blue", fg = "orange")
ResetButton = Button(MainWindow, text = "RESET", command = Reset, height = 10, width = 20, font=("Times New Roman", 30), bg = "blue", fg = "orange")

StartButton.pack()
StopButton.pack()

#Labels
Message = Label(MainWindow, width = 15, height = "2" ,  text = "Current Load", bg = 'blue' , font=("Times New Roman", 80), fg = "orange")

MessageMax = Label(MainWindow, width = "15", height = "2" ,  text = "Congratulations!!", bg = 'red' , font=("Times New Roman", 80), fg = "blue")
weightText = Label(MainWindow, width = "6", height = "2" ,  text = "0", fg = 'orange', bg = 'blue')#,relief = RAISED)
weightTextMax = Label(MainWindow, width = "6", height = "2" ,  text = "MAX", fg = 'blue', bg = 'red')#relief = RAISED)
Lbs= Label(MainWindow, width = "4", height = "2" ,  text = "lbs ", bg = 'blue' , font=("Times New Roman", 80), fg = "orange")
LbsMax= Label(MainWindow, width = "4", height = "2" ,  text = "lbs ", bg = 'red' , font=("Times New Roman", 80), fg = "blue")

MessageMax.lower()
weightTextMax.lower()
LbsMax.lower()

weightText.config(font=("Times New Roman", 80))
weightTextMax.config(font=("Times New Roman", 80))
Lbs.config(font=("Times New Roman", 80))
LbsMax.config(font=("Times New Roman", 80))

weightText.place( x = 790 , y = 100)
Message.place( x = 50 , y = 100)
Lbs.place( x = 1100 , y = 100)
LbsMax.place( x = 1100 , y = 100)

MessageMax.place(x = 50, y = 100)
weightTextMax.place( x = 800 , y = 100)

#Pictures
aliefLogo = (Image.open("alief_new.png"))
aliefLogo = ImageTk.PhotoImage(aliefLogo)
uttLogo = (Image.open("utt_new.png"))
uttLogo = ImageTk.PhotoImage(uttLogo)
bridge = (Image.open("b5.png"))
bridge = bridge.resize((600, 250), Image.ANTIALIAS) #
bridge = ImageTk.PhotoImage(bridge)
aLogo = Label(MainWindow, image = aliefLogo , bg = 'light blue')
aLogo.place(x=75, y = 550)
uLogo = Label(MainWindow, image = uttLogo , bg = 'orange')
uLogo.place(x=1000, y =500)
bPic = Label(MainWindow, image = bridge , bg = 'orange')
bPic.place(x=360, y =500)

StartButton.place(x = 400, y = 375)
StopButton.place(x = 600, y = 375)
ResetButton.place(x = 800, y = 375)
StartButton.config(height = 2, width = 8)
StopButton.config(height = 2, width = 8)
ResetButton.config(height = 2, width = 8)

MainWindow.state('normal')
MainWindow.attributes('-fullscreen',True)
MainWindow.mainloop()

