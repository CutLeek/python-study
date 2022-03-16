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


