
"""
changing after moving from LR to WS

"""
"""
Tkinter is the standard GUI library for Python.
 Python when combined with Tkinter provides a fast 
 and easy way to create GUI applications. Tkinter 
 provides a powerful object-oriented interface to the
 Tk GUI toolkit. (Source: Link)
 
 
 tk.label() is used to display text in the GUI window

"""

import tkinter as tk


from tkinter_module import Register

import tkinter_module


root = tk.Tk()
root.title("Desktop Registration Application in python")
root.geometry("300x300")


reg_user=Register()





tk.Label(text="If new user then REGISTER else LOGIN", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
tk.Label(text="").pack() 
 
# create Login Button 
tk.Button(text="Login", height="2", width="30",command=reg_user.displayLoginForm).pack() 
tk.Label(text="").pack() 
 
# create a register button
tk.Button(text="Register", height="2", width="30",command=reg_user.displayForm).pack()
 



"""
button1= tk.Button(root, text='SignUp', width=15,bg='red', command=reg_user.displayForm)
button2= tk.Button(root, text='SignIn', width=15, bg='blue')
button1.grid(row= 1, column= 1)

button2.grid(row= 1, column= 3)
"""



root.mainloop()


