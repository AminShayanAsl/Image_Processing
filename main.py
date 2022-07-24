from tkinter import *
from functions import *

my_w = Tk()
my_w.geometry("550x950")  # Size of the window 
my_w.config(bg='cyan')

my_w.title('Image Processing')
my_font1=('times', 15, 'bold')

label = Label(my_w,text='\nWelcome :)',width=50,font=my_font1)  
label.grid(row=1,column=1,columnspan=4)
label.config(bg='cyan')

l1 = Label(my_w,text='\n\nUpload Main Image',width=50,font=my_font1)  
l1.grid(row=2,column=1,columnspan=4)
l1.config(bg='cyan')

b1 = Button(my_w, text='Upload Files', width=20,command = lambda:upload_file(my_w,3,4))
b1.grid(row=3,column=1,columnspan=4)
b1.config(bg='yellow')

l2 = Label(my_w,text='\n\nUpload Sample Image',width=50,font=my_font1)  
l2.grid(row=5,column=1,columnspan=4)
l2.config(bg='cyan')

b2 = Button(my_w, text='Upload Files', width=20,command = lambda:upload_file(my_w,3,7))
b2.grid(row=6,column=1,columnspan=4)
b2.config(bg='yellow')

b3 = Button(my_w, text='Find Location', width=20,command = lambda:imageProcessing(my_w))
b3.grid(row=8,column=1,columnspan=4)
b3.config(bg='green')
               
my_w.mainloop()  # Keep the window open
