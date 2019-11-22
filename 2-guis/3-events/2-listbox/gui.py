from tkinter import *
from tkinter import messagebox


class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        
        
        
        # add components
        self.__add_ticket_buy_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        self.__add_lyrics_label()
        self.__add_lyrics_listbox()


    def __add_ticket_buy_frame(self):
        self.ticket_buy_frame= Frame()
        self.ticket_buy_frame.grid(row=2,column=0)
        self.ticket_buy_frame.configure(padx=10,pady=10)
        
   
        
    def __add_heading_label(self):
        
        self.heading_label= Label()
        self.heading_label.grid(row=0,column=0)
        self.heading_label.configure(text="Song Maker",font="Arial 30")
        
    def __add_instruction_label(self):
        self.instruction_label= Label()
        self.instruction_label.grid(row=1,column=0,sticky=W,padx=10)
        self.instruction_label.configure(text="Lyric to add: ",font="Aria1 15")


    
        
    def __add_tickets_entry(self):
        self.tickets_entry=Entry(self.ticket_buy_frame)
        self.tickets_entry.pack(side=LEFT)
        self.tickets_entry.configure(width=30,font="Arial 15")
        
        
    def __add_buy_button(self):
        
        self.buy_button=Button(self.ticket_buy_frame)
        self.buy_button.pack(side=RIGHT,padx=10)
        self.buy_button.configure(text="Buy",font="Arial 10", pady=10,padx=30)
        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)



    def __add_lyrics_label(self):
        self.lyrics_label=Label()
        self.lyrics_label.grid(row=3,column=0,sticky=W,padx=10)
        self.lyrics_label.configure(text="Lyrics:", font="Arial 15")

    def __add_lyrics_listbox(self):
        self.lyrics_label=Listbox()
        self.lyrics_label.grid(row=4,column=0,sticky=E+W ,padx=10)
        self.lyrics_label.configure(font="Arial 15")
        
    def __buy_button_clicked(self, event):
        self.lyrics_label.insert(END,self.tickets_entry.get())
