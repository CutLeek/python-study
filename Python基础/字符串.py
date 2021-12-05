s1="abc"
s2="123"

#字符串的拼接
s3=s1+s2
print(s3)
s4=s1 * 2
print(s4)

#in的用法
name = "shenhuaijin"
result1 = 'i' in name
print(result1)
result2 = 'i' not in name
print(result2)

#[]的用法
filename='picture.png'
print(filename[0:-4])

#字符串的逆序    [初始位置：末位置：步长]
print(filename[::-1])

#字符串的大小写
string="this is a sTudy demO"
print(string.capitalize())     #将字符串的第一个字符转换为大写，并将其他的大写转为小写
print(string.title())          #将每个单词的第一个字母转成大写，并将其他的大写转成小写
print(string.upper())          #将所有的字母转成大写
print(string.lower())          #将所有的字母转成小写

#练习，产生一个验证码
code="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789"
s=''
import random
for i in range(4):
    ran = random.randint(0,len(code)-1)
    s +=code[ran]
print(s)
#input=input("请输入验证码：")
#if s.lower()==input.lower():
#    print("验证码正确")
#else:
#    exit(255)

#字符串的查找和替换
s1="http://baidu.com"
print(s1.find('h'))     #find会返回找到的第一个字母的索引位置，如果返回-1，代表没有找到

print(s1.find('p',1,8))   #从指定位置开始找，并指定结束位置

url='http://baidu.com/agb/abas/sadf/asdfd/test.png'
print(url[url.rfind('/')+1:])     #rfind就是从最右边开始找，找到之后，返回第一个的索引位置

s2='hello'
print(s2.replace('l','r',1))      #replace就是替换，找字符串中的l，替换成r，默认全部替换，后面的1代表只替换第一个，写2就代表替换前两个


#字符串的编码和判断开头结尾

"""encode是编码，decode是解码"""
msg='大家好'
result = msg.encode('utf-8')
print(result)
msg = result.decode('utf-8')
print(msg)

"""startswith()判断是否以xxx开头和endswith()判断是否以xxx结尾"""
file_name = "字符串.md"
result=file_name.endswith('md')
print(result)

#字符串判断是否是数字
"""isalpha()表示判断是否字符串都是字母，isdigit()表示判断字符串是否都是数字"""
num='12345412341'
if num.isdigit():
    print("你全是数字啊")

#字符串的拆分与合并
list1=['a','b','c']
print('-'.join(list1))

s='        hello          '
print(s.lstrip())  #去除字符串左侧的空格
print(s.rstrip())  #去除字符串右侧的空格
print(s.strip())   #去除字符串左右两侧的空格


"""split()字符串的拆分"""
s = 'hello world hello cutleek'
result=s.split(' ',1)    #以空格为分隔符，将分割后的结果放在列表中，分割一次
print(result)

"""count()求字符串中指定字符的个数"""
print(s.count('l'))

#练习：如果遇到s2中的字母，就从s1中删除掉
s1="they are student"
s2="aeiou"
for i in s2:
    s1=s1.replace(i,"")
print(s1)

#练习：循环提示用户输入用户名、密码、邮箱，且不能超过20个字符，如果用户输入q，则退出
while True:
    username=input("请输入用户名：")
    password=input("请输入密码：")
    mail=input("请输入邮箱：")
    if "q" ==username or "q"==password or "q"==mail:
        break
    elif len(username) >20 or len(password)>20 or len(mail)>20:
        print("字符串长度不能超过20")
        continue
    else:
        print("")
        break



















