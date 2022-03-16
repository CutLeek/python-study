stream=open('E:/a.txt','r')

#把全文读出来
continer=stream.read()
print('read',continer)


#判断文件是否可读
continer1=stream.readable()
print(continer1)

#一行一行的读
line = stream.readline()
print(line)

#把每一行读到列表里
lines = stream.readlines()
print(lines)
stream.close()



stream=open('E:/a.txt','w')
#write用来写内容到文件里，但是会覆盖掉原有的内容,writelines可以追加写，但是默认没有换行
stream.write('heiheihei\n')
stream.writelines('hahaha')
stream.close()

#在a模式下， 用write是追加，而不会覆盖
stream=open('E:/a.txt','a')
stream.write('\nxixixi')
stream.close()

#用with open('E:/a.txt','w') as stream：就可以不用每次都close一下了
#--------------------------------------------文件的复制---------------------------------------------
import os
print(os.path.dirname(__file__))

#isabs 判断是否为绝对路径
print(os.path.isabs('test.txt'))

#1.返回操作系统类型值为：posix，是Linux操作系统
print(os.name)
print('Linux' if os.name == 'posix' else 'Windows')

#2.操作系统的详细信息  ，在Linux用的
# info = os.uname()
# print(info)
# print(info.sysname)
# print(info.nodename)

#3.系统的环境变量
print(os.environ)

#4.通过key值获取环境变量对应的value值


#5.判断是否为绝对路径 /tmp/passwd data.txt
print(os.path.isabs('/tmp/passwd3'))
print(os.path.isabs('hello'))

#6.生成绝对路径
print(os.path.abspath('hello.png'))
print(os.path.join('/home/kiosk','hello.png'))
print(os.path.join(os.path.abspath('.'),'hello.png'))    # 三种方法任选其一

#7.获取目录名或文件名
filename = '/home/kiosk/PycharmProjects/20181117/day09/hello.png'
print(os.path.basename(filename))                        # 获取文件名
print(os.path.dirname(filename))                         # 获取目录名

#8.新建目录
os.makedirs('img/file1/file2')  # 递归建立目录
os.mkdir('hello')  		# 建立目录
os.rmdir('hello')   		# 删除目录
# 不能递归删除目录


#9.创建文件 删除文件
os.mknod('ok.txt')
os.remove('ok.txt')

#10.文件重命名（mv）
os.rename('ok.txt','yes.txt')

#11.判断文件或目录是否存在
print(os.path.exists('ips.txt'))

#12.分离后缀名和文件名
print(os.path.splitext('hello.png'))



