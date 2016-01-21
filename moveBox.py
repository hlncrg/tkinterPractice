from Tkinter import *
from PIL import Image, ImageTk

root=Tk()

class app(Frame):
    def createWidgets(self):
        #creates a canvas to draw objects on
        self.draw = Canvas(self, width="5i", height="5i")
        #draw a box
        self.box = self.draw.create_rectangle("1i", "1i", "1.10i", "1.10i",
                                          fill="red")
        #add the canvas
        self.draw.pack(side=LEFT)
        #create a title for the window
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        #add a quit button
        quitButton=Button(self,text='Quit',command=self.client_exit)
        quitButton.place(x=0,y=0)
        #add buttons to the menu
        menu=Menu(self.master)
        self.master.config(menu=menu)
        file=Menu(menu)
        file.add_command(label='Save')
        file.add_command(label='Exit',command=self.client_exit)
        menu.add_cascade(label='File',menu=file)
        #add image and text buttons
        edit = Menu(menu)
        edit.add_command(label="Show Image",command=self.showImg)
        edit.add_command(label="Show Text",command=self.showTxt)
        menu.add_cascade(label="Edit", menu=edit)
        #add the ability to move the box
        root.bind('<Left>',self.leftKey)
        root.bind('<Right>',self.rightKey)
        root.bind('<Up>',self.upKey)
        root.bind('<Down>',self.downKey)

    def client_exit(self):
        exit()#exit button
    def showImg(self):#show an image
        load=Image.open('cats.gif')
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render)
        img.image=render
        img.place(x=0,y=0)
    def showTxt(self):#show text
        text = Label(self, text="Hey there good lookin!")
        text.pack()





    def leftKey(self,event):#move box left
        self.draw.move(self.box,-1,0)
    def rightKey(self,event):#move box right
        self.draw.move(self.box,1,0)
    def upKey(self,event):#move box up
        self.draw.move(self.box,0,-1)
    def downKey(self,event):#move box down
        self.draw.move(self.box,0,1)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        Pack.config(self)
        self.createWidgets()

game = app()
game.mainloop()
