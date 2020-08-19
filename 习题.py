#  第一题
"""
a=["手机", "电脑", "鼠标垫", "游艇" ]
b=input("请输入你想加入的商品：")
a.append(b)
print(a)
c=int(input("请输入序号："))
print(a[c-1])
"""

#  第二题  转换
s="alex"
print(list(s))
print(tuple(s))

li = ["alex", "seven"]
print(tuple(li))
tu = ("Alex", "seven")
print(list(tu))

# 第三题
li=["alex","eric","rain"]
print(len(li))

li.append("seven")
print(li)

li.insert(0,"Tony")
print(li)

li[1]="Kelly"
print(li)

li.pop(2)
print(li)

print(li[1])
del li[1]
print(li)

li.remove("seven")
print(li)

del li[1:5]
print(li)

li=["alex","eric","rain"]
li.reverse()
print(li)

# 第四题
li=["hello","seven",["mon",["h","kelly"],"all",123,446]]
print(li[2][1][1])

# 第五题
print(bool())
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))




