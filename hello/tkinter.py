from tkinter import *

class Application(Frame):
    def  __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.creatWidgets()


    def creatWidgets(self):
        self.helloLable = Label(self, test = 'Hello World'
        self.helloLable = pack()
        self.quitButton = Button(self, text='Quit',command = self.quit)
        self.quitButton.pack()

    app = Application()
    # 设置窗口标题:
    app.master.title('Hello World')
    # 主消息循环:
    app.mainloop()

    