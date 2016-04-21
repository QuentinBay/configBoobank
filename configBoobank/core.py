# -*- coding: utf-8 -*-

import sys
from helpers.fileIO import read, write, append, parse_json
from helpers.console import ask_bank, ask_done, ask_credentials
import helpers.banks as bank


# File containing paths
configFile = "/home/quentin/src/configBoobank/.config"

def switch_to_local_update(sourceFile):
	content = "file:///home/quentin/src/weboob/modules"
	write(sourceFile, content)

def get_user_config():
	backends = []
	done = 'n'
	while done is not 'o' and done is not 'O':
		bank.list_banks()
		chosen_bank = ask_bank("Veuillez selectionner votre banque (q pour quitter) :", len(bank.banks))
		if chosen_bank is 'q':
			break
		login = ask_credentials("Numéro client (caché) :")
		password = ask_credentials("Code secret (caché) :")
		backend = {
			"name" : bank.banks[int(chosen_bank)-1]["module"],
			"website" : "pp",
			"login" : login,
			"password" : password
		}
		backends.append(backend)
		done = ask_done("Avez-vous terminé ? (o/n)")
	return backends


def set_modules(backendFile, modules):
	write(backendFile,"")
	for module in modules:
		content = "["+module['name']+"]\n"
		content += "_module = "+module['name']+"\n"
		content += "website = "+module['website']+"\n"
		content += "login = "+module['login']+"\n"
		content += "password = "+module['password']+"\n\n"
		append(backendFile, content)


def config_backends(backendFile):
	print("Bienvenue sur Weboob !")
	backends = get_user_config()
	set_modules(backendFile, backends)


def main():
	config = parse_json(configFile)
	switch_to_local_update(config['sourcesFile'])
	config_backends(config['backendsFile'])
	
