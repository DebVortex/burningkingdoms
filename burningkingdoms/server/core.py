import tornado.ioloop
import tornado.web
import tornado.websocket

# we gonna store clients in dictionary..
clients = dict()


class GameHandler(tornado.websocket.WebSocketHandler):

    def open(self, *args):
        self.id = id(self)
        self.stream.set_nodelay(True)
        clients[self.id] = self
        print("New client connected. Id: {id}".format(id=self.id))
        for _id, sock in clients.items():
            if _id != self.id:
                sock.write_message('New client connected: {id}'.format(id=self.id))

    def on_message(self, message):
        """
        when we receive some message we want some message handler..
        for this example i will just print message to console
        """
        print("Client {id} received a message : {message}".format(id=self.id, message=message))
        for _id, sock in clients.items():
            if not self.id == _id:
                sock.write_message('[{id}]: {message}'.format(id=self.id, message=message))

    def on_close(self):
        if self.id in clients:
            print("Client {id} disconnected".format(id=self.id))
            del clients[self.id]
        for _id, sock in clients.items():
            sock.write_message("Client {id} disconnected".format(id=self.id))

    def check_origin(self, *args, **kwargs):
        return True
