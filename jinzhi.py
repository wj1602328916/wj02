li1=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
def jinzhi(number,jz):
    li2=[]
    while 1:
        shang=number//jz
        yu=number%jz
        li2.append(yu)
        if shang ==0:
            break
        number=shang
    li2.reverse()
    s=" "
    for i in li2:
        # i=li1[i]
        s+=str(li1[i])
    print(s)
jinzhi(int(input("请输入数字：")),int(input("请输入要转化的进制：")))









