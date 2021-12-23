#字典使用的符号是{}，元素以键值对的形式存在
dict1={'ken':123,'de':345,'ji':562}

#字典增加元素
dict1['li']=137
print(dict1)

#字典修改元素
dict1['li']=138
print(dict1)

#查
#直接遍历取到的是字典的key,再根据key去取到value
for i in dict1:
    print(i,dict1.get(i))
print(dict1['ken'])            #这样也可以根据key拿到Value
print(dict1.get('abc',90))      #调用get函数的时候，可以传一个默认值，取不到就返回这个默认值

print(dict1.items())           #取出来的结果是列表套元组

print(dict1.values())           #这样搞取出来的是所有的值

#字典的删除操作
#dict1.clear()                    #通过clear函数，字典就被清空了
#print(dict1)

result1=dict1.pop('ken')           #这样删除的话，就是把key和value都删掉了，result1拿到的是value的值
print(result1,dict1)

result2=dict1.popitem()            #默认删除最后一个元素，result2拿到的是元组，被删掉的键值对组成的元组
print(result2,dict1)

#字典的其他内置函数
dict2={1:2}
dict3={3:4,1:5}
dict2.update(dict3)        #update就是两个字典相加
print(dict2)












