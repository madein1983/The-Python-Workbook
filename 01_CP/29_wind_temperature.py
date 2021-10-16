# определение коэффициента охлаждения ветров
# Ta - temperature in celsium, V - velocity of wind kmph
#  используется обычно для температур меньше 10 по целсию и скорости ветра более 4,8 км/час
#import math
Ta = float(input("Enter the temperature in celsium: "))
V = float(input("Enter the speed of wind in kmph:"))
W_OFFSET = 13.12
W_FACTOR1 = 0.62
W_FACTOR2 = -11.37
W_FACTOR3 = 0.3965
W_EXPONENT = 0.16
WCI = W_OFFSET + W_FACTOR1*Ta + W_FACTOR2*V**W_EXPONENT + W_FACTOR3*Ta*V**W_EXPONENT
print(round(WCI))


#1 км/час = 0.277778 м/с
#1 м/с = 3.6 км/ч