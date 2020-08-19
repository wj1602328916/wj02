# 1.编写一个名为collatz()的函数,它有一个名为number的参数
#    如果参数是偶数,那么collatz()就打印出number//2
#    如果number是奇数,collatz()就打印3*number+1

# def collatz(number):
#     if number%2==0:
#         print(number//2)
#     else:
#         print(3*number+1)
# collatz(int(input("number:")))

# 2.使用匿名函数对多个数字求和，形参不能给死
a1=lambda *args:sum(args)
print(a1(1,2,3,4,5,6))

# 3、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def a(**kwargs):
    for k,v in kwargs.items():
        if len(v)>2:
            print(k,v[:2])
        else:
            print(k,v)
a(name="北慕仔",age="19",sex="男性吧啦啦")

def a(**kwargs):
    for k,v in kwargs.items():
        if len(v)>2:
            kwargs[k]=v[:2]
    return kwargs

print(a(name="北慕仔",age="19",sex="男性吧"))