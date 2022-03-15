def func():
    n = 100
    list1 = [1,2,3,4]

    def inner_func():
        for i in list1:
            print(i)
    inner_func()
func()

#-------------------------------------函数的闭包------------------------------------------------
#闭包的特点：1、有内部函数 2、外部函数return内部函数名 3、内部函数引用了外部函数的变量

def func1():
    a = 100
    def inner_func1():
        b=99
        print(a,b)
    return inner_func1
x=func1()
x()
#----------------匿名函数---------------------------------------------------------------------
#格式：lambda 参数1，参数2.....:运算
s = lambda a,b:a+b
print(s(1,2))

#对列表里的奇数进行加1操作,map就是用来对列表里元素进行操作的，不改变源列表，返回列表
list1=[1,2,3,4,5,6,7,8]
result = map(lambda x:x if x % 2 ==0 else x+1,list1)
print(list1)
print(list(result))

#reduce 对列表中的元素进行加减乘除操作，返回操作结果
from functools import reduce
tuple1=(3,5,7,8,9)
result=reduce(lambda x,y:x+y,tuple1)
print(result)

#filter,对列表中的元素进行过滤，不改变原列表
list2=[12,6,8,95,98,34,36,2,8]
result=filter(lambda x:x>10,list2)
print(list(result))

#sorted 排序，重点就是可以指定key
result = sorted(list2)
print(result)

#-------------------------------------------------------递归函数-------------------------------------------------
#特点：我自己调用我自己、





