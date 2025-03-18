from tkinter import *
import math
from PIL import ImageTk, Image
import solver
import main_page


def reset_all():
    power.set('')
    gear_ratio.set('')
    gear_grade.set('')
    pinion_teeth.set('')
    #    gear_teeth.set('')
    tooth_width.set(1.0)
    pinion_bhn.set('')
    gear_bhn.set('')
    fos.set('')
    pinion_rpm.set('')
    gear_Sut.set('')
    pinion_Sut.set('')
    Cs.set('')
    pressure_angle.set('Select')
    Cv.set('Select')
    Cm.set('')
    C.set('')
    helix_angle.set(0)


def destroy_win(pg):
    pg.destroy()
    main_page.start()


def spur_start(typ):
    spur_gear = Tk()
    # width =int(spur_gear.winfo_screenwidth())
    # height =int(spur_gear.winfo_screenheight())
    # print(height,width)
    width = 1300
    height = 700
    spur_gear.geometry(str(width) + 'x' + str(height))
    spur_gear.resizable(False, False)
    if typ == 'spur':
        spur_gear.title('Spur Gear Design')
    elif typ == 'helical':
        spur_gear.title('Helical Gear Design')
    else:
        spur_gear.title('Bevel Gear Design')
    spur_gear.configure(background='slate gray')

    global helix_angle, C, Cm, power, gear_ratio, gear_grade, pinion_teeth, tooth_width, pinion_bhn, gear_bhn, fos, pinion_rpm, gear_Sut, pinion_Sut, Cs, pressure_angle, Cv  # ,gear_teeth

    power = DoubleVar()
    gear_ratio = DoubleVar()
    gear_grade = DoubleVar()
    pinion_teeth = DoubleVar()
    #    gear_teeth=DoubleVar()
    tooth_width = DoubleVar()
    pinion_bhn = DoubleVar()
    gear_bhn = DoubleVar()
    fos = DoubleVar()
    pinion_rpm = DoubleVar()
    pinion_Sut = DoubleVar()
    gear_Sut = DoubleVar()
    Cs = DoubleVar()
    pressure_angle = StringVar()
    Cv = StringVar()
    Cm = DoubleVar()
    C = DoubleVar()
    helix_angle = DoubleVar()

    power_label = Label(spur_gear, text="Power (kW):", font='Times 20 bold', bg='slate gray').place(x=30, y=20)
    power_entry = Entry(spur_gear, textvariable=power, font='Times 20 bold', width=10)
    power_entry.place(x=210, y=20)

    fos_label = Label(spur_gear, text="FOS:", font='Times 20 bold', bg='slate gray').place(x=30, y=90)
    fos_entry = Entry(spur_gear, textvariable=fos, width=10, font='Times 20 bold')
    fos_entry.place(x=210, y=90)

    gear_ratio_label = Label(spur_gear, text="Gear Ratio:", font='Times 20 bold', bg='slate gray').place(x=30, y=160)
    gear_ratio_entry = Entry(spur_gear, font='Times 20 bold', textvariable=gear_ratio, width=10)
    gear_ratio_entry.place(x=210, y=160)

    gear_grade_label = Label(spur_gear, text="Gear Grade:", font='Times 20 bold', bg='slate gray').place(x=30, y=230)
    gear_grade_entry = Entry(spur_gear, textvariable=gear_grade, width=10, font='Times 20 bold')
    gear_grade_entry.place(x=210, y=230)

    #    gear_teeth_label=Label(spur_gear,text="Gear Teeth:",font='Times 20 bold').place(x=30,y=440)
    #    gear_teeth_entry=Entry(spur_gear,textvariable=gear_teeth,font='Times 20 bold')
    #    gear_teeth_entry.place(x=210,y=440)

    pinion_bhn_label = Label(spur_gear, text="Pinion BHN:", font='Times 20 bold', bg='slate gray').place(x=30, y=300)
    pinion_bhn_entry = Entry(spur_gear, textvariable=pinion_bhn, width=10, font='Times 20 bold')
    pinion_bhn_entry.place(x=210, y=300)

    gear_bhn_label = Label(spur_gear, text="Gear BHN:", font='Times 20 bold', bg='slate gray').place(x=30, y=370)
    gear_bhn_entry = Entry(spur_gear, textvariable=gear_bhn, width=10, font='Times 20 bold')
    gear_bhn_entry.place(x=210, y=370)

    pinion_teeth_label = Label(spur_gear, text="Pinion Teeth:", font='Times 20 bold', bg='slate gray').place(x=30,
                                                                                                              y=440)
    pinion_teeth_entry = Entry(spur_gear, textvariable=pinion_teeth, width=10, font='Times 20 bold')
    pinion_teeth_entry.place(x=210, y=440)

    pinion_Sut_label = Label(spur_gear, text="Pinion Sut (MPa):", font='Times 20 bold', bg='slate gray').place(x=400,
                                                                                                                y=20)
    pinion_Sut_entry = Entry(spur_gear, textvariable=pinion_Sut, width=10, font='Times 20 bold')
    pinion_Sut_entry.place(x=670, y=20)

    gear_Sut_label = Label(spur_gear, text="Gear Sut (MPa):", font='Times 20 bold', bg='slate gray').place(x=400, y=90)
    gear_Sut_entry = Entry(spur_gear, textvariable=gear_Sut, width=10, font='Times 20 bold')
    gear_Sut_entry.place(x=670, y=90)

    pinion_rpm_label = Label(spur_gear, text="Pinion RPM (rpm):", font='Times 20 bold', bg='slate gray').place(x=400,
                                                                                                                y=160)
    pinion_rpm_entry = Entry(spur_gear, textvariable=pinion_rpm, width=10, font='Times 20 bold')
    pinion_rpm_entry.place(x=670, y=160)

    Cs_label = Label(spur_gear, text="Service Factor:", font='Times 20 bold', bg='slate gray').place(x=400, y=230)
    Cs_entry = Entry(spur_gear, textvariable=Cs, width=10, font='Times 20 bold')
    Cs_entry.place(x=670, y=230)

    pressure_angle.set('Select')
    pressure_angle_label = Label(spur_gear, text="Pressure Angle (α˚):", font='Times 20 bold', bg='slate gray').place(
        x=400, y=370)
    pressure_angle_entry = OptionMenu(spur_gear, pressure_angle,
                                      *['Select', '14.5˚ Full Depth Involute', '20˚ Full Depth Involute',
                                        '20˚ Stub Tooth Involute'])
    pressure_angle_entry.place(x=670, y=370)
    pressure_angle_entry.config(font='Times 20 bold', bg='white', width=9)

    Cv.set('Select')
    Cv_label = Label(spur_gear, text="Velocity Factor:", font='Times 20 bold', bg='slate gray').place(x=400, y=300)
    Cv_entry = OptionMenu(spur_gear, Cv, *['Select', '3/(3+v)', '6/(6+v)', '5.6/(5.6+√v)'])
    Cv_entry.place(x=670, y=300)
    Cv_entry.config(font='Times 20 bold', bg='white', width=9)

    Cm_label = Label(spur_gear, text="Load Factor:", font='Times 20 bold', bg='slate gray').place(x=400, y=440)
    Cm_entry = Entry(spur_gear, textvariable=Cm, width=10, font='Times 20 bold')
    Cm_entry.place(x=670, y=440)

    C_label = Label(spur_gear, text="Deformation Factor:", font='Times 20 bold', bg='slate gray').place(x=850, y=20)
    C_entry = Entry(spur_gear, textvariable=C, width=10, font='Times 20 bold')
    C_entry.place(x=1125, y=20)

    if typ == 'spur' or typ == 'helical':
        tooth_width_label = Label(spur_gear, text="Tooth Width:", font='Times 20 bold', bg='slate gray').place(x=850,
                                                                                                                y=90)
        tooth_width_entry = Entry(spur_gear, textvariable=tooth_width, width=6, font='Times 20 bold').place(x=1050,
                                                                                                            y=90)
        Label(spur_gear, text="x module", font='Times 20 bold', bg='slate gray').place(x=1140, y=85)

    if typ == 'helical':
        helix_angle_label = Label(spur_gear, text="Helix Angle (ψ˚):", font='Times 20 bold', bg='slate gray').place(
            x=850, y=160)
        helix_angle_entry = Entry(spur_gear, textvariable=helix_angle, width=10, font='Times 20 bold').place(x=1125,
                                                                                                             y=160)

    solution_image = ImageTk.PhotoImage(Image.open(r"2.jpg"))
    main_menu_image = ImageTk.PhotoImage(Image.open(r"1.png"))
    exit_image = ImageTk.PhotoImage(Image.open(r"0.jpg"))
    reset_image = ImageTk.PhotoImage(Image.open(r"3.jpg"))

    main_menu = Button(spur_gear, text='Main Menu', command=lambda: destroy_win(spur_gear), image=main_menu_image,
                       compound='top', font=30, bd=7).place(x=110, y=500)
    solution = Button(spur_gear, text='Solve',
                      command=lambda: solver.solve(spur_gear, typ, power.get(), gear_ratio.get(), gear_grade.get(),
                                                   pinion_teeth.get(), pinion_bhn.get(), gear_bhn.get(), fos.get(),
                                                   pinion_rpm.get(), gear_Sut.get(), pinion_Sut.get(), Cs.get(),
                                                   pressure_angle.get(), Cv.get(), tooth_width.get(), Cm.get(), C.get(),
                                                   helix_angle.get()), image=solution_image, compound='top', font=30,
                      bd=7).place(x=430, y=500)
    reset = Button(spur_gear, text='Reset All', command=lambda: reset_all(), image=reset_image, compound='top', font=30,
                   bd=7).place(x=750, y=500)
    exit_button = Button(spur_gear, text='Exit', command=lambda: spur_gear.destroy(), image=exit_image, compound='top',
                         font=30, bd=7).place(x=1070, y=500)

    reset_all()

    spur_gear.mainloop()
