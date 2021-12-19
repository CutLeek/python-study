#列表：根据索引取值
name=['shen','huai','jin']
print(name[0])

#列表值的修改
name[1]='jin'
name[-1]="bing"
print(name)

#列表的索引获取
print("jin这个字符串在列表name中的索引值为{}".format(name.index("jin")))

#列表的删除操作
name.remove("shen")        #删除指定元素
print(name)
name1=name.pop(0)       #根据索引来删除列表中的元素，并且返回删除的值，默认删除最后一个元素

#列表的切片操作
list1=["test1","test2","test2",name,"test5","test6"]
print(list1[3:4])

#列表的添加
list2=[12,23,34,56]
value=input("请输入想输入的值：")
list2.append(value)           #末尾追加，将值追加到列表的末尾
print(list2)

list3=[1,2,3,4]
list2.extend(list3)           #extend通常用来把一个列表添加到另一个列表中，列表的合并也可以用"+"
print(list2)

listtest=[111,222,333,444,555]
listtest.insert(1,777)         #insert是指定位置插入，原本的值依次往后靠
print(listtest)

#练习：产生10个随机数，并保存在列表中
import random
b=[]
for i in range(10):
    a = random.randint(1, 100)
    b.append(a)
print(b)

#统计列表中某个元素在列表中出现的次数
print(b.count(12))

#为列表的中元素进行排序，改变了原列表，b.sort()的返回值是None
b.sort()
print(b)

#将列表进行反转，改变了原列表
b.reverse()
print(b)

#找出列表中的最大值
c=max(b)
print(c)

#找出列表中的最小值
d=min(b)
print(d)

#练习：值班表的排列
zhiban=["zhangsan","lisi",'wangermazi']
for i in range(30):
    name2=zhiban.pop(0)
    zhiban.append(name2)
    print("第{}天的值班顺序是{}".format(i+1,zhiban))

#列表的相关运算符
lista=[1,2,3]
listb=[4,5,6]
listc=lista * 2     #乘法，代表listc中的元素是lista重复了两次
listd=lista+listb   #加法，代表了列表的拼接
print(listd)
print(listc)
