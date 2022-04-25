from tkinter import *
from Agent import *

# create obj here
root = Tk()
root.geometry("400x400")
root.option_add("*Font", "consolas 20")
root.title("Property Manageing Program")
root.geometry("700x400")

#TODO create window have 2 button 1.Create Agent 2.Select Agent
photo = PhotoImage(file="assert/bropng.png")
main_label = Label(root, text="Property Managment Program", fg="red").pack(pady= 30)
create_agent_btn = Button(root, text="Create Agent", image=photo, compound=LEFT).pack(side=TOP, pady=30)
select_agent_btn = Button(root, text="Select Agent").pack()


root.mainloop()