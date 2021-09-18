import math
import sympy as sp
import result_display
import ctypes


def weaker(gear_Sut, pinion_Sut, gear_teeth, pinion_teeth, pressure_angle):
    print(gear_teeth, pinion_teeth)
    if (pressure_angle == '20˚ Full Depth Involute'):
        Yp = 0.484 - (2.87 / pinion_teeth)
        Yg = 0.484 - (2.87 / gear_teeth)
    elif (pressure_angle == '20˚ Stub Tooth Involute'):
        Yp = 0.55 - (2.64 / pinion_teeth)
        Yg = 0.55 - (2.64 / gear_teeth)
    elif (pressure_angle == '14.5˚ Full Depth Involute'):
        Yp = 0.39 - (2.15 / pinion_teeth)
        Yg = 0.39 - (2.15 / gear_teeth)

    if (gear_Sut == pinion_Sut):
        return 'pinion', Yp, pinion_Sut
    elif ((gear_Sut / 3) * Yg > (pinion_Sut / 3) * Yp):
        return 'pinion', Yp, pinion_Sut
    else:
        return 'gear', Yg, gear_Sut


def safety(typ, module, power, fos, Sut, Cs, b, Cm, C, gear_teeth, pinion_teeth, Q, K, Y, pinion_rpm, weak,
           helix_angle):
    tooth_width = b * module
    if typ == 'spur':
        pinion_diameter = module * pinion_teeth
        gear_diameter = module * gear_teeth
        A = 1
    elif typ == 'helical':
        pinion_diameter = (module * pinion_teeth) / (math.cos(math.radians(helix_angle)))
        gear_diameter = module * gear_teeth / (math.cos(math.radians(helix_angle)))
        A = 1
    elif typ == 'bevel':
        pinion_diameter = module * pinion_teeth
        gear_diameter = module * gear_teeth
        A = math.sqrt(((pinion_diameter / 2) ** 2) + ((gear_diameter / 2) ** 2))
        if ((A / 3) < 10 * module):
            tooth_width = math.ceil(A / 3)
        else:
            tooth_width = 10 * module
        print(A, tooth_width)

    addendum = module
    dedendum = 1.25 * module
    v = (math.pi * pinion_diameter * pinion_rpm) / 60000
    Pt = power * 1000 / v
    Sb = (Sut / 3) * module * tooth_width * Y
    if typ == 'spur':
        Sw = pinion_diameter * tooth_width * Q * K
        Pd = ((21 * v) * ((tooth_width * C) + (Cs * Cm * Pt)) / (
                    21 * v + math.sqrt((tooth_width * C) + (Cs * Cm * Pt))))
    elif typ == 'helical':
        Sw = pinion_diameter * tooth_width * Q * K / ((math.cos(math.radians(helix_angle))) ** 2)
        Pd = ((21 * v) * ((tooth_width * C * ((math.cos(math.radians(helix_angle))) ** 2)) + (Cs * Cm * Pt)) * (
            math.cos(math.radians(helix_angle))) / (21 * v + math.sqrt(
            (tooth_width * C * ((math.cos(math.radians(helix_angle))) ** 2)) + (Cs * Cm * Pt))))
    if typ == 'bevel':
        dedendum = 1.2 * module
        Sb = (Sut / 3) * module * tooth_width * Y * (1 - (tooth_width / A))
        Sw = 0.75 * pinion_diameter * tooth_width * Q * K / (math.cos(math.atan(pinion_teeth / gear_teeth)))
        Pd = ((21 * v) * ((tooth_width * C) + (Cs * Cm * Pt)) / (
                    21 * v + math.sqrt((tooth_width * C) + (Cs * Cm * Pt))))
        print('123', Sb, Sw, Pd)

    Peff = ((Cs * Cm * Pt) + Pd)

    print('V', v)
    print('Bearing Strength', Sb)
    print('Wear Strength', Sw)
    print('Ft', Pt)
    print('Feff', Peff)
    print('Fd', Pd)
    print('addendum', addendum)
    print('Dedendum', dedendum)
    print('module', module)
    print('tooth width', tooth_width)
    print('Pinion diameter', pinion_diameter)
    print('Gear diameter', gear_diameter)
    if (Sb > Sw):
        if (Sw / Peff) > fos:
            print('Safe')
            result_display.display(
                [round(gear_diameter, 2), round(pinion_diameter, 2), round(gear_teeth, 2), round(pinion_teeth, 2),
                 round(tooth_width, 2), round(addendum, 2), round(dedendum, 2), round(module, 2), weak,
                 round(module / math.cos(math.radians(helix_angle)), 2),
                 round((gear_diameter + pinion_diameter) / 2, 2),
                 round(math.degrees(math.atan(pinion_teeth / gear_teeth)), 2),
                 round(math.degrees(math.atan(gear_teeth / pinion_teeth)), 2), round(A, 2), typ])
            return 'Safe'
        else:
            print('Unsafe')
            return 'Unsafe'
    else:
        if (Sb / Peff) > fos:
            print('Safe')
            result_display.display(
                [round(gear_diameter, 2), round(pinion_diameter, 2), round(gear_teeth, 2), round(pinion_teeth, 2),
                 round(tooth_width, 2), round(addendum, 2), round(dedendum, 2), round(module, 2), weak,
                 round(module / math.cos(math.radians(helix_angle)), 2),
                 round((gear_diameter + pinion_diameter) / 2, 2),
                 round(math.degrees(math.atan(pinion_teeth / gear_teeth)), 2),
                 round(math.degrees(math.atan(gear_teeth / pinion_teeth)), 2), round(A, 2), typ])
            return 'Safe'
        else:
            print('Unsafe')
            return 'Unsafe'


def solve(spur_gear, typ, power, gear_ratio, gear_grade, pinion_teeth, pinion_bhn, gear_bhn, fos, pinion_rpm, gear_Sut,
          pinion_Sut, Cs, pressure_angle, Cv, tooth_width, Cm, C, helix_angle):
    print('-----------------------------------------------------')
    try:
        gear_teeth = float(math.ceil(gear_ratio * pinion_teeth))
        b = tooth_width
        m = sp.symbols('m', real=True)
        tooth_width = tooth_width * m
        if typ == 'spur':
            weak, Y, Sut = weaker(gear_Sut, pinion_Sut, gear_teeth, pinion_teeth, pressure_angle)
            pinion_diameter = m * pinion_teeth
        elif typ == 'helical':
            weak, Y, Sut = weaker(gear_Sut, pinion_Sut, (gear_teeth / ((math.cos(math.radians(helix_angle))) ** 3)),
                                  (pinion_teeth / ((math.cos(math.radians(helix_angle))) ** 3)), pressure_angle)
            pinion_diameter = (m * pinion_teeth) / (math.cos(math.radians(helix_angle)))
        elif typ == 'bevel':
            m = sp.symbols('m', real=True, positive=True)
            weak, Y, Sut = weaker(gear_Sut, pinion_Sut, gear_teeth / (math.cos(math.atan(gear_teeth / pinion_teeth))),
                                  pinion_teeth / (math.cos(math.atan(pinion_teeth / gear_teeth))), pressure_angle)
            pinion_diameter = m * pinion_teeth
            gear_diameter = m * gear_teeth
            A = sp.sqrt(((pinion_diameter / 2) ** 2) + ((gear_diameter / 2) ** 2))
            if ((A / 3).coeff(m) < 10):
                tooth_width = (round((A / 3).coeff(sp.sqrt(m ** 2)))) * m
            else:
                tooth_width = 10 * m
            print('123', tooth_width, pinion_diameter, gear_diameter)
        #        print(weak)
        print(gear_teeth, tooth_width, pinion_teeth, Y)
        v = (math.pi * pinion_diameter * pinion_rpm) / 60000
        if Cv == '5.6/(5.6+√v)':
            Cv = str(5.6 / (5.6 + v ** 0.5))

        Pt = power * 1000 / v
        Peff = Cs * Cm * Pt / eval(Cv)
        Sb = (Sut / 3) * m * tooth_width * Y
        Q = 2 * gear_teeth / (gear_teeth + pinion_teeth)
        if weak == 'pinion':
            K = 0.16 * ((pinion_bhn / 100) ** 2)
        elif weak == 'gear':
            K = 0.16 * ((gear_bhn / 100) ** 2)

        if typ == 'spur':
            Sw = pinion_diameter * tooth_width * Q * K
        elif typ == 'helical':
            Sw = pinion_diameter * tooth_width * Q * K / ((math.cos(math.radians(helix_angle))) ** 2)
        elif typ == 'bevel':
            Sb = (Sut / 3) * m * tooth_width * Y * (1 - (tooth_width / A))
            Q = 2 * gear_teeth / (gear_teeth + (pinion_teeth * pinion_teeth / gear_teeth))
            Sw = 0.75 * pinion_diameter * tooth_width * Q * K / (math.cos(math.atan(pinion_teeth / gear_teeth)))
        print('123', Sb, Q, Sw)

        if (Sb.coeff(m ** 2) > Sw.coeff(m ** 2)):
            print(1)
            ans = sp.solve((Sw - fos * Peff), m)
        else:
            print(Sb - fos * Peff)
            ans = sp.solve((Sb - fos * Peff), m)
        print(ans)

        del pinion_diameter, tooth_width, v, Pt, Sb, Sw, m, Peff
        flag = 0
        status = 'Unsafe'
        for q in ans:
            print(3)
            if ('I' not in str(q) and q > 0):
                flag = 1
                module = float(math.ceil(q))
                status = safety(typ, module, power, fos, Sut, Cs, b, Cm, C, gear_teeth, pinion_teeth, Q, K, Y,
                                pinion_rpm, weak, helix_angle)
                if (status == 'Safe'):
                    #                    print('**********************************************************************')
                    break
                else:
                    continue
            else:
                status = 'Unsafe'
                continue
        #        print(status)
        if status == 'Unsafe':
            while status == 'Unsafe':
                if (status == 'Unsafe'):
                    if flag == 1:
                        module = module + 1
                    elif (flag == 0):
                        module = 1
                        flag = 1
                    status = safety(typ, module, power, fos, Sut, Cs, b, Cm, C, gear_teeth, pinion_teeth, Q, K, Y,
                                    pinion_rpm, weak, helix_angle)
                    if (status == 'Safe'):
                        #                        print('**************************************************************************')
                        break
                    else:
                        continue
    except:
        val = ctypes.windll.user32.MessageBoxW(0,
                                               'There was an error solving the problem!!!\nPlease restart the application and try again!!!',
                                               'Functioning Error', 16)
        spur_gear.destroy()

# 2.Exception handling 3.Dimensions 4.3D
