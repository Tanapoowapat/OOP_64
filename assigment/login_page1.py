#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    May 11, 2022 09:25:27 PM +07  platform: Windows NT

from logging import root
from login import Login
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import tkinter.messagebox as tsmg




from Backend.station import Station
from Backend.admin import Admin
from Backend.customer import Customer

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

        top.geometry("1200x700+370+152")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("E-Tracking App - Log In")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ff8080")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        
        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0, rely=0, height=700, width=1200)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(cursor="fleur")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = "img/user_bg (Custom).png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)

        self.Frame_login = tk.Frame(self.Frame1)
        self.Frame_login.place(relx=0.325, rely=0.043, relheight=0.92, relwidth=0.345)
        self.Frame_login.configure(relief='groove')
        self.Frame_login.configure(borderwidth="2")
        self.Frame_login.configure(relief="groove")
        self.Frame_login.configure(background="#ffffff")
        self.Frame_login.configure(highlightbackground="#d9d9d9")
        self.Frame_login.configure(highlightcolor="black")

        self.Label_login = tk.Label(self.Frame_login)
        self.Label_login.place(relx=0.072, rely=0.035, height=76, width=352)
        self.Label_login.configure(activebackground="#ffffff")
        self.Label_login.configure(background="#ffffff")
        self.Label_login.configure(compound='left')
        self.Label_login.configure(disabledforeground="#ffffff")
        self.Label_login.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.Label_login.configure(foreground="#000000")
        self.Label_login.configure(highlightbackground="#d9d9d9")
        self.Label_login.configure(highlightcolor="black")
        self.Label_login.configure(text='''Log In''')

        self.Entry_user = tk.Entry(self.Frame_login)
        self.Entry_user.place(relx=0.121, rely=0.266, height=34, relwidth=0.778)
        self.Entry_user.configure(background="white")
        self.Entry_user.configure(borderwidth="1")
        self.Entry_user.configure(disabledforeground="#a3a3a3")
        self.Entry_user.configure(font="-family {Segoe UI} -size 10")
        self.Entry_user.configure(foreground="#000000")
        self.Entry_user.configure(highlightbackground="#d9d9d9")
        self.Entry_user.configure(highlightcolor="black")
        self.Entry_user.configure(insertbackground="black")
        self.Entry_user.configure(selectbackground="#c4c4c4")
        self.Entry_user.configure(selectforeground="black")

        self.Entry_password = tk.Entry(self.Frame_login)
        self.Entry_password.place(relx=0.121, rely=0.405, height=34, relwidth=0.778)
        self.Entry_password.configure(background="white")
        self.Entry_password.configure(borderwidth="1")
        self.Entry_password.configure(disabledforeground="#a3a3a3")
        self.Entry_password.configure(font="-family {Segoe UI} -size 10")
        self.Entry_password.configure(foreground="#000000")
        self.Entry_password.configure(highlightbackground="#d9d9d9")
        self.Entry_password.configure(highlightcolor="black")
        self.Entry_password.configure(insertbackground="black")
        self.Entry_password.configure(selectbackground="#c4c4c4")
        self.Entry_password.configure(selectforeground="black")
        self.Entry_password.configure(show="*")

        self.Label_user = tk.Label(self.Frame_login)
        self.Label_user.place(relx=0.121, rely=0.214, height=26, width=42)
        self.Label_user.configure(activebackground="#f9f9f9")
        self.Label_user.configure(anchor='w')
        self.Label_user.configure(background="#ffffff")
        self.Label_user.configure(compound='left')
        self.Label_user.configure(disabledforeground="#a3a3a3")
        self.Label_user.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Label_user.configure(foreground="#000000")
        self.Label_user.configure(highlightbackground="#d9d9d9")
        self.Label_user.configure(highlightcolor="black")
        self.Label_user.configure(text='''User''')

        self.Label_password = tk.Label(self.Frame_login)
        self.Label_password.place(relx=0.121, rely=0.353, height=26, width=82)
        self.Label_password.configure(activebackground="#f9f9f9")
        self.Label_password.configure(anchor='w')
        self.Label_password.configure(background="#ffffff")
        self.Label_password.configure(compound='left')
        self.Label_password.configure(disabledforeground="#a3a3a3")
        self.Label_password.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Label_password.configure(foreground="#000000")
        self.Label_password.configure(highlightbackground="#d9d9d9")
        self.Label_password.configure(highlightcolor="black")
        self.Label_password.configure(text='''Password''')

        self.Label_station = tk.Label(self.Frame_login)
        self.Label_station.place(relx=0.121, rely=0.490, height=26, width=90)
        self.Label_station.configure(activebackground="#f9f9f9")
        self.Label_station.configure(anchor='w')
        self.Label_station.configure(background="#ffffff")
        self.Label_station.configure(compound='left')
        self.Label_station.configure(disabledforeground="#a3a3a3")
        self.Label_station.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Label_station.configure(foreground="#000000")
        self.Label_station.configure(highlightbackground="#d9d9d9")
        self.Label_station.configure(highlightcolor="black")
        self.Label_station.configure(text='''Station's ID''')

        # Dropdown menu options
        options_station = []
        for station in Station.All_station_list:
            options_station.append(station)
        
        # datatype of menu text
        clicked_station = tk.StringVar()
        
        # initial menu text
        clicked_station.set( "Please Select" )

        self.Entry_station = ttk.Combobox(self.Frame_login, values=options_station)
        self.Entry_station.place(relx=0.121, rely=0.550, height=34, relwidth=0.778)
        self.Entry_station.set('--Select Station--')
        
        self.Button_login = tk.Button(self.Frame_login)
        self.Button_login.place(relx=0.386, rely=0.879, height=53, width=96)
        self.Button_login.configure(activebackground="#008040")
        self.Button_login.configure(activeforeground="white")
        self.Button_login.configure(activeforeground="#000000")
        self.Button_login.configure(background="#00d776")
        self.Button_login.configure(compound='left')
        self.Button_login.configure(disabledforeground="#008000")
        self.Button_login.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Button_login.configure(foreground="#ffffff")
        self.Button_login.configure(highlightbackground="#000000")
        self.Button_login.configure(highlightcolor="black")
        self.Button_login.configure(pady="0")
        self.Button_login.configure(text='''Log In''')
        self.Button_login.configure(command=self.login_btn)
        
        self.Label_type_account = tk.Label(self.Frame_login)
        self.Label_type_account.place(relx=0.121, rely=0.620, height=26, width=100)
        self.Label_type_account.configure(activebackground="#f9f9f9")
        self.Label_type_account.configure(anchor='w')
        self.Label_type_account.configure(background="#ffffff")
        self.Label_type_account.configure(compound='left')
        self.Label_type_account.configure(disabledforeground="#a3a3a3")
        self.Label_type_account.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Label_type_account.configure(foreground="#000000")
        self.Label_type_account.configure(highlightbackground="#d9d9d9")
        self.Label_type_account.configure(highlightcolor="black")
        self.Label_type_account.configure(text='''Type Account''')
        
        
        # Dropdown menu options
        options_station = ['Customer', 'Employee', 'Admin']
        
        self.Entry_type_acount = ttk.Combobox(self.Frame_login, values=options_station)
        self.Entry_type_acount.place(relx=0.121, rely=0.680, height=34, relwidth=0.778)
        self.Entry_type_acount.set('--Select Type--')

        

        

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

    def login_btn(self):
        print(Customer.All_Customer_list)
        username = self.Entry_user.get()
        password = self.Entry_password.get()
        station = self.Entry_station.get()

        if self.Entry_type_acount.get() == "Customer":
            
            if Login.login_customer(username, password):
                self.top.destroy() 
                all_support.main_search_page()
                if __name__ == '__main__':
                    all_support.main_search_page()
            else:
                tsmg.showerror('login failed','can not log in, please try again!') #alert pop-up
        
        elif self.Entry_type_acount.get() == "Employee":
            if Login.login_employee(username, password, station):
                self.top.destroy() 
                all_support.main_backend_page1()
                if __name__ == '__main__':
                    all_support.main_backend_page1()
            else:
                tsmg.showerror('login failed','can not log in, please try again!') #alert pop-up

        elif self.Entry_type_acount.get() == "Admin":
            if Login.login_admin(username, password):
                self.top.destroy() 
                all_support.main_administrator_page()
                if __name__ == '__main__':
                    all_support.main_administrator_page()
            else:
                tsmg.showerror('login failed','can not log in, please try again!') #alert pop-up
        else:
            tsmg.showerror('login failed','can not log in, please try again!') #alert pop-up




def start_up():
    all_support.main_login_page1()

if __name__ == '__main__':
    all_support.main_login_page1()



