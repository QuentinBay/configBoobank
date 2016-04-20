# -*- coding: utf-8 -*-

banks = [
	{"module" : "americanexpress", "name" : "American Express"},
	{"module" : "apivie", "name" : "Apivie"},
	{"module" : "axabanque", "name" : "AXA Banque"},
	{"module" : "banqueaccord", "name" : "Banque Accord"},
	{"module" : "creditdunord", "name" : "Banque Courtois"},
	{"module" : "creditdunord", "name" : "Banque Kolb"},
	{"module" : "banquepopulaire", "name" : "Banque Populaire"},
	{"module" : "bp", "name" : "Banque postale"},
	{"module" : "creditdunord", "name" : "Banque Tarneaud"},
	{"module" : "barclays", "name" : "Barclays"},
	{"module" : "bforbank", "name" : "BforBank"},
	{"module" : "bnporc", "name" : "BNP Paribas"},
	{"module" : "s2e", "name" : "BNP Paribas Epargne & Retraite Entreprises"},
	{"module" : "boursorama", "name" : "Boursorama Banque"},
	{"module" : "bred", "name" : "BRED Banque Populaire"},
	{"module" : "caissedepargne", "name" : "Caisse d'Epargne"},
	{"module" : "s2e", "name" : "Cape@si"},
	{"module" : "carrefourbanque", "name" : "Carrefour Banque"},
	{"module" : "cic", "name" : "CIC"},
	{"module" : "citelis", "name" : "Citélis"},
	{"module" : "citibank", "name" : "Citibank"},
	{"module" : "cragr", "name" : "Crédit Agricole"},
	{"module" : "creditcooperatif", "name" : "Crédit Coopératif"},
	{"module" : "creditdunord", "name" : "Crédit du Nord"},
	{"module" : "creditmutuel", "name" : "Crédit Mutuel"},
	{"module" : "cmb", "name" : "Crédit Mutuel de Bretagne"},
	{"module" : "cmso", "name" : "Crédit Mutuel du Sud-Ouest"},
	{"module" : "delubac", "name" : "Banque Delubac & Cie"},
	{"module" : "s2e", "name" : "ESALIA"},
	{"module" : "fortuneo", "name" : "Fortunéo"},
	{"module" : "ganassurances", "name" : "Groupama"},
	{"module" : "groupamaes", "name" : "Groupama Epargne Salariale"},
	{"module" : "hsbc", "name" : "HSBC France"},
	{"module" : "s2e", "name" : "HSBC Epargne & Retraite en Entreprise"},
	{"module" : "ing", "name" : "ING Direct"},
	{"module" : "kiwibank", "name" : "Kiwibank"},
	{"module" : "lcl", "name" : "LCL"},
	{"module" : "oney", "name" : "Oney"},
	{"module" : "paypal", "name" : "PayPal"},
	{"module" : "societegenerale", "name" : "Société Générale"},
	{"module" : "creditdunord", "name" : "Société Marseillaise de Crédit"},
	{"module" : "vicseccard", "name" : "Victoria's Secret Angel Card"},
	{"module" : "wellsfargo", "name" : "Wells Fargo"},
]

def display_bank():
	pass

def list_banks():
	id = 1
	for bank in banks:
		print id,") => ",bank["name"]
		id += 1

