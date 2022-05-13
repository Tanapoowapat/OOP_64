#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    May 12, 2022 07:16:36 AM +07  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from Backend.station import Station
from Backend.admin import Admin
import tkinter.messagebox as tsmg

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

        top.geometry("1200x700+316+148")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("E-Tracking App - Administrator - Update Employee")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#c1cb50")
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
        photo_location = "img/Background-PNG-Clipart-Background.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.275, rely=0.071, relheight=0.864
                , relwidth=0.463)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#ffffff")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label_update_employee = tk.Label(self.Frame2)
        self.Label_update_employee.place(relx=0.126, rely=0.033, height=106, width=422)
        self.Label_update_employee.configure(activebackground="#f9f9f9")
        self.Label_update_employee.configure(background="#ffffff")
        self.Label_update_employee.configure(compound='left')
        self.Label_update_employee.configure(disabledforeground="#a3a3a3")
        self.Label_update_employee.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.Label_update_employee.configure(foreground="#000000")
        self.Label_update_employee.configure(highlightbackground="#d9d9d9")
        self.Label_update_employee.configure(highlightcolor="black")
        self.Label_update_employee.configure(text='''Update Employee''')

        self.Label_employee_ID = tk.Label(self.Frame2)
        self.Label_employee_ID.place(relx=0.162, rely=0.231, height=26, width=112)
        self.Label_employee_ID.configure(activebackground="#f9f9f9")
        self.Label_employee_ID.configure(anchor='w')
        self.Label_employee_ID.configure(background="#ffffff")
        self.Label_employee_ID.configure(compound='left')
        self.Label_employee_ID.configure(disabledforeground="#a3a3a3")
        self.Label_employee_ID.configure(font="-family {Segoe UI} -size 9")
        self.Label_employee_ID.configure(foreground="#000000")
        self.Label_employee_ID.configure(highlightbackground="#d9d9d9")
        self.Label_employee_ID.configure(highlightcolor="black")
        self.Label_employee_ID.configure(text='''Employee's ID''')


 
        # Dropdown menu options
        options_employee_ID = []

        self.Entry_employee_ID = ttk.Combobox(self.Frame2, values = options_employee_ID)
        self.Entry_employee_ID.place(relx=0.162, rely=0.298, height=34, relwidth=0.655)
        self.Entry_employee_ID.set('')
        

        self.Label_status = tk.Label(self.Frame2)
        self.Label_status.place(relx=0.162, rely=0.396, height=26, width=62)
        self.Label_status.configure(activebackground="#f9f9f9")
        self.Label_status.configure(anchor='w')
        self.Label_status.configure(background="#ffffff")
        self.Label_status.configure(compound='left')
        self.Label_status.configure(disabledforeground="#a3a3a3")
        self.Label_status.configure(foreground="#000000")
        self.Label_status.configure(highlightbackground="#d9d9d9")
        self.Label_status.configure(highlightcolor="black")
        self.Label_status.configure(text='''Status''')


        # Dropdown menu options
        options_status = ['Active', 'Fired']

        self.Entry_status = ttk.Combobox(self.Frame2, values = options_status)
        self.Entry_status.place(relx=0.162, rely=0.462, height=34, relwidth=0.655)
        self.Entry_status.set("")
        

        self.Label_station_ID = tk.Label(self.Frame2)
        self.Label_station_ID.place(relx=0.162, rely=0.558, height=26, width=92)
        self.Label_station_ID.configure(activebackground="#f9f9f9")
        self.Label_station_ID.configure(anchor='w')
        self.Label_station_ID.configure(background="#ffffff")
        self.Label_station_ID.configure(compound='left')
        self.Label_station_ID.configure(disabledforeground="#a3a3a3")
        self.Label_station_ID.configure(font="-family {Segoe UI} -size 9")
        self.Label_station_ID.configure(foreground="#000000")
        self.Label_station_ID.configure(highlightbackground="#d9d9d9")
        self.Label_station_ID.configure(highlightcolor="black")
        self.Label_station_ID.configure(text='''Station's ID''')


        # Dropdown menu options
        options_station_ID = []
        for station in Station.All_station_list:
            options_station_ID.append(station)


        self.Entry_station_ID = ttk.Combobox(self.Frame2, values = options_station_ID)
        self.Entry_station_ID.place(relx=0.162, rely=0.624, height=34, relwidth=0.655)
        self.Entry_station_ID.set('')


        self.Button_update = tk.Button(self.Frame2)
        self.Button_update.place(relx=0.234, rely=0.81, height=53, width=96)
        self.Button_update.configure(activebackground="beige")
        self.Button_update.configure(activeforeground="#000000")
        self.Button_update.configure(background="#44c9b0")
        self.Button_update.configure(compound='left')
        self.Button_update.configure(disabledforeground="#a3a3a3")
        self.Button_update.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Button_update.configure(foreground="#ffffff")
        self.Button_update.configure(highlightbackground="#d9d9d9")
        self.Button_update.configure(highlightcolor="black")
        self.Button_update.configure(pady="0")
        self.Button_update.configure(text='''Update''')
        self.Button_update.configure(command=self.update_employee_btn)
        
        self.Button_cancel = tk.Button(self.Frame2)
        self.Button_cancel.place(relx=0.614, rely=0.81, height=53, width=96)
        self.Button_cancel.configure(activebackground="beige")
        self.Button_cancel.configure(activeforeground="#000000")
        self.Button_cancel.configure(background="#e21e26")
        self.Button_cancel.configure(compound='left')
        self.Button_cancel.configure(disabledforeground="#a3a3a3")
        self.Button_cancel.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Button_cancel.configure(foreground="#ffffff")
        self.Button_cancel.configure(highlightbackground="#d9d9d9")
        self.Button_cancel.configure(highlightcolor="black")
        self.Button_cancel.configure(pady="0")
        self.Button_cancel.configure(text='''Cancel''')
        self.Button_cancel.configure(command=self.cancel_btn)


    def update_employee_btn(self):
        station = self.Entry_station_ID.get()
        employee_username = self.Entry_employee_ID.get()
        status = self.Entry_status.get()
        if station == "" or employee_username == "" or status == "":
            tsmg.showerror('Update Fail','User ID NotFound!') #alert pop-up
        else:
            if (Admin.update_employee(station, employee_username, status)) == None:
                tsmg.showerror('Update Fail','User ID NotFound!') #alert pop-up
            else:
                tsmg.showinfo('Update Complate','Status Change') #alert pop-up

    def cancel_btn(self):
        self.top.destroy()
        all_support.main_administrator_page()
        if __name__ == '__main__':
            all_support.main_administrator_page()



def start_up():
    all_support.main_update_employee_page()

if __name__ == '__main__':
    all_support.main_update_employee_page()



