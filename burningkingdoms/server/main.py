import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line

from core import GameHandler

define("port", default=8888, help="run on the given port", type=int)


def main():
    parse_command_line()
    server = tornado.web.Application([(r'/', GameHandler)])
    server.listen(options.port)
    print("Running Server on port {port}".format(port=options.port))
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
