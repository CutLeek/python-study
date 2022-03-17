# 一边循环一边计算的机制，称为生成器

# 1、通过列表推导式得到生成器
newlist = (x * 3 for x in range(10))
print(type(newlist))

# 调用生成器自带的方法，调用一次，给我生成一个
print(newlist.__next__())

# 利用系统 自带的next方法
print(next(newlist))


# 如果调用次数超过len(newlist)，那么就会抛出异常

# 利用函数定义生成器
def func():
    n = 0
    while True:
        n += 1
        yield n


x = func()
print(x)


# 进程--线程--协程
def task1(n):
    for i in range(n):
        print(i)
        yield None


def task2(n):
    for i in range(n):
        print(i)
        yield None


g1 = task1(10)
g2 = task1(5)
while True:
    try:
        next(g1)
        next(g2)
    except Exception as e:
        break
