#!/usr/bin/python3

import  configparser
 
config = configparser.ConfigParser()
file = 'config.ini'
config.read(file)
username = config.get('login','username')
password = config.get('login','password')
print(username,password)
