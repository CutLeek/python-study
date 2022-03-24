# 私有化
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__socre = 59  # 这个__socre就是私有变量，外界是没有办法修改的

    def setSocre(self, socre):
        self.__socre = socre

    def __str__(self):
        return '姓名：{} 年龄：{} 分数：{}'.format(self.name, self.age, self.__socre)


zhangsan = Student('zhangsan', 16)
print(zhangsan)

zhangsan.setSocre(98)
print(zhangsan)


# 继承
print('-----------------------------------------我是继承分割线------------------------------------------------')
class Book:
    def __init__(self, bname, author, number):
        self.bname = bname
        self.author = author
        self.number = number

class Student:
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        self.book = book
        self.books=[]
        self.books.append(book)



class compouter:
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def online(self):
        print("正在使用电脑上网")

dell = compouter('dell','ele','puple')

shenmu= Book('神墓','辰南',100)

lisi = Student('lisi',dell.brand,shenmu.bname)