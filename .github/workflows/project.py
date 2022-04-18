import decimal
import math

speed_value = []
height_value = []
plotnost_value = []

h1 = float(input('Высота выбраcывания груза (м) - '))
h1_ = float(input('Высота раскрытия парашюта (м) - '))
g = 9.806
m = float(input('Масса груза(кг) - '))
h_ = float(input('Ширина груза(м) - '))
b = float(input('Длина груза(м) - '))
S1 = h_ * b
p = 1.225 * ((1 - 2.25 * (10 ** (-5)) * h1) ** 4.2559)
Cx1 = 0.5
Cx2 = 2
S2 = float(input('Площадь купола парашюта(м^2) - '))

if h1<1000 or h1_<100 or m<5 or h_<0.1 or b<0.1 or S2<10 or S2>200 or h1>7000 or h1_>7000 or m>10000 or h_>15 or b>15:
    print('Введите, пожалуйста, значения в следующем диапазоне:')
    print('Высота сбрасывания груза - от 1000 до 7000 м')
    print('Высота раскрытия парашюта - от 100 до 7000 м')
    print('Масса груза- от 5 до 10000 кг')
    print('Ширина груза - от 0.1 до 25 м')
    print('Длина груза - от 0.1 до 15 м')
    exit()

def toFixed(numObj, digits = 0):
    return f"{numObj:.{digits}f}"

def dvdt(v):
    return g - (Cx1 * p * (v ** 2) * S1)/(2 * m)
t = 0
h = 0.01
Cx = Cx1
S = S1
V = 0

while h1 > h1_:
    V1 = h * dvdt(V)
    V2 = h * dvdt(V + V1/2)
    V3 = h * dvdt(V + V2/2)
    V4 = h * dvdt(V + V3)
    
    
    VV = float(toFixed((1.0 / 6.0) * (V1 + 2*V2 + 2*V3 +V4), 6))
    V += VV
    hh1 = float(toFixed(V * h, 6))
    h1 -= hh1    
    
    
    p = 1.225 * ((1 - 2.25 * (10 ** (-5)) * h1) ** 4.2559)
    t += h
    speed_value.append(V)
    height_value.append(h1)
    plotnost_value.append(p)

print('Конечная скорость(м/с): ', speed_value[-1])

speed_value1 = []
height_value1 = []
h2_ = 0
p_ = 1.225 * ((1 - 2.25 * (10 ** (-5)) * h1_) ** 4.2559)

def dv1dt(v1):
    return g - (Cx2 * p_ * (v1 ** 2) * S2)/(2 * m)
t_ = 0
h_ = 0.01
V_ = 60.1161269999999

while h1_ >= h2_:
    V1_ = h_ * dv1dt(V_)
    V2_ = h_ * dv1dt(V_ + V1_/2)
    V3_ = h_ * dv1dt(V_ + V2_/2)
    V4_ = h_ * dv1dt(V_ + V3_)
    VV_ = float(toFixed((1.0 / 6.0) * (V1_ + 2*V2_ + 2*V3_ +V4_), 6))
    V_ += VV_
    hh1_ = float(toFixed(V_ * h_, 6))
    h1_ -= hh1_
    p_ = 1.225 * ((1 - 2.25 * (10 ** (-5)) * h1_) ** 4.2559)
    t_ += h_
    speed_value1.append(V_)
    height_value1.append(h1_)
    plotnost_value.append(p_)

print('Время, проведённое в полете(с): ', t + t_)
