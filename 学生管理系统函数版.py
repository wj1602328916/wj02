
# 定义一个空列表，用来存储所有学生信息
list_info=[]

# 打印菜单
def menu():
    print("-"*30)
    print("1.添加学生信息")
    print("2.修改学生信息")
    print("3.删除学生信息")
    print("4.显示学生信息")
    print("-"*30)
    choice=int(input("请输入要操作的序号："))
    return choice



# 添加学生信息
def add_stu():
    # 定义一个空字典，用来存储单个学生信息
    stu_dict={}
    add_name=input("请输入添加的学生的姓名")
    add_sex=input("请输入添加的学生的性别")
    add_phone=input("请输入添加的学生的电话")
    # 把学生信息添加到字典中
    stu_dict.update(name=add_name,sex=add_sex,phone=add_phone)
    # print(stu_dict)
    # 把字典中中的学生信息放入列表中
    list_info.append(stu_dict)
    print(list_info)



# 删除学生信息
def del_stu():
    # 输入你要删除学生对应的编号
    del_num=int(input("请输入要删除的编号"))-1
    # 通过索引删除所对应的字典，字典中存储的为学生信息，即通过索引删除学生信息
    list_info.pop(del_num)
    print(list_info)

# 显示所有学生信息
def show_stu():
    print("编号\t\t姓名\t\t性别\t\t电话")
    num=1
    # 遍历列表中的所有元素（学生信息）
    for stu in list_info:
        # print("%d  %s  %s  %s"%(num,stu["name"],stu["sex"],stu["phone"]))
        print(num,stu["name"], stu["sex"], stu["phone"])
        num+=1

# 修改学生信息
def amend():
    # 输入你要修改的学生信息所对应的编号
    amend_num = int(input("请输入要修改的编号"))-1
    # 输入新的学生信息
    new_name = input("请输入新的姓名")
    new_sex = input("请输入新的性别")
    new_phone = input("请输入新的电话")
    # 通过key修改value，即修改学生信息
    stu_dict={"name":new_name,"sex":new_sex,"phone":new_phone}
    # 通过索引来截取需要修改的字典
    list_info[amend_num]=stu_dict
    print(list_info)

# 定义一个主函数，用于实现系统循环
def main():
    # 死循环
    while True:
        a=menu()
        if a==1:
            add_stu()
        elif a==2:
            del_stu()
        elif a==4:
            show_stu()
        elif a==3:
            amend()
        elif a==0:
            break
        else:
            print("你输入序号的不能识别")

main()