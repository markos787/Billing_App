from tkinter import *

class Bill_App(): # another approach to define root - via class
    def __init__(self, root):
        self.root=root
        self.root.geometry('1350x700+0+0')
        self.root.title('Billing App')
        self.root.resizable(False, False)
        title=Label(root, text='Billing App', font=('Times New Roman', 30, 'bold'), bg='#074463', fg='orangered', bd=12, relief=GROOVE,pady=2)
        title.pack(fill=X) # fill horizontally

        # Variables
        self.cust_name=StringVar()
        self.cust_phone=StringVar()
        self.cust_bill=StringVar()
        self.bill=StringVar() # not used yet

        self.c1=IntVar() # default value = 0
        self.c2=IntVar()
        self.c3=IntVar()
        self.c4=IntVar()
        self.c5=IntVar()
        self.c6=IntVar()
        self.g1=IntVar()
        self.g2=IntVar()
        self.g3=IntVar()
        self.g4=IntVar()
        self.g5=IntVar()
        self.g6=IntVar()
        self.d1=IntVar()
        self.d2=IntVar()
        self.d3=IntVar()
        self.d4=IntVar()
        self.d5=IntVar()
        self.d6=IntVar()

        self.m1=StringVar()
        self.m2=StringVar()
        self.m3=StringVar()
        self.t1=StringVar()
        self.t2=StringVar()
        self.t3=StringVar()

        # Customer details frame
        frame1=LabelFrame(self.root, text='Customer details', font=('Times New Roman', 15, 'bold'), bg='#074463', fg='gold', bd=10, relief=GROOVE) # LabelFrame works like Frame but with the title
        frame1.place(x=0, y=80, relwidth=1)

        cust_name_lbl=Label(frame1, text='Customer Name', font=('Times New Roman', 18, 'bold'), bg='#074463', fg='lightblue1')
        cust_name_ent=Entry(frame1, textvariable=self.cust_name, font='arial 15', bd=7, relief=SUNKEN, width=15, justify='center')
        cust_phone_lbl=Label(frame1, text='Customer Phone', font=('Times New Roman', 18, 'bold'), bg='#074463', fg='lightblue1')
        cust_phone_ent=Entry(frame1, textvariable=self.cust_phone, font='arial 15', bd=7, relief=SUNKEN, width=15, justify='center')
        cust_bill_lbl=Label(frame1, text='Bill Number', font=('Times New Roman', 18, 'bold'), bg='#074463', fg='lightblue1')
        cust_bill_ent=Entry(frame1, textvariable=self.cust_bill, font='arial 15', bd=7, relief=SUNKEN, width=15, justify='center')
        bill_btn=Button(frame1, text='Search', font=('Arial', 12, 'bold'), bd=7, width=10)

        cust_name_lbl.grid(row=0, column=0, padx=(55, 0), pady=1)
        cust_name_ent.grid(row=0, column=1, padx=10, pady=5)
        cust_phone_lbl.grid(row=0, column=2, padx=5, pady=1)
        cust_phone_ent.grid(row=0, column=3, padx=10, pady=5)
        cust_bill_lbl.grid(row=0, column=4, padx=5, pady=1)
        cust_bill_ent.grid(row=0, column=5, padx=10, pady=5)
        bill_btn.grid(row=0, column=6, padx=10)

        # Cosmetics frame
        frame2=LabelFrame(self.root, text='Cosmetics', font=('Times New Roman', 15, 'bold'), bg='#074463', fg='gold', bd=10, relief=GROOVE)
        frame2.place(x=5, y=170, width=325, height=380)

        c1_lbl=Label(frame2, text='Bath Soap', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        c1_txt=Entry(frame2, textvariable=self.c1, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')
        c2_lbl=Label(frame2, text='Face Cream', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        c2_txt=Entry(frame2, textvariable=self.c2, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')
        c3_lbl=Label(frame2, text='Face Wash', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        c3_txt=Entry(frame2, textvariable=self.c3, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')
        c4_lbl=Label(frame2, text='Hair Spray', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        c4_txt=Entry(frame2, textvariable=self.c4, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')
        c5_lbl=Label(frame2, text='Hair Gell', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        c5_txt=Entry(frame2, textvariable=self.c5, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')
        c6_lbl=Label(frame2, text='Body Lotion', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        c6_txt=Entry(frame2, textvariable=self.c6, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')

        c1_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        c1_txt.grid(row=0, column=1, padx=30, pady=10)
        c2_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        c2_txt.grid(row=1, column=1, padx=30, pady=10)
        c3_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        c3_txt.grid(row=2, column=1, padx=30, pady=10)
        c4_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        c4_txt.grid(row=3, column=1, padx=30, pady=10)
        c5_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        c5_txt.grid(row=4, column=1, padx=30, pady=10)
        c6_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        c6_txt.grid(row=5, column=1, padx=30, pady=10)

        # Grocery frame
        frame3=LabelFrame(self.root, text='Grocery', font=('Times New Roman', 15, 'bold'), bg='#074463', fg='gold', bd=10, relief=GROOVE)
        frame3.place(x=340, y=170, width=325, height=380)

        g1_lbl=Label(frame3, text='Rice', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        g1_txt=Entry(frame3, textvariable=self.g1, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')
        g2_lbl=Label(frame3, text='Potatoes', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        g2_txt=Entry(frame3, textvariable=self.g2, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')
        g3_lbl=Label(frame3, text='Corn', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        g3_txt=Entry(frame3, textvariable=self.g3, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')
        g4_lbl=Label(frame3, text='Coffee', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        g4_txt=Entry(frame3, textvariable=self.g4, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')
        g5_lbl=Label(frame3, text='Sugar', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        g5_txt=Entry(frame3, textvariable=self.g5, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')
        g6_lbl=Label(frame3, text='Tea', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        g6_txt=Entry(frame3, textvariable=self.g6, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')

        g1_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        g1_txt.grid(row=0, column=1, padx=30, pady=10)
        g2_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        g2_txt.grid(row=1, column=1, padx=30, pady=10)
        g3_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        g3_txt.grid(row=2, column=1, padx=30, pady=10)
        g4_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        g4_txt.grid(row=3, column=1, padx=30, pady=10)
        g5_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        g5_txt.grid(row=4, column=1, padx=30, pady=10)
        g6_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        g6_txt.grid(row=5, column=1, padx=30, pady=10)

        # Drink frame
        frame4=LabelFrame(self.root, text='Drink', font=('Times New Roman', 15, 'bold'), bg='#074463', fg='gold', bd=10, relief=GROOVE)
        frame4.place(x=675, y=170, width=325, height=380)

        d1_lbl=Label(frame4, text='Coca-Cola', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        d1_txt=Entry(frame4, textvariable=self.d1, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')
        d2_lbl=Label(frame4, text='7up', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        d2_txt=Entry(frame4, textvariable=self.d2, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')
        d3_lbl=Label(frame4, text='Fanta', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        d3_txt=Entry(frame4, textvariable=self.d3, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')
        d4_lbl=Label(frame4, text='Sprite', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        d4_txt=Entry(frame4, textvariable=self.d4, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')
        d5_lbl=Label(frame4, text='Schwepps', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        d5_txt=Entry(frame4, textvariable=self.d5, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')
        d6_lbl=Label(frame4, text='Mirinda', font=('Times New Roman', 16, 'bold'), bg='#074463', fg='lightgreen')
        d6_txt=Entry(frame4, textvariable=self.d6, font=('Times New Roman', 16, 'bold'), width=10, bd=5, relief=SUNKEN, justify='center')

        d1_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        d1_txt.grid(row=0, column=1, padx=30, pady=10)
        d2_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        d2_txt.grid(row=1, column=1, padx=30, pady=10)
        d3_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        d3_txt.grid(row=2, column=1, padx=30, pady=10)
        d4_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        d4_txt.grid(row=3, column=1, padx=30, pady=10)
        d5_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        d5_txt.grid(row=4, column=1, padx=30, pady=10)
        d6_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        d6_txt.grid(row=5, column=1, padx=30, pady=10)

        # Bill area
        frame5=LabelFrame(self.root, bd=10, relief=GROOVE)
        frame5.place(x=1010, y=170, width=340, height=380)

        bill_title=Label(frame5, text='Bill Area', font=('Arial', 15, 'bold'), bd=7, relief=GROOVE)
        bill_title.pack(fill=X)

        scroll=Scrollbar(frame5, orient=VERTICAL)
        self.txtarea=Text(frame5, yscrollcommand=scroll.set) # initialize place for scrollbar in the vertical position
        scroll.pack(side=RIGHT, fill=Y) # scrollbar on the right, fill verically
        scroll.config(command=self.txtarea.yview) # necessary for proper work of scrollbar
        self.txtarea.pack(fill=BOTH, expand=1) # fit scrollbar to the content

        # Button frame
        frame6=LabelFrame(self.root, text='Bill Menu', font=('Times New Roman', 15, 'bold'), bg='#074463', fg='gold', bd=10, relief=GROOVE)
        frame6.place(x=0, y=560, relwidth=1, height=140) # relwidth = 1 expands the frame to the whole window

        m1_lbl=Label(frame6, text='Total cosmetic price', font=('Times New Roman', 14, 'bold'), bg='#074463', fg='cyan')
        m1_ent=Entry(frame6, textvariable=self.m1, font=('Arial', 10, 'bold'), width=18, bd=5, relief=SUNKEN, justify='center')
        m2_lbl=Label(frame6, text='Total grocery price', font=('Times New Roman', 14, 'bold'), bg='#074463', fg='cyan')
        m2_ent=Entry(frame6, textvariable=self.m2, font=('Arial', 10, 'bold'), width=18, bd=5, relief=SUNKEN, justify='center')
        m3_lbl=Label(frame6, text='Total drink price', font=('Times New Roman', 14, 'bold'), bg='#074463', fg='cyan')
        m3_ent=Entry(frame6, textvariable=self.m3, font=('Arial', 10, 'bold'), width=18, bd=5, relief=SUNKEN, justify='center')

        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='w')
        m1_ent.grid(row=0, column=1, padx=10, pady=1)
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='w')
        m2_ent.grid(row=1, column=1, padx=10, pady=5)
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='w')
        m3_ent.grid(row=2, column=1, padx=10, pady=1)

        t1_lbl=Label(frame6, text='Cosmetic tax', font=('Times New Roman', 14, 'bold'), bg='#074463', fg='plum1')
        t1_ent=Entry(frame6, textvariable=self.t1, font=('Arial', 10, 'bold'), width=18, bd=5, relief=SUNKEN, justify='center')
        t2_lbl=Label(frame6, text='Grocery tax', font=('Times New Roman', 14, 'bold'), bg='#074463', fg='plum1')
        t2_ent=Entry(frame6, textvariable=self.t2, font=('Arial', 10, 'bold'), width=18, bd=5, relief=SUNKEN, justify='center')
        t3_lbl=Label(frame6, text='Drink tax', font=('Times New Roman', 14, 'bold'), bg='#074463', fg='plum1')
        t3_ent=Entry(frame6, textvariable=self.t3, font=('Arial', 10, 'bold'), width=18, bd=5, relief=SUNKEN, justify='center')

        t1_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='w')
        t1_ent.grid(row=0, column=3, padx=10, pady=1)
        t2_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='w')
        t2_ent.grid(row=1, column=3, padx=10, pady=5)
        t3_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='w')
        t3_ent.grid(row=2, column=3, padx=10, pady=1)

        frame_btn=Frame(frame6, bd=7, relief=GROOVE)
        frame_btn.place(x=740, width=585, height=100)

        total_btn=Button(frame_btn, text='Total', font=('Arial', 14, 'bold'), bd=4, bg='cadetblue', fg='gray20', width=10, height=2)
        gen_bill_btn=Button(frame_btn, text='Generate Bill', font=('Arial', 14, 'bold'), bd=4, bg='cadetblue', fg='gray20', width=10, height=2)
        clear_btn=Button(frame_btn, text='Clear', font=('Arial', 14, 'bold'), bd=4, bg='cadetblue', fg='gray20', width=10, height=2)
        exit_btn=Button(frame_btn, text='Exit', font=('Arial', 14, 'bold'), bd=4, bg='cadetblue', fg='gray20', width=10, height=2)

        total_btn.grid(row=0, column=0, padx=4, pady=9)
        gen_bill_btn.grid(row=0, column=1, padx=4, pady=9)
        clear_btn.grid(row=0, column=2, padx=4, pady=9)
        exit_btn.grid(row=0, column=3, padx=4, pady=9)


root=Tk()
obj=Bill_App(root)
root.mainloop()