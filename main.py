# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle3

urls = (
    '/wx', 'Handle',
    '/wx2', 'Handle3',
)

class Handle(object):
    def GET(self):
        return "hello, this is a test"

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
