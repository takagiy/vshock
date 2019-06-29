from os import path
from logging import getLogger, INFO
from tornado import web
from tornado.web import StaticFileHandler
from tornado.websocket import WebSocketHandler
from tornado.ioloop import IOLoop
import json
from .io import JoystickStream

getLogger(__name__).setLevel(INFO)


class WsServer(WebSocketHandler):
    def initialize(self, js_stream):
        self.js_stream = js_stream
        self.logger = getLogger(__name__)

    def open(self, *args, **kwargs):
        self.logger.info('WebSocket connection has been established.')

    def on_close(self):
        self.logger.info('WebSocket connection has been broken up.')

    def on_message(self, message):
        self.logger.info('Resieve a message: %s', message)
        message = json.loads(message)
        self.js_stream.emit(message)


def serve(port, stream_path, launch_browser):
    with JoystickStream(stream_path) as js_stream:
        ui = path.join(path.dirname(__file__), 'assets/ui')
        app = web.Application([(r"/input", WsServer,
                                dict(js_stream=js_stream)),
                               (r"/(.*)", StaticFileHandler, {
                                   'path': ui,
                                   'default_filename': 'index.html'
                               })])
        app.listen(port)
        IOLoop.instance().start()
