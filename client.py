import socket
import threading
import os
import tkinter as tk


UDP_MAX_SIZE = 65535

def listen(s: socket.socket):
    while True:
        msg = s.recv(UDP_MAX_SIZE)
        print('\r\r' + msg.decode('ascii') + '\n' + f'you: ', end='')


def connect(host: str = '127.0.0.1', port: int = 3000):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.connect((host, port))

    threading.Thread(target=listen, args=(s,), daemon=True).start()

    # s.send('__join'.encode('ascii'))

    # s.send('hello'.encode('ascii'))

    app = HelloWindow(s)
    app.geometry("250x75")

    app.mainloop()


class HelloWindow(tk.Tk):

    def greet(self, socket):
        print('123123123123')
        socket.send('helllo'.encode('ascii'))

    def __init__(self, socket, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Hello Window GUI app")
        btn = tk.Button(self, text="CLICK ME", command=lambda: self.greet(socket))
        btn.pack(side=tk.TOP)


if __name__ == "__main__":
    connect()