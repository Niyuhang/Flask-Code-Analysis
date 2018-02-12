# 规范的WSGI应用


def application(env, start_response):
    '''
    :param env:一个包含所有的http请求的dict
    :param start_response:发送http相应的函数
    :return:
    '''
    print(env["PATH_INFO"])
    start_response('200 OK', [('Content-Type', 'text/html')])
    return b'<h1>hello world<h1>'


# 响应函数要接受两个参数一个是http响应码，一个是HTTP头部，发送响应头
def start_response(http_status, http_head):
    '''
    :param http_status:响应码
    :param http_head: http头部，type:list
    :return:发送响应头
    '''
    pass

# 符合要求的application写好以后，就可以由服务器来调用，其中的env参数和响应函数就会有服务器传入,在server.py中写入我们的服务
