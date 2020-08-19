#1、使用while循环和for循环,求1～100之间所有偶数之和(至少一种方法)
#  方法1
s=0
i=0
while i<=100:
    s+=i
    i+=2
print(s)

#  方法2
n=0
s = 0
while n <=100:
        n+=1
        if n%2==0:
            s+=n
print(s)

#  方法3
s1=0
for i in range(0,101,2):
    s1+=i
print(s1)


#  方法4
s=0
for n in range(1,101):
    if n%2==0:
        s+=n
print(s)



# 2、 使用while循环和for循环输出1 2 3 4 5 6     8 9 10(至少一种方法)
#  方法1
for a in range(1,11):
    if a==7:
        print("",end=" ")
        continue
    else:
        print(a,end=" ")

#  方法2
for a in range(1,11):
    if a==7:
        continue
    print(a,end=" ")

# 方法2
a = 0
while a<10:
        a+=1
        if a==7:
            continue
        print(a)

# 3、使用for循环,求1-100的所有数的和
s=0
for b in range(0,101):
    s+=b
print(s)

# 4、输入1到100之间的偶数:
#  方法1
for a in range(0,101,2):
    print(a,end=" ")

#  方法2
for a in range(0,101,2):
    print(a)

#  方法3
for a in range(101):
    if a%2==0:
        print(a)

#  5、用户登陆（三次机会重试），用户名为: abc；密码为123
for i in range(3) :
        a=input("账号:")
        b=input("密码:")
        if a == 'abc' and b=='123' :
                print('登陆成功！')
                break
        else:
                print('账号或密码错误！')


# 六、有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
count = 0
for i in range(1,5):
        for j in range(1,5):
                for k in range(1,5):
                        if( i != k ) and (i != j) and (j != k):
                                print(i,j,k)
                                count += 1
print("总共有%d个"%count)

# 七、输入三个整数x,y,z，请把这三个数由小到大输出。
# 方法1
a=int(input("x"))
b=int(input("y"))
c=int(input("z"))
d=[a,b,c]
d.sort()
print(d)

#  方法2
list1 = []
for i in range(3):
        num = int(input("请输入3个整数"))
        list1.append(num)
list1.sort()
print(list1)

# 八、将一个列表的数据复制到另一个列表中。使用两种方法
# 列表如下所示list1 = [11,22,33,44]
list1 = [11,22,33,44]
list2 = [55,66]
print(list1+list2)

list1.extend(list2)
print(list1)

# 方法1：
list1 = [11,22,33,44]
b=list1[:]
print(b)

# 方法2:
list1 = [11,22,33,44]
b = list1.copy()
print(b)

# 9、按相反的顺序输出列表的值。a = ['one', 'two', 'three']
a = ['one', 'two', 'three']
a.reverse()
print(a)

# 10、有如下值集合[11,22,33,44,55,66,77,88,99,90], 将所有大于66的值保存至字典的第一个key中，将小于66值保存至第二个key的值中。
li = [11,22,33,44,55,66,77,88,99,90]
dic = {}
n = []
m = []
for i in li:
        if i > 66:
                n.append(i)
        if i < 66:
                m.append(i)
dic.update(k1 = m, k2 = n)
print(dic)

# 十一、一行代码实现两个变量进行交换
a = 10
b = 20
a,b=b,a
print(a,b)







