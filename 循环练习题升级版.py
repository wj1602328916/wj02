"""
example2 = [[1,2,3],[4,5,6],[7,8,9],[10]]
example3 = [j**2 for i in example2 for j in i if j%2 == 0]
print(example3)
"""

# example2 = [[1,2,3],[4,5,6],[7,8,9],[10]]
# for i in example2:
#     for j in i:
#         if j%2 ==0:
#             j=j**2
#             print(j,end=" ")

# 一、输入一个人名，如果字典中有这个人输出人名对应的城市。
"""
a=input("请输入人名")
places={'张三':['上海','广州','深圳'],'李四':['九寨沟','张家界','张++']}
for k,v in places.items():
    if a==k:
        print(v)
"""
"""
name=input("请输入人名")
places={'张三':['上海','广州','深圳'],'李四':['九寨沟','张家界','张++']}
if name in places:
    print(places.get(name))
"""

"""
# 二、求阶乘：
a=int(input("num:"))
b=1
for i in range(1,a+1):
    b=b*i
print("%d的阶乘为%d"%(a,b))
"""

"""
# 三、从键盘输入一个字符串，将小写字母都转换成大写字母，将字符串以列表的形式输出：
a=input("str:")
l=[]
for i in a:
    if a.isdigit()==True:
        l.append(i)
        print(i)
    else:
        l.append(i.upper())
print(l)
"""
"""
# for i in 123:
#     print(i)

for i in "gjhj":
    print(i)

for i in ["gjhj",1,5,-6.6]:
    print(i)

for i in (12,"hghj",42):
    print(i)

for i in {"l":"jgbn","ug":123}:
    print(i)

for i in {"l",24,-10,"nki"}:
    print(i)
"""

# 随机输入一个八位以内的整数，求它是几位数，然后逆序打印其他数字
"""
a=input("请输入数字")
print(len(a))
print(a[::-1])
"""

"""
num=input("请输入数字")
a=list(num)
for i in range(1,len(a)+1):
    if len(a)<=8:
        a.reverse()
        print(a)
        break
else:
    print("请输入8位以内的数字")
"""


#  五、猜年龄游戏
# 1.允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
# 2.猜的数字给定要求：1----18之间的整数

"""
import random
a=random.randint(1,18)
print(a)
for i in range(3):
    guss=int(input("age:"))
    if guss == a:
        print("恭喜你猜对了")
        break
else:
    print("game over")
"""

"""
import random
a=random.randint(1,18)
print(a)
alo="y"
while alo =='y':
    for i in range(3):
        guss=int(input("age:"))
        if guss == a:
            print("恭喜你猜对了")
            break
else:
    alo = input('是否继续玩y/n？')
"""

"""
import random
rand = random.randint(1,18)
print(rand)
now = 'y'
while now =='y' or now =='Y' :
    for i in range(3):
        a = int(input('请输入要猜的年龄：'))
        if a==rand :
            print('猜对了')
            rand = random.randint(1, 18)
            break
        elif a<rand :
            print('猜小了')
        elif a>rand :
            print('猜大了')
    now=input('是否继续玩y/n？')
"""


#  等腰三角形
# 方法1
#  行号
for i in range(4):
    #  空格数
    for j in range(3-i):
        print(" ",end=" ")
    #  **数
    for k in range(2*i+1):
        print("*",end=" ")
    # 每打印一次换行
    print()
# 方法2
for i in range(4):
    print(("*"*(2*i+1)).center(7))

#  行号
for i in range(4):
    #  **数
    for j in range(4):
        print("*",end=" ")
    print()

#  直角三角形
for i in range(5):
    for j in range(i):
        print("*",end=" ")
    print()


#  冒泡
list01 = [5,65,41,1,32,8,9,89,670]
for i in range(len(list01)):
   for j in range(1,len(list01)):
      if list01[j]>list01[j-1]:
         list01[j],list01[j-1]=list01[j-1],list01[j]
print(list01)


for i in range(1,6):
    print(i)
    for j in range(i):
        print(j,end=" ")
