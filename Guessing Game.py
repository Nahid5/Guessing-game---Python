'''
Learning python, making a guessing game

Learned you need to cast when taking input, inputs seems to be taken in as string
'''
import random

random.seed()
randNum = random.randrange(11)      #integer from 0 to 10
name = input("What is your name?")
name = name.lstrip()        #remove leading spaces
name = name.rstrip()        #remove trailing spaces
print ("Hello " + name + " welcome to the guessing game.")
guess = int(input("Please enter a number"))

while guess != randNum:
    guess = int(input ("That was not the correct number, try again"))
print ("Congrats, your number " + str(guess) + " matches the random number which is " + str(randNum))