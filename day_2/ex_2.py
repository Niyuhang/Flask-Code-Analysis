# 一个最简单的flask服务
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'


if __name__ == '__main__':
    app.run()

# app继承Flask类
# app.run()实际上
