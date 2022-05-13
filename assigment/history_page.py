#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    May 12, 2022 05:02:33 AM +07  platform: Windows NT

import sys

from Backend.customer import Customer
from Backend.package import Package
from Backend.admin import Admin
from Backend.record_package import Record_Package

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import history_page_support

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

        top.geometry("1200x700+310+146")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("E-tracking - History")
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

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.1, rely=0.1, relheight=0.779, relwidth=0.795)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#ffffff")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.game_scroll = ttk.Scrollbar(self.Frame2,orient='vertical')
        self.game_scroll.pack(side=RIGHT, fill=Y)

        self.my_game = ttk.Treeview(self.Frame2,yscrollcommand=self.game_scroll.set)
        self.my_game.place(relx=0.052, rely=0.092, relheight=0.804, relwidth=0.893)
        
        self.game_scroll.config(command=self.my_game.yview)
        self.game_scroll.config(command=self.my_game.xview)
        
        self.my_game['columns'] = ('player_id', 'player_name')

        # format our column
        self.my_game.column("#0", width=0,  stretch=NO)
        self.my_game.column("player_id",anchor=CENTER, width=80,)
        self.my_game.column("player_name",anchor=CENTER,width=0, stretch=NO)
        # self.my_game.column("player_Rank",anchor=CENTER,width=80)
        # self.my_game.column("player_states",anchor=CENTER,width=80)
        # self.my_game.column("player_city",anchor=CENTER,width=80)
        #self.my_game.column("player_power",anchor=CENTER,width=80)

        #Create Headings 
        self.my_game.heading("#0",text="",anchor=CENTER)
        self.my_game.heading("player_id",text="Id",anchor=CENTER)
        self.my_game.heading("player_name",text="Name",anchor=CENTER)
        # self.my_game.heading("player_Rank",text="Rank",anchor=CENTER)
        # self.my_game.heading("player_states",text="States",anchor=CENTER)
        # self.my_game.heading("player_city",text="States",anchor=CENTER)
        #self.my_game.heading("player_power",text="States",anchor=CENTER)

        

        round = 0
        #add data 
        Num_no = 0
        Len_num = 0
        # c = 0
        check = 0
        record_list = []
        for v in record_list:
            for i in v:
                self.my_game.insert(parent='', index='end', iid=round, text="Parent", values=(i, 1, "salie"))
                if check >= 1:
                    self.my_game.move(Num_no, Len_num, '0')
                else:
                    check += 1

                Num_no += 1
                round += 1
            check = 0
            Len_num = Num_no
                    
            
            
            
            
            
            
            
            






            
        # self.my_game.insert(parent='',index='end',iid=2,text='',
        # values=('3','Deamon','103', 'California', 'Placentia', '100'))
        # self.my_game.insert(parent='',index='end',iid=3,text='',
        # values=('4','Dragon','104','New York' , 'White Plains', '100'))
        # self.my_game.insert(parent='',index='end',iid=4,text='',
        # values=('5','CrissCross','105','California', 'San Diego', '100'))
        # self.my_game.insert(parent='',index='end',iid=5,text='',
        # values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY', '100'))
        # self.my_game.insert(parent='',index='end',iid=6,text='',
        # values=('7','RayRizzo','107','Colorado' , 'Denver', '100'))
        # self.my_game.insert(parent='',index='end',iid=7,text='',
        # values=('8','Byun','108','Pennsylvania' , 'ORVISTON', '100'))
        # self.my_game.insert(parent='',index='end',iid=8,text='',
        # values=('9','Trink','109','Ohio' , 'Cleveland', '100'))
        # self.my_game.insert(parent='',index='end',iid=9,text='',
        # values=('10','Twitch','110','Georgia' , 'Duluth', '100'))
        # self.my_game.insert(parent='',index='end',iid=10,text='',
        # values=('11','Animus','111', 'Connecticut' , 'Hartford', '100'))
        # self.my_game.insert(parent='',index='end',iid=11,text='',
        # values=('12','Animus','111', 'Connecticut' , 'Hartford', '100'))
        
        self.Button1 = tk.Button(self.Frame2)
        self.Button1.place(relx=0.43, rely=0.917, height=33, width=136)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''close''')


        self.Entry_employee_ID = tk.Entry(self.Frame2)
        self.Entry_employee_ID.place(relx=0.18, rely=0.678, height=34, relwidth=0.654)
        self.Entry_employee_ID.configure(background="white")
        self.Entry_employee_ID.configure(disabledforeground="#a3a3a3")
        self.Entry_employee_ID.configure(font="TkFixedFont")
        self.Entry_employee_ID.configure(foreground="#000000")
        self.Entry_employee_ID.configure(highlightbackground="#d9d9d9")
        self.Entry_employee_ID.configure(highlightcolor="black")
        self.Entry_employee_ID.configure(insertbackground="black")
        self.Entry_employee_ID.configure(selectbackground="#c4c4c4")
        self.Entry_employee_ID.configure(selectforeground="black")

        self.Button_add = tk.Button(self.Frame2)
        self.Button_add.place(relx=0.460, rely=0.793, height=43, width=76)
        self.Button_add.configure(activebackground="beige")
        self.Button_add.configure(activeforeground="#000000")
        self.Button_add.configure(background="#0080ff")
        self.Button_add.configure(compound='left')
        self.Button_add.configure(disabledforeground="#a3a3a3")
        self.Button_add.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Button_add.configure(foreground="#ffffff")
        self.Button_add.configure(highlightbackground="#d9d9d9")
        self.Button_add.configure(highlightcolor="black")
        self.Button_add.configure(pady="0")
        self.Button_add.configure(text='''Submit''')
        self.Button_add.configure(command=self.add_btn)

    def add_btn(self):
        customer_id = self.Entry_employee_ID.get()
        for i in Customer.All_Customer_list:
            if i.c_id == customer_id:
                print('foo')
                print(i.show_history())
            else:
                print('bar')

def start_up():
    history_page_support.main()

if __name__ == '__main__':
    history_page_support.main()



