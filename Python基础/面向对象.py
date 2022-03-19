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
    def DoHomeWork(self):
        print(self)
        print(self.pen)


lisi = Student()
print(lisi)
lisi.pen = 'pen'
lisi.DoHomeWork()


# 构造器和__init__方法
class Student:
    # 魔术方法之一,__init__，用类创建对象的时候，有这个方法，就会把这个方法里面的东西执行一下
    def __init__(self, pen):
        self.pen = pen
        print('----------------------init--------------------')


wangwu = Student('hhhhhhhddddddddd')


