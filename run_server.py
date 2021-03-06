import os
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(r"tasklist/projecklist.html")
#        self.write("Hello, world")

def make_app():
    app = tornado.web.Application([
        (r"/", MainHandler),
        ],
        template_path=os.path.join(os.getcwd(),  "templates"),
        static_path=os.path.join(os.getcwd(),  "static"),
        )
    return app

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
