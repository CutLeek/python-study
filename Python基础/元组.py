#元组：元组的符号是()，元组中的元素不可修改，不支持增删改
tuple1=(1,2,3,3)
print(tuple1,type(tuple1))
print(tuple1.count(3))    #统计元组中，元素3出现的次数
print("元素3的索引是：",tuple1.index(3))

#元组拆包
tuple2=(1,2,3,4,56,7,89,0)
a,b,*c=tuple2
print(a,b,c)
print(*c)

#拆，狠狠的拆
test='asdklfjakfja'
print(*test)
print(tuple(sorted(tuple2)))