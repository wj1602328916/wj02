l=[0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
def jinzhi(number,jz):
    li=[]
    while True:
        shang=number//jz
        yu=number%jz
        li.append(yu)
        if shang == 0:
            break
        number=shang
    li.reverse()
    s=""
    for i in li:
        s+=str(l[i])
    print(s)

jinzhi(int(input("请输入要转换的数字：")),int(input("请输入要转换的进制：")))

"""
l=[0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
li=[]
number=1500
jz=16
while True:
    shang=number//jz
    yu=number%jz
    li.append(yu)
    if shang == 0:
        break
    number=shang
li.reverse()
s=""
for i in li:
    s+=str(l[i])
print(s)
"""