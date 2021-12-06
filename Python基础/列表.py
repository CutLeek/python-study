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
del name[2]
print(name)









