from pymysql import *

class Students():

    # 定义两个类属性
    conn=connect(user="root", password="malong1", port=3306, host="localhost", database="jian", charset="utf8")
    cur=conn.cursor()

    @staticmethod
    def menu():
        print("*" * 40)
        print("1.查看所有学生信息")
        print("2.插入数据")
        print("3.删除学生")
        print("4.查看班级对应哪些学生")
        print("5.退出")
        print("*" * 40)
        a = int(input("请输入操作的序号"))
        return a



    def add_student(self):
        add_name = input("请输入学生姓名")
        add_age = input("请输入学生年龄")
        add_height = input("请输入学生身高")
        add_gender = input("请输入学生性别")
        add_cls_name = input("请输入学生所在班级")

        sql = """
        insert into students(name ,age,height,gender,cls_name) values(%s,%s,%s,%s,%s)
        """


        try:
            self.cur.execute(sql,(add_name,add_age,add_height,add_gender,add_cls_name))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.roolback()


    # 查询所有信息
    def show_student(self):

        sql="""select * from students"""

        try:
            self.cur.execute(sql)
            mll=self.cur.fetchall()
            print("序号  姓名  年龄  身高  性别  班级")
            for i in mll:
                print(i[0],i[1],i[2],i[3],i[4],i[5])
        except Exception as e:
            print(e)
            self.conn.rollback()

    def del_student(self):
        id=int(input("请输入你要删除的编号"))
        sql="""delete from students where id=%s"""

        try:
            self.cur.execute(sql,id)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def inquire_student(self):
        cls_name = input("请输入你要查寻的班级")
        sql = """select name from students where cls_name=%s"""

        try:
            self.cur.execute(sql,cls_name)
            mm=self.cur.fetchall()
            if mm:
                print(mm)
        except Exception as e:
            print(e)
            self.conn.rollback()

class Main():
    while True:
        s = Students()
        b=s.menu()
        if b==2:
            s.add_student()
        if b==1:
            s.show_student()
        if b==3:
            s.del_student()
        if b==4:
            s.inquire_student()
        elif b==0:
            s.cur.close()
            s.conn.close()
            break



if __name__ == '__main__':
    Main()


