from tkinter import *
from tkinter import ttk 
import PIL
from PIL import ImageTk,Image
from tkinter import filedialog


root = Tk()
root.title("Aayu Wifi HeatMap")
root.geometry("700x600")
root.config(bg ='#292929')
root.resizable(False,False)
root.iconbitmap('D:/Aayu_personal/WIFI Range Identifier/pics/heatmapicon.ico')

pro_select = 0
ac_select = 0

def move2(e):
    x = 600//2
    y = 400//2

    global img8
    global img9

    img8 = PhotoImage(file='pics/heatmap3.png')
    my_image8 = canvas6.create_image(e.x, e.y, image=img8)

    img9 = PhotoImage(file='pics/macpro.png')
    my_image9 = canvas6.create_image(e.x, e.y, image=img9)

    my_label.config(text="Coordinates: x = "+ str(e.x) + "y  = " + str(e.y))



def move(e):
    x = 600//2
    y = 400//2

    global img5
    global img6
    global count

    img5 = PhotoImage(file='pics/heatmap2.png')
    my_image5 = canvas6.create_image(e.x, e.y, image=img5)

    img6 = PhotoImage(file='pics/macpro.png')
    my_image6 = canvas6.create_image(e.x, e.y, image=img6)

    my_label.config(text="Coordinates: x = "+ str(e.x) + ' y = ' + str(e.y))

def pro_func(event):
    global pro_select
    pro_select += 1

    if pro_select >= 1:
        canvas6.bind('<B1-Motion>', move)

def pro_func2(event):
    global pro_select
    pro_select += 1

    if pro_select >= 1:
        canvas6.bind('<B1-Motion>',move2)

def importsite():
    apps = []
    filename = filedialog.askopenfilename(initialdir='D:',title='Select Files')
    filetypes=("all files","*.*")
    apps.append(filename)

    global canvas6
    global photo6

    canvas6 = Canvas(main_canvas, height=8, width=17,bg='white')
    photo6 = ImageTk.PhotoImage(file = apps[0])
    item6 = canvas6.create_image(310,210,image=photo6)
    canvas6.place(relx=0,rely=0,relheight=1,relwidth=1)



def donothing():
    pass

    


main_canvas = Canvas(root, width=600, height=400, bg='white')
main_canvas.pack(pady=10)

bottom_canvas = Canvas(root, width=600, height=120, bg='#383838')
bottom_canvas.pack()

my_label = Label(root, text='', bg='#292929', fg='white')
my_label.pack(side="bottom")

img = PhotoImage(file = 'pics/apicon.png')
imglabel = Label(bottom_canvas, image=img, bg = '#383838')
imglabel.bind('<Button-1>',pro_func)
imglabel.place(relx=0.03,rely=0.13)

img2= PhotoImage(file = 'pics/macpro.png')
imglabel = Label(bottom_canvas, image=img2, bg = '#383838')
imglabel.bind('<Button-1>',pro_func2)
imglabel.place(relx=0.28,rely=0.26)

acpro_label = Label(bottom_canvas,text="Aayu's AC-AP-PRO",font=('helvetica',10), bg = '#383838', fg= 'white')
acpro_label.place(relx=0.03, rely=0.7)

ac_label = Label(bottom_canvas,text="Aayu's AC-AP Lite",font=('helvetica',10),bg = '#383838',fg= 'white')
ac_label.place(relx=0.25, rely=0.7)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Import",command = importsite)
filemenu.add_command(label='Save', command = donothing)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)
menubar.add_cascade(label='File',menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Info",command =donothing)
menubar.add_cascade(label='Help',menu=helpmenu)


root.config(menu=menubar)











root.mainloop()