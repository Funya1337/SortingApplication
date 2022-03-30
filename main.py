from tkinter import *
import random
import time

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
        self.createButton(215, 50, "Back", self.test)
        self.createButton(260, 50, "Forward", self.test)
        self.createDrawingBtn()

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
        print(self.root)

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
        btn = Button(self.root, text = 'Drawing Mode', command = self.useDrawingMode, width = 12, height = 3)
        btn.place(x = 390, y = 20)

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
        default_y = 300
        default_width = 15
        self.array = []
        cnt = 0
        for i in range(self.scaleValue):
            element = random.randint(1, 100)
            self.createRectangle(default_x + cnt, default_y, default_width, element * 2)
            self.array.append(element)
            cnt += 20

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
        for i in self.items:
            self.canvas.itemconfig(i, fill = GUI.selection_color)
            self.canvas.update()
            time.sleep(self.speed)

        for i in self.items:
            self.canvas.itemconfig(i, fill= GUI.default_color)

    def bubbleSort(self):
        self.items = list(self.canvas.find_all())
        for i in range(0, len(self.array) - 1):
            for j in range(len(self.array) - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.reDrawChart(j, j + 1)
        self.finalHightLight()

    def selectionSort(self):
        self.items = list(self.canvas.find_all())
        for i in range(len(self.array)):
            min_idx = i
            for j in range(i + 1, len(self.array)):
                if self.array[min_idx] > self.array[j]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.reDrawChart(i, min_idx)
        self.finalHightLight()

gui = GUI()