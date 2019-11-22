#import all classses from the tkinter library
from tkinter import *

#class definition for our gui
class Gui(Tk):

    #constructor for making Gui objects
    def __init__(self):
        super().__init__()

        #set window attributes
        self.geometry("500x500")
        self.title("Newsletter")
        self.configure(bg="#ff0", height=500,width=500)


        #add components ot the window
        self.__add_heading_label()
        self.__add_describe_label()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_subscribe_button()

    def __add_heading_label(self):
        # create
        self.heading_label= Label()
        self.heading_label.place(x=30,y=0)
        # style
        self.heading_label.configure(text="RECEIVE OUR NEWSLETTER",bg="#ff0", font="Arial 18")
        # handle events

     

    def __add_describe_label(self):
        # create
        self.describe_label= Label()
        self.describe_label.place(x=20,y=50)
        # style
        self.describe_label.configure(text="Please enter your email below to receive our newsletter",bg="#ff0", font="Arial 10")
        # handle events

    def __add_email_label(self):
        # create
        self.email_label= Label()
        self.email_label.place(x=30,y=100)
        # style
        self.email_label.configure(text="Email: ",bg="#ff0", font="Arial 10")
        # handle events

    def __add_email_entry(self):
        # create
        self.email_entry= Entry()
        self.email_entry.place(x=80,y=100)
        # style
        self.email_label.configure(width=40)
        # handle events

    def __add_subscribe_button(self):
        # create
        self.subscribe_button= Button()
        self.subscribe_button.place(x=10,y=150)
        # style
        self.subscribe_button.configure(text="Subscribe",width=50)
        # handle events
