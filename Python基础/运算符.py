#赋值运算符  =

test1=10
test2=20
print("初始的test1是{}，test2是{}".format(test1,test2))

#交换test1和test2的值
test1,test2=test2,test1
print("当前的test1是{},test2是{}".format(test1,test2))
print("-----------------------------------------------")
#算数运算符  + - * / % **
a = 1
b = 2
sum = a+b
jian = b-a
cheng = a*b
chu = a/b
chengfang= a ** b  #a的b次方
zhengchu = a // b
quyu = a % b
print(sum,jian,cheng,chu,chengfang,zhengchu,quyu)
print("---------------------------------------")
#关系运算符  >、<、 >=、 <=、 ==、 !=、 is 、is not
num1 = 20
num2 = 40
if num1 is not num2:
    print(num1)
else:
    print(num2)
print("-----------------------------------------")
#逻辑运算符  and or not  逻辑与、或、非

a1=5
a2=10
if a1 >=10 or a2 >=10:
    print(a2)
if a1 >=10 and a2 >=10:
    print(a2)
print("------------------------------------------")

#位运算符