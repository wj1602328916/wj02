"""
# 1.冒泡排序
li=[55,12,64,-45,68,181]
for i in range(len(li)):
    for j in range(1,len(li)-1):
        if li[j-1]>li[j]:
            li[j-1],li[j]=li[j],li[j-1]
print(li)

# 2.十进制转换为任意进制
li2=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
def jinzhi(number,jz):
    li1=[]
    while True:
        shang=number//jz
        yu=number%jz
        li1.append(yu)
        if shang == 0:
            break
        number=shang
    li1.reverse()
    s=""
    for i in li1:
        s+=str(li2[i])
    print(s)
jinzhi(int(input("请输入要转换的十进制数：")),int(input("请输入要转换的进制：")))

# 3.
score=int(input("请输入成绩："))
if score>=90:
    print("A")
elif score>=60 and score<=89:
    print("B")
else:
    print("C")
"""
# 4.判断一个数是否为素数

num1=int(input("请输入一个大于1的数字:"))
n=2
while num1>n:
    if num1%n==0:
        print("%d不是素数"%num1)
        break
    n+=1
else:
    print("%d是素数"%num1)


# 5.自定义一个异常类，继承Exception类，捕获下面过程，判断input（）输入的字符串长度是否小于5
"""
class Err(Exception):
    def __init__(self,length):
        self.length=length
    def jkh(self):
        return "The input is of length %d,excepting at least 5"%len(st)   #异常信息描述
try:
    st=input("请输入一个字符串:")
    if len(st)<5:
        raise Err(st)     #抛出异常
    else:
        print("print success")
except Err as e:       #捕获异常
    print(e.jkh())
"""


"""
class Erroe(Exception):
    # 初始化方法====创建对象自动调用
    def __init__(self,name):
        self.name = name
    # 去做长度判断的方法
    def pan(self):
        if len(self.name)<5:
            return "您输入的长度<5"
        else:
            return "您输入的长度>5"

s = input("请输入一组字符串")
try:
    raise Erroe(s)
except Erroe as e:
    print(e.pan())
"""

# 6.输入一个数字，把它拆分成所有可能的组合
"""
# num=int(input("请输入一个数字："))
# a=num/2
# print(a)

# num=6
li=[]
for i in range(1,7):
    li.append(i)
print("%d+%d"%(li[0],li[4]))
print("%d+%d"%(li[1],li[3]))
print("%d+%d"%(li[2],li[2]))
"""

