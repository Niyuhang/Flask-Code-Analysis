# python自带的简易服务器
from wsgiref.simple_server import make_server
from day_1.ex_1 import application

# 创建服务器，加入处理函数
http_server = make_server('', 8000, application)

if __name__ == '__main__':
    print("server start in port 8000")
    http_server.serve_forever()