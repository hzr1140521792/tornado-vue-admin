#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Copyright (c) 1997-2022 YMT.com, Inc. All Rights Reserved
@author: hanzhengrong (hanzhengrong@ymt360.com)
@create: 2022/2/18 10:35 AM
@brief: 入口
"""

import tornado.ioloop
import tornado.web
import os


settings = {
    "web_path": os.path.join(os.path.dirname(__file__), "web/dist/assets/"),
}


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("web/dist/index.html")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/assets/(.*)$", tornado.web.StaticFileHandler, dict(path=settings['web_path']))
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
