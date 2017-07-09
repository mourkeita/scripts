#! /usr/bin/python
# coding: utf-8

"""Ce jeu consiste à deviner quel nombre
 entre 1 et 100 a choisi le système.
 Pour quiiter tapez 'q'
"""
import random
from random import randint

print "System is choosing..."
number = random.randint(1,100)
choice = raw_input("Give a number : ")
ret = 1
while (choice != number):
	if choice == 'q':
		break
	if int(choice) > number:
		choice = raw_input("Give a smaller number : ")
		ret+=1
		print choice, type(choice)
	elif int(choice) < number:
		choice = raw_input("Give a greater number : ")
		ret+=1		
		print choice, type(choice)
	elif int(choice) == number:
		print "You win with %d retry!" % ret 
		break

print "Bye !"