import os
import xlrd
import shutil

lis = []

def ly():
    # 打开 name_list.xlsx表
    xls = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\name_list.xlsx")
    sheet = xls.sheet_by_name("NAME")

    # 用for循环获取该表第一列的值
    for i in sheet.col_values(0)[1:]:
        lis.append(int(i))
    return lis


li1 = []
li2 = []
def lly():
    # 获取文件夹“000_PCAP”中所有文件名称
    dirlist = os.listdir(r"C:\Users\Administrator\Desktop\2000_PCAP\\")

    for name in dirlist:
        # 所获取的所有文件名的前缀放到列表li1中
        li1.append(name[:name.rfind(".")])
        hzm = name[name.rfind("."):]
        li2.append(hzm)
    return li1,li2

def llye():
    source_path = r"C:\Users\Administrator\Desktop\2000_PCAP"  # 源文件目录
    target_path = r"C:\Users\Administrator\Desktop\2000_PCAP_part1"  # 目标目录

    for old_name in lis:
        for names in li1:
            if str(old_name) == names:
                # print(source_path + "\\" + old_name + ".docx")
                return shutil.copy(source_path + "\\" + str(old_name) + ".docx", target_path)

if __name__ == '__main__':
    print(ly())
    print(lly())
    print(llye())