# -*- coding: utf-8 -*-
#1
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")

#2 
import sys
print (sys.version_info)
print (sys.version)

#3 display current date&time
import datetime
timenow = datetime.datetime.now()
print (timenow)

import datetime  
nowtime = datetime.datetime.now()  
print ("Current date and time : ")  
print (nowtime.strftime("%Y-%m-%d %H:%M:%S")) 

#4 input
import math
r = float(input("type radius here"))
Area = (math.pi)*r*r
print ("r = ", r)
print ("Area = ", Area)

#######input returns a string (a sequence of characters)
textinput = "jiji\n"
med= textinput*5
print(med)

#6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

sample_data = str([3, 5, 7, 23])
listA = list(sample_data)
tupleA = tuple(sample_data)
print (listA)
print (tupleA)

#7. Write a Python program to accept a filename from the user print the extension of that. 
program_file = input()
extension = str.index(str, beg=(len(program_file)-3) end=len(program_file))