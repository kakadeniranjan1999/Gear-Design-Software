from tkinter import *


# [gear_diameter,pinion_diameter,gear_teeth,pinion_teeth,tooth_width,addendum,dedendum,module]

def display(content):
    display_gui = Tk()
    display_gui.geometry('1000x600')
    display_gui.resizable(False, False)
    display_gui.title('Design Parameters')
    display_gui.configure(background='slate gray')

    Label(display_gui, text='Solution:', font='Times 24 bold', fg='green3', bg='slate gray').place(x=20, y=10)
    Label(display_gui, text=str(content[8]).upper() + ' is weaker', font='Times 22', bg='slate gray', fg='Red').place(
        x=170, y=15)
    Label(display_gui, text='Gear Diameter (d₉): ' + str(content[0]) + ' mm', font='Times 20', bg='slate gray').place(
        x=30, y=80)
    Label(display_gui, text='Pinion Diameter (dₚ): ' + str(content[1]) + ' mm', font='Times 20',
          bg='slate gray').place(x=30, y=150)
    Label(display_gui, text='Gear Teeth (z₉): ' + str(content[2]), font='Times 20', bg='slate gray').place(x=30, y=220)
    Label(display_gui, text='Pinion Teeth (zₚ): ' + str(content[3]), font='Times 20', bg='slate gray').place(x=30,
                                                                                                              y=290)
    Label(display_gui, text='Centre Distance (a): ' + str(content[10]) + ' mm', font='Times 20',
          bg='slate gray').place(x=30, y=360)
    Label(display_gui, text='Tooth Width (b): ' + str(content[4]) + ' mm', font='Times 20', bg='slate gray').place(
        x=500, y=80)
    Label(display_gui, text='Addendum (hₐ): ' + str(content[5]) + ' mm', font='Times 20', bg='slate gray').place(x=500,
                                                                                                                  y=150)
    Label(display_gui, text='Dedendum (hₔ): ' + str(content[6]) + ' mm', font='Times 20', bg='slate gray').place(x=500,
                                                                                                                  y=220)

    if (content[14] == 'helical'):
        Label(display_gui, text='Normal Module (mₙ): ' + str(content[7]) + ' mm', font='Times 20',
              bg='slate gray').place(x=500, y=290)
        Label(display_gui, text='Transverse Module (mₜ): ' + str(content[9]) + ' mm', font='Times 20',
              bg='slate gray').place(x=500, y=360)
    elif (content[14] == 'bevel'):
        Label(display_gui, text='Module (m): ' + str(content[7]) + ' mm', font='Times 20', bg='slate gray').place(
            x=500, y=290)
        Label(display_gui, text='Pinion Cone Angle (γₚ): ' + str(content[11]) + '°', font='Times 20',
              bg='slate gray').place(x=30, y=430)
        Label(display_gui, text='Gear Cone Angle (γ₉): ' + str(content[12]) + '°', font='Times 20',
              bg='slate gray').place(x=500, y=430)
        Label(display_gui, text='Pitch Cone Diameter (A): ' + str(content[13]) + ' mm', font='Times 20',
              bg='slate gray').place(x=500, y=360)
    else:
        Label(display_gui, text='Module (m): ' + str(content[7]) + ' mm', font='Times 20', bg='slate gray').place(
            x=500, y=290)
    display_gui.mainloop()

# display([100,250,230,40,22,78,36,780,'pinion',100,100,100,100,100,'bevel'])
