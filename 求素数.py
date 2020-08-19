# 1.求100以内的素数
# for i in range(2,100):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=" ")

# 2.map（）函数：它接收一个函数f和一个序列，并通过函数f依次作用在序列的每个元素上，得到一个新的list返回。map(函数名，序列）
# 给（1,2,3,4,5,6,7,8,9）每个元素都作平方
def f(x):
    return x*x
li=list(map(f,(1,2,3,4,5,6,7,8,9)))
print(li)

# filter（）函数   filter（函数名，序列），过滤序列，过滤掉不符合条件的元素，返回符合条件的元素组成的新列表。注意:要嵌套在list里面
a=[1,2,3,4,5,6,7,8,9]
def fun(a):
    return a%2 == 1
new_a=list(filter(fun,a))
print(new_a)



