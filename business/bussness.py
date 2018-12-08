#coding=utf-8
from business.MysqlHelper import MysqlHelper
from hashlib import sha1
from bottle import route, run, static_file, request,template


def do_register(uname,upwd):
    ret = {'code':'','msg':''}

#注册
# uname=input("请输入用户名：")
# upwd=input("请输入密码：")

    s1 = sha1()
    #初始化sha1对象
    s1.update(upwd.encode('utf-8'))
    #对s1进行更新
    upwd2 = s1.hexdigest()
    #加密

    sql = 'insert into userinfos(uname, upwd) values(%s,%s)'
    #sql语句 这是小写
    params = [uname,upwd2]
    #将插入的值存入列表中

    helper = MysqlHelper()
    #将sql语句以及值传给对象中的方法
    row = helper.insert(sql,params)
    #返回的是受到改变的行
    print (row)
    ret = {'code': '1', 'msg': '注册成功'}
    return ret

#登录
def do_login(uname,upwd):
    # uname = input("请输入用户名：")
    # upwd = input("请输入密码：")

    s1 = sha1()
    s1.update(upwd.encode())
    upwd2 = s1.hexdigest()

    sql = "SELECT upwd from userinfos where uname = %s "
    #大写也可以
    params = [uname]

    helper = MysqlHelper()
    result = helper.fetchone(sql, params)
    message = ''
    if result == None:
        message = '用户名错误'
    elif result[0] == upwd2:
        message = '登录成功'
    else:
        message = '密码错误'
    return message

# do_register('ff','ff1')
