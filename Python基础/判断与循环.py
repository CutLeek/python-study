import random

c = random.randint(1,10)
print("c的值是{}".format(c))
d = random.randrange(0,100,20)
print("d的值是{}".format(d),type(d))


#if判断
a = 3
b = 20
if a > 5:
    print(a)
else:
    print(b)


#for循环
#range左闭右开的区间,range(1,10)代表1到9，range(10)代表0到9
for i in range(1,10):
    c = random.randint(1, 10)
    print(i,c)


#while循环
i = 0
while i <=10:
    print(i)
    i +=1

"""打印1-30之间所有的3的倍数且是5的倍数"""
i=1
while i<=30:
    if i%3==0 and i%5==0:
        print(i)
    i+=1


"""使用while循环计算1-20的所有数的和"""
i=1
sum=0
while i<=20:
    sum +=i
    i+=1
print(sum)

#嵌套循环












