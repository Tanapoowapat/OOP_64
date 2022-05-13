#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    May 11, 2022 10:00:58 PM +07  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from Backend.customer import Customer
from Backend.station import Station
from Backend.admin import Admin
from tkinter.constants import *

import all_support

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 
        _tabbg1 = 'grey75' 
        _tabbg2 = 'grey89' 
        _bgmode = 'light' 

        top.geometry("1200x700+312+165")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("E-Tracking App - Search")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.0, rely=-0.014, relheight=1.014, relwidth=1.0)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ff8080")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.0, rely=-0.014, relheight=1.014, relwidth=1.0)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(cursor="fleur")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")


        self.Frame_search = tk.Frame(self.Frame1)
        self.Frame_search.place(relx=0.133, rely=0.144, relheight=0.693
                , relwidth=0.742)
        self.Frame_search.configure(relief='groove')
        self.Frame_search.configure(borderwidth="2")
        self.Frame_search.configure(relief="groove")
        self.Frame_search.configure(background="#ffffff")
        self.Frame_search.configure(highlightbackground="#d9d9d9")
        self.Frame_search.configure(highlightcolor="black")

        self.Entry1 = tk.Entry(self.Frame_search)
        self.Entry1.place(relx=0.213, rely=0.39, height=74, relwidth=0.6)
        self.Entry1.configure(background="white")
        self.Entry1.configure(borderwidth="5")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 20")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(justify='center')
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Button_search = tk.Button(self.Frame_search)
        self.Button_search.place(relx=0.427, rely=0.65, height=63, width=136)
        self.Button_search.configure(activebackground="#c0c0c0")
        self.Button_search.configure(activeforeground="#000000")
        self.Button_search.configure(background="#0080ff")
        self.Button_search.configure(compound='left')
        self.Button_search.configure(disabledforeground="#0080ff")
        self.Button_search.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Button_search.configure(foreground="#ffffff")
        self.Button_search.configure(highlightbackground="#d9d9d9")
        self.Button_search.configure(highlightcolor="black")
        self.Button_search.configure(pady="0")
        self.Button_search.configure(text='''Search''')
        self.Button_search.configure(command=self.search_btn)

        self.Label_search = tk.Label(self.Frame_search)
        self.Label_search.place(relx=0.247, rely=0.144, height=56, width=463)
        self.Label_search.configure(activebackground="#f9f9f9")
        self.Label_search.configure(background="#ffffff")
        self.Label_search.configure(compound='left')
        self.Label_search.configure(disabledforeground="#a3a3a3")
        self.Label_search.configure(font="-family {Segoe UI} -size 23 -weight bold")
        self.Label_search.configure(foreground="#000000")
        self.Label_search.configure(highlightbackground="#d9d9d9")
        self.Label_search.configure(highlightcolor="black")
        self.Label_search.configure(text='''Enter your package's uguiID''')

        
        self.Button_history = tk.Button(self.Frame1)
        self.Button_history.place(relx=0.842, rely=0.9, height=43, width=156)
        self.Button_history.configure(activebackground="beige")
        self.Button_history.configure(activeforeground="#000000")
        self.Button_history.configure(background="#d9d9d9")
        self.Button_history.configure(compound='left')
        self.Button_history.configure(disabledforeground="#a3a3a3")
        self.Button_history.configure(foreground="#000000")
        self.Button_history.configure(highlightbackground="#d9d9d9")
        self.Button_history.configure(highlightcolor="black")
        self.Button_history.configure(pady="0")
        self.Button_history.configure(text='''History''')
        self.Button_history.configure(command=self.history_btn)

        self.Label_search = tk.Label(self.Frame_search)
        self.Label_search.place(relx=0.447, rely=0.144, height=56, width=463)
        self.Label_search.configure(activebackground="#f9f9f9")
        self.Label_search.configure(background="#ffffff")
        self.Label_search.configure(compound='left')
        self.Label_search.configure(disabledforeground="#a3a3a3")
        self.Label_search.configure(font="-family {Segoe UI} -size 23 -weight bold")
        self.Label_search.configure(foreground="#000000")
        self.Label_search.configure(highlightbackground="#d9d9d9")
        self.Label_search.configure(highlightcolor="black")
        self.Label_search.configure(text='')

    def search_btn(self):
        package_id = self.Entry1.get()
        print(package_id)

    def history_btn(self):
        print('history')
        self.top.destroy() 
        all_support.main_history_page()
        if __name__ == '__main__':
            all_support.main_history_page()
                    

def start_up():
    all_support.main_search_page1()

if __name__ == '__main__':
    all_support.main_search_page1()




