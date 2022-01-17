def login(username,passswd):
    use="test"
    password=123
    if username==use and password==passswd:
        print("登陆成功")
#username=input("输入用户名：")
#passswd=int(input("输入密码："))
#login(username,passswd)

#---------------------------------------------------可变参数----------------------------------------------------------
def add(*args):
    print(args)
add(1,2,3,4,5,6,7)

#------------------------------------------------关键字参数，key=value-----------------------------------------------
def add1(**kwargs):
    print(kwargs)
add1(a=1,b=2,c=13)


