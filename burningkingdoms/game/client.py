from ws4py.client.threadedclient import WebSocketClient


class Client(WebSocketClient):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        super(Client, self).__init__(self._url)

    @property
    def _url(self):
        return 'ws://{host}:{port}/'.format(host=self.host, port=self.port)

    def opened(self):
        print("Connected to server at {host}:{port}".format(host=self.host, port=self.port))

    def received_message(self, message):
        print(message)
