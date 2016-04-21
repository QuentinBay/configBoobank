# -*- coding: utf-8 -*-

import getpass
from fileIO import read, write, append

def check_number(value, size):
	if (value.isdigit() and int(value) is not 0 
	   and int(value) <= int(size)):
		return True
	return False

def ask_bank(question, size):
	response = raw_input(question)
	while not check_number(response, size) and response is not 'q':
		print "Erreur: Choix invalide."
		response = raw_input(question)
	return response

def ask_done(question):
	response = raw_input(question)
	while (response is not 'o' and response is not 'O'
		  and response is not 'n' and response is not 'N'):
		print "Erreur: Choix invalide."
		response = raw_input(question)
	return response

def ask_credentials(question):
	response = getpass.getpass(question)
	return response

def ask(question):
	response = raw_input(question)
	return response

def display(text):
	print text

def interact(info, question):
	display(info)
	response = ask(question)
	return response
