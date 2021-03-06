#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    May 11, 2022 10:31:26 PM +07  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
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

        top.geometry("1200x700+321+168")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("E-Tracking App - for Employees")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#0080ff")
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
        photo_location = "img/employee_bg (Custom).png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.175, rely=0.2, relheight=0.607, relwidth=0.646)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#ffffff")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Button_update = tk.Button(self.Frame2)
        self.Button_update.place(relx=0.284, rely=0.118, height=43, width=336)
        self.Button_update.configure(activebackground="beige")
        self.Button_update.configure(activeforeground="#000000")
        self.Button_update.configure(background="#d9d9d9")
        self.Button_update.configure(compound='left')
        self.Button_update.configure(cursor="fleur")
        self.Button_update.configure(disabledforeground="#a3a3a3")
        self.Button_update.configure(foreground="#000000")
        self.Button_update.configure(highlightbackground="#d9d9d9")
        self.Button_update.configure(highlightcolor="black")
        self.Button_update.configure(pady="0")
        self.Button_update.configure(text='''Update Package's Status''')
        self.Button_update.configure(command=self.update_btn)

        self.Button_add = tk.Button(self.Frame2)
        self.Button_add.place(relx=0.284, rely=0.306, height=43, width=336)
        self.Button_add.configure(activebackground="beige")
        self.Button_add.configure(activeforeground="#000000")
        self.Button_add.configure(background="#d9d9d9")
        self.Button_add.configure(compound='left')
        self.Button_add.configure(disabledforeground="#a3a3a3")
        self.Button_add.configure(foreground="#000000")
        self.Button_add.configure(highlightbackground="#d9d9d9")
        self.Button_add.configure(highlightcolor="black")
        self.Button_add.configure(pady="0")
        self.Button_add.configure(text='''Add Package''')
        self.Button_add.configure(command=self.add_btn)

        self.Button_sign_up = tk.Button(self.Frame2)
        self.Button_sign_up.place(relx=0.284, rely=0.494, height=43, width=336)
        self.Button_sign_up.configure(activebackground="beige")
        self.Button_sign_up.configure(activeforeground="#000000")
        self.Button_sign_up.configure(background="#d9d9d9")
        self.Button_sign_up.configure(compound='left')
        self.Button_sign_up.configure(disabledforeground="#a3a3a3")
        self.Button_sign_up.configure(foreground="#000000")
        self.Button_sign_up.configure(highlightbackground="#d9d9d9")
        self.Button_sign_up.configure(highlightcolor="black")
        self.Button_sign_up.configure(pady="0")
        self.Button_sign_up.configure(text='''Sign Up User''')
        self.Button_sign_up.configure(command=self.sign_up_btn)

        self.Button_log_out = tk.Button(self.top)
        self.Button_log_out.place(relx=0.883, rely=0.029, height=100, width=100)
        self.Button_log_out.configure(activebackground="beige")
        self.Button_log_out.configure(activeforeground="#000000")
        self.Button_log_out.configure(background="#f5010a")
        self.Button_log_out.configure(compound='left')
        self.Button_log_out.configure(disabledforeground="#a3a3a3")
        self.Button_log_out.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Button_log_out.configure(foreground="#ffffff")
        self.Button_log_out.configure(highlightbackground="#d9d9d9")
        self.Button_log_out.configure(highlightcolor="black")
        self.Button_log_out.configure(pady="0")
        # self.Button_log_out.configure(text='''Log Out''')
        self.Button_log_out.configure(command=self.log_out_btn)
        photo_location = "img/Log Out (Custom).png"
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.Button_log_out.configure(image=_img4)

    def update_btn(self):
        self.top.destroy() 
        all_support.main_update_package_page()
        if __name__ == '__main__':
            all_support.main_update_package_page()

    def add_btn(self):
        self.top.destroy() 
        all_support.main_add_package()
        if __name__ == '__main__':
            all_support.main_add_package()

    def sign_up_btn(self):
        self.top.destroy() 
        all_support.main_create_user_page1()
        if __name__ == '__main__':
            all_support.main_create_user_page1()

    def log_out_btn(self):
        self.top.destroy() 
        all_support.main_login_page1()
        if __name__ == '__main__':
            all_support.main_login_page1()


def start_up():
    all_support.main_backend_page1()

if __name__ == '__main__':
    all_support.main_backend_page1()




