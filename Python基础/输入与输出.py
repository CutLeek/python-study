#变量的赋值
test1=10
test2=20

#交换test1和test2的值
test1,test2=test2,test1
print(test1,test2)

#print输出普通字符串
print("hello world")

#print输出变量
a=30
print(a)

#print中的三引号，完美还原原来的格式
print("""
this is the first line
this is the "second" line
""")


#格式化的输出
print("变量a的值是:%s,变量test1的值是:%s" % (a,test1))
print("{}比9大".format(a))
print("{1}比1大，{0}比20小".format(test1,test2))

#读取键盘的输入
ToEat=input("今晚吃什么：")
print(ToEat)
