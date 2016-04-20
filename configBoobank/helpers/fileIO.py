# -*- coding: utf-8 -*-

import json

def write(filePath, content):
	with open(filePath, 'wb') as file:
		file.write(content)

def read(filePath):
	with open(filePath, 'rb') as file:
		file_text = file.read()
	return file_text

def append(filePath, content):
	with open(filePath, 'ab') as file:
		file.write(content)

def parse_json(filePath):
	with open(filePath, 'rU') as file:
		data = json.load(file)
	return data

