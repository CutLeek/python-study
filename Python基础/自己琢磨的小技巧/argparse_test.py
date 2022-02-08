#!/usr/bin/python3

import argparse
parser = argparse.ArgumentParser(description="used for test")

#查看版本，可选参数

parser.add_argument('-v','--version',action='version',version='%(prog)s version : v 0.01',help='show the version')

args = parser.parse_args()

















