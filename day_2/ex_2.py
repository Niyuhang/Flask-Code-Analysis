# 一个最简单的flask服务
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'


if __name__ == '__main__':
    app.run()

# app是一个Flask的实例
app.run()

#================ 华丽的分割线=====================================================


def wsgi_app(self, environ, start_response):
    """The actual WSGI application.  This is not implemented in
    `__call__` so that middlewares can be applied without losing a
    reference to the class.  So instead of doing this::

        app = MyMiddleware(app)

    It's a better idea to do this instead::

        app.wsgi_app = MyMiddleware(app.wsgi_app)

    Then you still have the original application object around and
    can continue to call methods on it.

    .. versionchanged:: 0.7
       The behavior of the before and after request callbacks was changed
       under error conditions and a new callback was added that will
       always execute at the end of the request, independent on if an
       error occurred or not.  See :ref:`callbacks-and-errors`.

    :param environ: a WSGI environment
    :param start_response: a callable accepting a status code,
                           a list of headers and an optional
                           exception context to start the response
    """
    ctx = self.request_context(environ)
    ctx.push()
    error = None
    try:
        try:
            response = self.full_dispatch_request()
        except Exception as e:
            error = e
            response = self.handle_exception(e)
        return response(environ, start_response)
    finally:
        if self.should_ignore_error(error):
            error = None
        ctx.auto_pop(error)
