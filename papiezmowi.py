#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys
import random
import os

def lettersCount(words):
	return len(words)

def drukujPapsona(co, lenght):	
	papaj_station = os.get_terminal_size().columns
	dymek = papaj_station if lenght + 2 > papaj_station  else lenght +2
	#spaghetti code aka kremowka code
	print ("██" * dymek)
	print  ("█ " + co)
	print ("██" * dymek)
	print ("░░███░░░░░░░░░░░░░░░░")
	print ("░░░███░░░░░░░▄▄▀▀▀▀▀▀▄▄")
	print ("░░░░███░░░▄▄▀▄▄▄█████▄▄▀▄")
	print ("░░░░░██▄█▀▒▀▀▀█████████▄█▄")
	print ("░░░░░█▄██▒▒▒▒▒▒▒▒▀▒▀▒▀▄▒▀▒▀▄")
	print ("░░░░▄██▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▄")
	print ("░░░░██▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▌")
	print ("░░░▐██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐█")
	print ("░▄▄███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█")
	print ("▐▒▄▀██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▌")
	print ("▌▒▒▌▒▀▒▒▒▒▒▒▄▀▀▄▄▒▒▒▒▒▒▒▒▒▒▒▒█▌")
	print ("▐▒▀▒▌▒▒▒▒▒▒▒▄▄▄▄▒▒▒▒▒▒▒▀▀▀▀▄▒▐")
	print ("░█▒▒▌▒▒▒▒▒▒▒▒▀▀▒▀▒▒▐▒▄▀██▀▒▒▒▌")
	print ("░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒▒▒█")
	print ("░░░▀▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▒▒▒▒▒▒▄▀")
	print ("░░░▐▒▒▒▒▒▒▒▒▒▄▀▐▒▒▒▒▒▐▒▒▒▒▄▀")
	print ("░░▄▌▒▒▒▒▒▒▒▄▀▒▒▒▀▄▄▒▒▒▌▒▒▒▐▀▀▀▄▄▄")
	print ("▄▀░▀▄▒▒▒▒▒▒▒▒▀▀▄▄▄▒▄▄▀▌▒▒▒▌░░░░░░")
	print ("▐▌░░░▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▀░░░░░░░")
	print ("░█░░░░░▀▄▄▒▒▒▒▒▒▒▒▒▒▒▒▄▀░█░░░░░░░")
	print ("░░█░░░░░░░▀▄▄▄▒▒▒▒▒▒▄▀░░░░█░░░░░░")

args = ' '.join(sys.argv[1:])

if lettersCount(args) == 0:
	slownikPapsona = ['coo', 'jeszcze jak', 'z warkoczykami albo bez warkoczyków', 'ja nie wiem bo mi nie dali nigdy', 'jak mi dadzą to zjem', 'a po maturze chodziliśmy na kremówki']
	papajmowi = random.choice(slownikPapsona)
	drukujPapsona(papajmowi, lettersCount(papajmowi))
else:
	drukujPapsona(args, lettersCount(args))
