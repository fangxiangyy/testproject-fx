# #!/usr/bin/env python
# # #coding:utf-8
# #
# # import socket
# #
# # def handle_request(client):
# #     #接收请求
# #     buf = client.recv(1024)
# #     #返回信息
# #     client.send("HTTP/1.1 200 OK\r\n\r\n")
# #     client.send("Hello, Tim")
# #
# # def main():
# #     #创建sock对象
# #     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #     #监听80端口
# #     sock.bind(('localhost',8000))
# #     #最大允许排队的客户端
# #     sock.listen(5)
# #
# #     #循环
# #     while True:
# #         #等待用户的连接,默认accept阻塞当有请求的时候往下执行
# #         connection, address = sock.accept()
# #         #把连接交给handle_request函数
# #         handle_request(connection)
# #         #关闭连接
# #         connection.close()
# #
# # if __name__ == '__main__':
# #     main()

from bottle import route,run,static_file,request,template

from business.bussness import do_register, do_login


@route('/hello/<name>')
def op(name = 'world'):
    return '<strong>Hello {}'.format(name)

@route('/<path>' )
def html(path):
    return static_file(path,root='../register/')

@route('/login1', method="POST")
def testlogin():
    uname=request.forms.get('username')
    upwd=request.forms.get('password')
    mess = do_login(uname, upwd)
    # return "{}:{}".format(uname, upwd)
    return template("<p>login name is :{{username}} and password is :{{password}} result is: {{message}}</p>", username=uname,
                    password=upwd,message=mess)

@route('/regist1', method="POST")
def test():
    uname=request.forms.get('username')
    upwd=request.forms.get('password')
    rer = do_register(uname, upwd)
    # return "{}:{}".format(uname, upwd)
    # return template("<p>regist name is :{{username}} and password is :{{password}}</p>", username=uname,
        #                 password=upwd,)
    return ({'username':uname,'password':upwd,'rer':rer} )

run(host='localhost',port=8088)






