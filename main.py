from tkinter import *
import random
import time
import socket
import select
import errno
import sys

# HEADER_LENGTH = 10

# IP = '127.0.0.1'
# PORT = 8080

# my_username = input("Username: ")

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect((IP, PORT))
# client_socket.setblocking(False)

# username = my_username.encode("utf-8")
# username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
# client_socket.send(username_header + username)

# while True:
#     #message = input(f"{my_username} > ")
#     message = ""

#     if message:
#         message = message.encode('utf-8')
#         message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
#         client_socket.send(message_header + message)
    
#     try:
#         while True:
#             username_header = client_socket.recv(HEADER_LENGTH)
#             if not len(username_header):
#                 print("connection closed by the server")
#                 sys.exit()
#             username_length = int(username_header.decode("utf-8").strip())
#             username = client_socket.recv(username_length).decode("utf-8")

#             message_header = client_socket.recv(HEADER_LENGTH)
#             message_length = int(message_header.decode("utf-8").strip())
#             message = client_socket.recv(message_length).decode("utf-8")

#             print(f"{username} > {message}")
    
#     except IOError as e:
#         if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
#             print('Reading error', str(e))
#             sys.exit()
#         continue

#     except Exception as e:
#         print('General error', str(e))
#         sys.exit()



class GUI:
    default_color = '#AAAAFF'
    hightlight_color = 'red'
    selection_color = 'green'
    def __init__(self):
        self.root = Tk()
        self.root.title('Sort Application')
        self.root.resizable(False, False)
        self.canvas = Canvas(self.root, width = 1000, height = 500)
        self.array = []
        self.items = []
        self.prevArray = []
        self.scaleValue = 10
        self.speed = 0.01
        self.canvas.pack()
        self.mainSettings()
        self.root.mainloop()

    def mainSettings(self):
        self.createButton(20, 20, "Rand Array", self.fillRandArray)
        self.createScale(100, 0, self.getValue)
        self.createButton(215, 20, "Bubble sort", self.bubbleSort)
        self.createButton(300, 20, "Selection sort", self.selectionSort)
        self.createLabel(0, 55)
        self.createSpeedScale(100, 38)
        self.createButton(215, 50, "Quick sort", self.startQuickSort)
        self.createButton(300, 50, "Insertion sort", self.insertionSort)
        self.createDrawingBtn()
        self.createEraseBtn()

    def getValue(self, event):
        self.scaleValue = self.scale.get()

    def test(self):
        print(self.array)
        #print(self.canvas.find_all())
        #items = list(self.canvas.find_all())
        #self.canvas.move(items[0], 20, 0)
        #self.canvas.delete(items[0])
        #self.canvas.itemconfig(items[0], fill = 'green')

    def useDrawingMode(self):
        self.old_x = None
        self.old_y = None
        self.line_width = 5
        self.color = "blue"
        self.eraser_on = False
        self.active_button = self.drawingBtn
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button = some_button
        self.eraser_on = eraser_mode
    
    def useErase(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def use_pen(self):
        self.activate_button(self.pen_button)
    
    def paint(self, event):
        if self.eraser_on:
            paint_color = 'SystemButtonFace'
            self.line_width = 15
        else:
            paint_color = self.color
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y
    
    def reset(self, event):
        self.old_x, self.old_y = None, None

    def getSpeed(self, event):
        if event == '1':
            self.speed = 0.01
        elif event == '2':
            self.speed = 0.05
        else:
            self.speed = 0.1

    def createSpeedScale(self, cord_x, cord_y):
        self.speedScale = Scale(self.canvas, from_=1, to=3, orient=HORIZONTAL, command=self.getSpeed)
        self.speedScale.place(x=cord_x, y=cord_y)

    def createDrawingBtn(self):
        self.drawingBtn = Button(self.root, text = 'Drawing Mode', command = self.useDrawingMode, width = 12, height = 3)
        self.drawingBtn.place(x = 390, y = 20)
    
    def createEraseBtn(self):
        self.eraser_button = Button(self.root, text = 'Erase Mode', command = self.useErase, width = 12, height = 3)
        self.eraser_button.place(x = 500, y = 20)

    def createLabel(self, cord_x, cord_y):
        label = Label(self.canvas, text='Animation Speed:')
        label.place(x = cord_x, y = cord_y)

    def createScale(self, cord_x, cord_y, func):
        self.scale = Scale(self.canvas, from_=10, to=46, orient=HORIZONTAL, command=func)
        self.scale.place(x=cord_x, y=cord_y)

    def createRectangle(self, x, y, width, height):
        return self.canvas.create_rectangle(x, y, x+width, y-height, fill=GUI.default_color, outline='#0000ff')

    def createButton(self, cord_x, cord_y, message, func):
        btn = Button(self.root, text = message, command = func)
        btn.place(x = cord_x, y = cord_y)

    def fillRandArray(self):
        print(self.scaleValue)
        self.canvas.delete('all')
        default_x = 50
        default_y = 350
        default_width = 15
        self.array = []
        cnt = 0
        for i in range(self.scaleValue):
            element = random.randint(1, 100)
            self.createRectangle(default_x + cnt, default_y, default_width, element * 2)
            self.array.append(element)
            cnt += 20
        self.items = list(self.canvas.find_all())

    def reDrawChart(self, idx1, idx2):
        mult = 20
        if idx2 - idx1 == 1:
            diff = 1
        else:
            diff = (idx2 - idx1)
        tag1 = self.items[idx1]
        tag2 = self.items[idx2]
        self.canvas.itemconfig(tag1, fill = GUI.hightlight_color)
        self.canvas.move(tag1, mult*diff, 0)
        self.canvas.update()
        self.canvas.itemconfig(tag2, fill = GUI.hightlight_color)
        self.canvas.move(tag2, -mult*diff, 0)
        self.canvas.update()
        self.canvas.itemconfig(tag1, fill = GUI.default_color)
        self.canvas.itemconfig(tag2, fill = GUI.default_color)
        self.items[idx1], self.items[idx2] = self.items[idx2], self.items[idx1]
        time.sleep(self.speed - 0.01)

    def finalHightLight(self):
        print(self.items)
        for i in self.items:
            self.canvas.itemconfig(i, fill = GUI.selection_color)
            self.canvas.update()
            time.sleep(self.speed)

        for i in self.items:
            self.canvas.itemconfig(i, fill= GUI.default_color)

    def bubbleSort(self):
        for i in range(0, len(self.array) - 1):
            for j in range(len(self.array) - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.reDrawChart(j, j + 1)
        self.finalHightLight()

    def selectionSort(self):
        for i in range(len(self.array)):
            min_idx = i
            for j in range(i + 1, len(self.array)):
                if self.array[min_idx] > self.array[j]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.reDrawChart(i, min_idx)
        self.finalHightLight()

    def partition(self, array, low, high):
      pivot = array[high]
      i = low - 1
      for j in range(low, high):
        if array[j] <= pivot:
          i = i + 1
          (array[i], array[j]) = (array[j], array[i])
          self.reDrawChart(i, j)

      (array[i + 1], array[high]) = (array[high], array[i + 1])
      self.reDrawChart(i + 1, high)
      return i + 1

    def quickSort(self, array, low, high):
      if low < high:
        pi = self.partition(array, low, high)
        self.quickSort(array, low, pi - 1)
        self.quickSort(array, pi + 1, high)

    def startQuickSort(self):
        self.quickSort(self.array, 0, len(self.array) - 1)
        self.finalHightLight()

    def insertionSort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i-1
            while j >= 0 and key < self.array[j] :
                    self.array[j + 1] = self.array[j]
                    self.reDrawChart(j + 1, j)
                    j -= 1
            self.array[j + 1] = key
        self.finalHightLight()

gui = GUI()
