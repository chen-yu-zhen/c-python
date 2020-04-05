stu_list = list()
def func():
    print('-' * 6 + '功能选项' + '-' * 6)
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员')
    print('4.查询学员信息')
    print('5.显示所有学员')
    print('6.退出系统')
    print('-' * 20)
def add_stu():
    ''' 添加函数'''
    # 输入新生信息（姓名，学号，性别）
    new_name = input('请输入新生的姓名：')
    new_num = input('请输入新生的学号：')
    new_gender = input('请输入新生的性别（男/1，女/0）：')
    # 检查是否已存在该名字
    for i in stu_list:
        if new_name == i['姓名']:
            print('该名字已存在')
            return
    # 创建新字典给新生
    new_stu = dict()
    new_stu['姓名'] = new_name
    new_stu['学号'] = new_num
    new_stu['性别'] = new_gender
    # 添加新生
    stu_list.append(new_stu)
def del_stu():
    # 输入删除的名字
    name = input('请输入删除的名字:')
    # 检查是否有这个名字
    for i in stu_list:
        if name == i['姓名']:
            stu_list.remove(i)
        else:
            print('该名字不存在')
def change_stu():
    # 输入需要替换的信息
    print('''
1.修改姓名
2.修改学号
3.修改性别
4.修改全部信息''')
    # 让用户选择
    user_chose = int(input('请输入你需要修改的内容：'))
    if user_chose == 1:
        name = input('请输入原来的名字：')
        for i in stu_list:
            if name ==i['姓名']:
                i['姓名']=input('请输入修改的名字：')
                print('修改完成')
            else :
                print('查无此人')
    elif user_chose == 2:
        name = input('请输入名字：')
        for i in stu_list:
            if name == i['姓名']:
                i['学号'] = input('请输入修改的学号：')
                print('修改完成')
            else :
                print('查无此人')
    elif user_chose == 3:
        name = input('请输入名字：')
        for i in stu_list:
            if name == i['姓名']:
                i['性别'] = input('请输入修改的性别（男/1，女/0）：')
                print('修改完成')
            else :
                print('查无此人')
    elif user_chose == 4:
        name = input('请输入名字：')
        for i in stu_list:
            if name == i['姓名']:
                i['姓名'] = input('请输入修改的名字：')
                i['学号'] = input('请输入修改的学号：')
                i['性别'] = input('请输入修改的性别（男/1，女/0）：')
                print('修改完成')
            else :
                print('查无此人')
def find_stu():
    name=input('请输入想要查找的名字：')
    for i in stu_list:
        if name==i['姓名']:
            print(i)
        else:
            print('查无此人')
while True:
    # 功能选项
    func()
    # 用户选择功能选项
    user_chose=int(input('请输入你要的功能：'))
    # 按用户需求打开功能选项
    if user_chose == 1:
        add_stu()
    elif user_chose == 2:
        del_stu()
    elif user_chose == 3:
        change_stu()
    elif user_chose == 4:
        find_stu()
    elif user_chose == 5:
        print(stu_list)
    elif user_chose == 6:
        exit()
    else:
        print('请输入正确的选项')
