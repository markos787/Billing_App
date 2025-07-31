from tkinter import *

class Bill_App(): # another approach to define root - via class
    def __init__(self, root):
        self.root=root
        self.root.geometry('1350x700+0+0')
        self.root.title('Billing App')
        self.root.resizable(False, False)
        title=Label(root, text='Billing App', font=('Times New Roman', 30, 'bold'), bg='#074463', fg='white', bd=12, relief=GROOVE,pady=2)
        title.pack(fill=X) # fill horizontally

root=Tk()
obj=Bill_App(root)
root.mainloop()