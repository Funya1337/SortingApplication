from tkinter import *
import socket
import threading
from gui import GUI

UDP_MAX_SIZE = 65535

root = Tk()
root.title('Sort Application')
root.resizable(False, False)
canvas = Canvas(root, width = 1000, height = 500)
canvas.pack()
gui = GUI(root, canvas)

def listen(s: socket.socket):
    while True:
        msg = s.recv(UDP_MAX_SIZE)
        msg = msg.decode('ascii')
        string = msg.split(" ")
        print(string)
        x0 = int(string[1])
        y0 = int(string[2])
        x1 = int(string[3])
        y1 = int(string[4])
        paintColor = string[5]
        gui.drawIncomeData(x0, y0, x1, y1, paintColor)
        print('\r\r' + msg + '\n' + f'you: ', end='')


def connect(host: str = '178.79.156.57', port: int = 80):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.connect((host, port))

    threading.Thread(target=listen, args=(s,), daemon=True).start()

    gui.setSocket(s)
    root.mainloop()

    # s.send('__join'.encode('ascii'))

    # s.send('hello'.encode('ascii'))

if __name__ == "__main__":
    connect()