# 类、对象、属性、方法
# 所有的类名都要求首字母大写，如果是多个单词，采用驼峰式命名
class Phone:
    leibie = 'chuizi'


# 使用类创建对象
SumSang = Phone()
print(SumSang.leibie)


class Student:
    name = 'skda'
    age = 2


zhangSan = Student()
print(zhangSan.age)
zhangSan.high = 183
print(zhangSan.high, '-----------------------------------------')


# 方法(普通方法，类方法，静态方法，魔术方法)
class Student:
    def DoHomeWork(self):  # self就是我的对象
        print(self)
        print(self.pen)


lisi = Student()
print('lisi是：', lisi)
lisi.pen = 'pen'
lisi.DoHomeWork()
print('---------------------------------')


# 构造器和__init__方法
class Student:
    # 魔术方法之一,__init__，用类创建对象的时候，有这个方法，就会把这个方法里面的东西执行一下
    def __init__(self, pen):
        self.pen = pen
        print('----------------------init--------------------')


wangwu = Student('hhhhhhhddddddddd')  # 这个值就是传给__init__了，pen=‘hhhhhdddd’，self.pen=pen,所以wangwu.pen=pen='hhhhhhdddd'
print(wangwu.pen)


# 类方法
class Dog:
    def __init__(self, name):
        self.name = name

    def run(self):  # 这个方法只有对象才能去调用
        print('{}在院子里跑'.format(self.name))

    @classmethod  # 加了装饰器就是类方法
    def test(cls):  # 这个cls就是我的类
        a = cls('aa')
        a.run()


Dog.test()  # 创建对象之前，就可以去调用类方法
d = Dog('大黄')
d.run()
d.test()


# 类的私有变量
class Person:
    __age = 18  # 在变量名前边加__就变成私有变量了，在外面没办法改

    def show(self):
        print(self.__age)

    @classmethod
    def update_age(cls):
        cls.__age += 1
        print('current age is {}'.format(cls.__age))

    @staticmethod  # 加了这个就是静态方法，静态方法也是不依赖对象的，可以直接拿类名去调用
    def test():
        print("I'm staticmethod")


Person.update_age()
Person.test()
