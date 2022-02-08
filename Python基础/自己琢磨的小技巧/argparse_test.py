#!/usr/bin/python3

import argparse
parser = argparse.ArgumentParser(description="used for test")

#查看版本，可选参数
parser.add_argument('-v','--version',action='version',version='%(prog)s version : v 0.01',help='show the version')
#parser.add_argument('-t','--test',dest='test',help='this is the aa')  #nargs - 指定这个参数后面的value有多少个,+表示至少一个,?表示一个或0个 dest的意思是
#parser.add_argument('-z', choices=['a', 'b', 'd'],type=str,default=c)  #required=True的意思是不能后面什么参数都不跟，至少也要有个-z


#-------------------------------------------子命令的使用方法--------------------------------------
def add(args):
    sum = args.a + args.b
    print(sum)

subparsers = parser.add_subparsers()
#添加子命令 add
parser_a = subparsers.add_parser('add', help='Calculate the sum of two numbers,you can run "python3 %(prog)s add --help" for more information.')
parser_a.add_argument('-a', type=int, help='set the a value')
parser_a.add_argument('-b', type=int, help='set the b value')
#设置默认函数
parser_a.set_defaults(func=add)
#添加子命令 add
parser_b = subparsers.add_parser('adb', help='Calculate the sum of two numbers,you can run "python3 %(prog)s add --help" for more information.')
parser_b.add_argument('-a', type=int, help='set the a value')
parser_b.add_argument('-b', type=int, help='set the b value')
#设置默认函数
parser_b.set_defaults(func=add)



args = parser.parse_args()
args.func(args)













