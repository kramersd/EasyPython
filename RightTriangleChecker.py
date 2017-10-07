#Author: Shane Kramer
#Date: 10/5/2017
#Descpt: Right Triangle Checker
#        Enter three integers into, one per each side, and this program will
#        check to see if it is a valid right triangle. It utilizes Pythagoras'
#        Theorem a^2 + b^2 = c^2

from math import pow

print("Enter three integers:" )
a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))

print("Your three side are " + str(a) + " " + str(b) + " " + str(c));
if((pow(a,2) + pow(b,2)) == pow(c,2)):
    print("These sides *do* make a right triangle. Yippy-skippy!")
else:
    print("N0! These sides do not make a right triangle!")
