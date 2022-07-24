from tkinter import *
import cv2
import os
import json
from cv2 import matchTemplate
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

global master_img_add
sample_img_add = ''


def upload_file(my_w, col, row):
    f_types = [('Jpg Files', '*.jpg'), ('PNG Files','*.png'), ('JPEG Files','*.jpeg')]   # type of files to select 
    filename = filedialog.askopenfilename(multiple=True,filetypes=f_types)

    data = {}

    if row==4:
        data['master_img_add'] = filename[0]
        json_string = json.dumps(data)
        with open('img_add.json', 'w') as outfile:
            outfile.write(json_string)
    elif row==7:
        with open("img_add.json", "r") as jsonFile:
            data = json.load(jsonFile)

        data['sample_img_add'] = filename[0]

        with open("img_add.json", "w") as jsonFile:
            json.dump(data, jsonFile)

    col=col # start from column 1
    row=row # start from row 3 
    img=Image.open(filename[0]) # read the image file
    img=img.resize((300,300)) # new width & height
    img=ImageTk.PhotoImage(img)
    e1 = Label(my_w)
    e1.grid(row=row,column=col)
    e1.image = img
    e1['image']=img # garbage collection  


def imageProcessing(my_w):
    with open('img_add.json') as json_file:
        data = json.load(json_file)

    master_img = cv2.imread(str(data['master_img_add']))
    sample_img = cv2.imread(str(data['sample_img_add']))

    w, h = sample_img.shape[:2]

    res = matchTemplate(master_img, sample_img, cv2.TM_CCOEFF)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) 

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    x = (top_left[0] + bottom_right[0])/2
    master_y = (top_left[1] + bottom_right[1])/2
    y = abs(master_img.shape[1] - master_y)

    my_font1=('times', 15, 'bold')

    x_str = "\nx : " + str(x)
    y_str = "y : " + str(y)

    label = Label(my_w,text=x_str,width=50,font=my_font1)  
    label.grid(row=9,column=1,columnspan=4)
    label.config(bg='cyan')

    l1 = Label(my_w,text=y_str,width=50,font=my_font1)  
    l1.grid(row=10,column=1,columnspan=4)
    l1.config(bg='cyan')

    cv2.rectangle(master_img, top_left, bottom_right, 255, 3)
    cv2.circle(master_img, (int(x), int(master_y)), 5, 255, -1)
    cv2.imshow("img", master_img)

    os.remove('img_add.json')

    cv2.waitKey(0)
    cv2.destroyAllWindows()
