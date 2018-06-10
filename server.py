import json
import os
import traceback
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options
import tornado.escape
from tornado.websocket import WebSocketHandler

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("angelhack-123-firebase-adminsdk-8z2vi-44c0b91d8a.json")
firebase_admin.initialize_app(cred)


db = firestore.client()
define("port", default=8080, help="runs on the given port", type=int)

cl=[]

class MyAppException(tornado.web.HTTPError):
    pass


class BaseHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        self.set_header('Content-Type', 'application/json')
        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            # in debug mode, try to send a traceback
            lines = []
            for line in traceback.format_exception(*kwargs["exc_info"]):
                lines.append(line)
            self.write(json.dumps({
                'status_code': status_code,
                'message': self._reason,
                'traceback': lines,
            }))
        else:
            self.write(json.dumps({
                'status_code': status_code,
                'message': self._reason,
            }))


class my404handler(BaseHandler):
    def get(self):
        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps({
            'status_code': 404,
            'message': 'illegal call.'
        }))


class darknetZ(WebSocketHandler):
    def check_origin(self, origin):
        return True

    async def open(self):
        if self not in cl:
            cl.append(self)
        print(cl)
        print("opened")
        self.write_message('connected')

    async def on_close(self):
        if self in cl:
            cl.remove(self)
        print(cl)

    async def on_message(self, message):
        data = {
            u'name': u'Los Angeles',
            u'state': u'CA',
            u'country': u'USA'
        }
        db.collection(u'cities').document(u'LA').set(data)


if __name__ == "__main__":
    options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r'/ws', darknetZ)
        ],
        default_handler_class=my404handler,
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(os.environ.get("PORT", options.port))
    tornado.ioloop.IOLoop.instance().start()