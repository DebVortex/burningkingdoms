from client import Client

HOST, PORT = "localhost", 9999


def main():
    client = Client(HOST, PORT)
    client.connect()
    running = True
    while running:
        message = input().strip()
        if message == 'quit':
            running = False
        else:
            client.send(message)


if __name__ == "__main__":
    main()
