from tkinter import *
from PIL import ImageTk, Image
import gears


def destroy_window(page, typ):
    page.destroy()
    gears.spur_start(typ)


def start():
    gear = Tk()
    #    width =int(gear.winfo_screenwidth())
    #    height =int(gear.winfo_screenheight())
    #    print(height,width)
    width = 1300
    height = 700
    gear.geometry(str(width) + 'x' + str(height))
    #    gear.resizable(False,False)
    gear.title('Gear Design')
    gear.configure(background='slate gray')

    spur_image = ImageTk.PhotoImage(Image.open(r"6.jpg"))
    helical_image = ImageTk.PhotoImage(Image.open(r"4.jpg"))
    exit_image = ImageTk.PhotoImage(Image.open(r"0.jpg"))
    bevel_image = ImageTk.PhotoImage(Image.open(r"5.jpg"))
    gear_image = ImageTk.PhotoImage(Image.open(r"7.png"))

    Label(gear, text='GEAR DESIGN', font='Times 80 bold underline', bg='slate gray').place(x=290, y=200)
    w = Canvas(gear, width=200, height=175)
    w.create_image(100, 87, image=gear_image)
    w.place(x=10, y=10)

    spur_button = Button(gear, text='Spur Gear', command=lambda: destroy_window(gear, 'spur'), image=spur_image,
                         compound='top', font=30, bd=7).place(x=110, y=500)
    helical_button = Button(gear, text='Helical Gear', command=lambda: destroy_window(gear, 'helical'),
                            image=helical_image, compound='top', font=30, bd=7).place(x=430, y=500)
    bevel_button = Button(gear, text='Bevel Gear', command=lambda: destroy_window(gear, 'bevel'), image=bevel_image,
                          compound='top', font=30, bd=7).place(x=750, y=500)
    exit_button = Button(gear, text='Exit', command=lambda: gear.destroy(), image=exit_image, compound='top', font=30,
                         bd=7).place(x=1070, y=500)

    gear.mainloop()


if __name__ == '__main__':
    start()
