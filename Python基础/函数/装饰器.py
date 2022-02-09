#装饰器
#定义：函数作为参数、要有闭包的特点

def decoratory(func):
    def wrapper(*args,**kwargs):
        print('111111111111111111')
        func(*args,**kwargs)
        print('------2--------------------')

    return wrapper

@decoratory
def house(n):
    print('我是毛坯房')

house(5)

#装饰器带参数，就在外面再套一层
def outer(a):
    def decoratory(func):
        def wrapper(*args,**kwargs):
            print('111111111111111111')
            func(*args,**kwargs)
            print('------{}--------------------'.format(a))

        return wrapper
    return decoratory

@outer(10)
def house(n):
    print('我是毛坯房')

house(5)




