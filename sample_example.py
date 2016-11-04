# -*- coding: utf-8 -*-

import math
a=1 
b=2
math.log10(10)
print (math.log10(10)+a+b)

# a "r" infront of string make the python read it as a whole
print ('c:\psyhyde\desktop\nudePics')
print (r'c:\psyhyde\desktop\nudePics')

# string is additive and multiplicative 
firstname = "Wei "
lastname = "Luo"
print (firstname + lastname)

#multiply strings
print (firstname*5)

#access individual characters
stringA = "Tuna Mcfish"
print (stringA[0])
print (stringA[-1])

#lenght of a string
print (len(stringA))

#list 
players = (4, 9, 11, 13, 23, 32, 33, 34)
print (players[0])

players2 = players + (5, 8)
print (players2)

#if statement

age = 27
if age <21 :
    print ("no beer for you")
else:
    print ("dont be drunk")
        
    
    
#define a function
def beef():
    print("Dayum, function are lame!")
    
beef()    

#another example function
def CAD_to_YEN(CAD):
    YEN = CAD * 100
    print(YEN)
    
CAD_to_YEN(100)


#return value
def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

my_limit = allowed_dating_age(24)
print("Hyde can date girls", my_limit, "or older")
    

def get_gender(sex = 'Unknown'):
    if sex is 'm':
        sex = 'Male'
    elif sex is 'f':
        sex = 'Female'
    print(sex)

get_gender('m')
get_gender('f')
get_gender()
get_gender('jijij')

a = 7823


def corn():
  print(a)


def fudge():
  print(a)

corn()
fudge()

def dumb_sentence(name='Bucky', action='ate', item='tuna'):
  print(name, action, item)

dumb_sentence()
dumb_sentence("Sally", "farts", "gently")
dumb_sentence(item='awesome')
dumb_sentence(item='awesome', action='is')

#######################################################
groceries = {'cereal', 'milk', 'starcrunch', 'beer', 'duck tape', 'lotion', 'beer'}
print(groceries)

if 'milk' in groceries:
  print("You already have milk hoss!")
else:
  print("Oh yea, you need milk!")
  
#import
import random

x = random.randrange(1, 1000)
print(x)
#################################################

classmates = {'Tony': ' cool but smells', 'Emma': ' sits behind me', 'Lucy': ' asks too many questions'}

for k, v in classmates.items():
    print(k + v)