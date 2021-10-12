# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 00:27:23 2021

@author: Prisha
"""

import tkinter as tk
from tkinter import messagebox


#import pymysql,os
import pymysql
from tkinter_sql import Database

from datetime import date
from datetime import datetime  
import pywhatkit as kit
    
obj_sql= Database()


"""
obj_sql.createtable("create table registration_detail(name varchar(20), \
               userid varchar(20),pwd varchar(15), email varchar(30),\
               address varchar(100), ph varchar(20))")


obj_sql.createtable("create table products(pid int, \
               pname varchar(20),price int)") 

   
obj_sql.createtable("create table order_detail(order_id int, \
               order_date varchar(20),userid varchar(20),ph varchar(20), p_id int,\
                   pname varchar(20), qty int,price varchar(10), bill varchar(10))") 


    
""" 

class Register():
    
    
    
    def __init__(self):
        self.reg_status = False
        self.customer_id=0
        self.bill= 0
        self.order_count=0
        
    def __finalProcessing(self,cname,ph_value, root):

        print("in final processing")
        root.destroy()
        msg= "You have got the order from " + cname+"."
            
        now = str(datetime.now()).split(" ")[1][0:8]
        hour = int(now[0:2])
        minute= int(now[3:5])
        print(hour,minute,ph_value,cname, "hi")    
        kit.sendwhatmsg("+12039280015", msg,hour,minute+2)
#           kit.sendwhatmsg(ph_value, "Order Confirmed",hour,minute+2)
        kit.sendwhatmsg(ph_value, "Order Confirmed",hour,minute+3)
        
        print("Whatsapp Message sent")
        
        
    def __displayBill(self,userid, root):
            
        print("in display bill ")
        root.destroy()
        cust= obj_sql.getphone(userid)
        cname= cust[0][0]
        ph_value= cust[0][5]
        self.displayBillForm(cname,ph_value)
            
 
    def __calculate_bill(self,li,qty0,qty1,qty2,qty3, qty4, qty5, qty6, qty7, qty8, qty9, userid, input_qty,input_bill,root):

        qty_list= [qty0, qty1,qty2,qty3, qty4, qty5, qty6, qty7, qty8, qty9]
        
        count=0 
        for item in qty_list:
            if item  != "":
                count +=1
                
        if count+ self.order_count <=10:         
        
            for i in range(0,10): 
                item_name= li[i][1]
                product= obj_sql.getpid(item_name)
                pid_value= product[0][0]
                cust =obj_sql.getphone(userid)
                ph_value= cust[0][5]
                cname= cust[0][0]
    
                running_bill = 0
                
                if qty_list[i] != "" :
                    running_bill=int(qty_list[i])* int(li[i][2])
                    price= "$" + str(li[i][2])
                        
                    self.bill += running_bill
                    self.order_count += 1
                    input_qty[i].delete(0,4)
                    input_qty[i].insert(0,"")
                    input_bill.delete(0,4)
                    input_bill.insert(0,str(self.bill) )               
                    today_date= str(date.today())
                        
                    print("hello", pid_value,ph_value)
                    print(item_name,qty_list[i], self.customer_id ,running_bill , self.order_count)
                    obj_sql.insertorderrecord(self.customer_id,today_date,userid,ph_value, pid_value,item_name, int(qty_list[i]), price,"$"+str(running_bill))

            messagebox.showwarning("Order Placed","Success!!! Thank You!!!") 
        
            if self.order_count ==10:
                messagebox.showwarning("Order Limit(10) Reached" ,"For placing  more orders, Login again!! Thank You!! ")
                root.destroy()
                self.displayBillForm(cname,ph_value)
        
        
                  
        else:
           
           for i in range(0,10):
               input_qty[i].delete(0,4)
               input_qty[i].insert(0,"")
        
        
#           input_bill.delete(0,4)
#          input_bill.insert(0,"" )       
           messagebox.showwarning("Over Order Limit (10)" ," Please Select fewer items again ")             
                         
            

  
    def __validate(self,userid, pwd,cpwd,name,email,add,ph,root):
        
#        while self.reg_status == False:
            
        print(userid, pwd,cpwd, name,email,add,ph)
            
        if not(userid.isalnum() and userid[0].isupper() and len(userid)>=8 ):
            self.reg_status= False
            messagebox.showwarning("Invalid userid","Enter any alphanumeric string with min length of 8 and First letter capital.")
        else:
            self.reg_status= True
                
                
        if self.reg_status == True:
                
            if not(pwd.isalnum() and cpwd.isalnum() and len(pwd) <=10 and pwd==cpwd ):
                self.reg_status= False
                messagebox.showwarning("Invalid password","Enter any alphanumeric string withmax length of 10 and both pwd should match")    
            else:
                self.reg_status= True
                
            
        if self.reg_status== True :
             messagebox.showwarning("Success","Registration completed")
             obj_sql.insertregrecord(userid, pwd,name,email,add,ph)
             root.destroy()
             self.displayLoginForm()


    def __validateuser(self, userid,pwd,root):
        print("hi",userid,pwd )
        li=obj_sql.showrecord("registration_detail",userid )        
        
        print(li)
        for item in li:
            if item[1]==userid :
                if item[2]== pwd:
                    messagebox.showwarning("Completed","Login Successful")                    
                    root.destroy()
                    self.customer_id +=1
                    self.order_count=0
                    self.bill=0
                    self.displayOrderForm(userid)
                    return
                    
        messagebox.showwarning("InComplete","Login Failed")    





    def displayBillForm(self, cname, ph_value):
        root=tk.Tk()
        root.title("BILLING")
        root.geometry("500x400")
        root.resizable(False, False) 
        
        
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):                
                root.destroy()
                

        root.protocol("WM_DELETE_WINDOW", on_closing)          
                
        tk.Label(root,text="Thank you "+cname+"!!!", bg="blue", width="30", height="2", font=("Calibri", 12)).grid(row=1, column=1) 
        
        
        tk.Label(root,text="Your Bill is $" +str(self.bill), bg="blue", width="30", height="2", font=("Calibri", 12)).grid(row=2, column=1) 
       
 
 
        tk.Button(root, text="Pay the Bill", height="1", width="20",command=lambda: self.__finalProcessing(cname,ph_value,root)).grid(row=7, column=2)
      
 
        root.mainloop()
        


    def displayOrderForm(self, userid):
        
        
        
        root=tk.Tk()
        root.title("Orders")
        root.geometry("600x600")
        root.resizable(False, False) 
        
        
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
#                obj_sql.delorderrecord(self.customer_id)                   
                root.destroy()
                

        root.protocol("WM_DELETE_WINDOW", on_closing)          
        
        
        tk.Label(root, text="SELECT THE FOOD ITEM",justify='left',width=30,\
             font=('bold',12), bg='blue', height=2 ).grid(row=1, column=1)        
    
        
            
        tk.Label( text=" ").pack()
        
        li=obj_sql.showrecord("products","" )
        
        var = tk.StringVar()
        var.set("")
        
        var1 = tk.StringVar()
        var1.set("")
  
        
        
        print(li)
        row_index=3
        index1=0
        
        input_FN = []
        
        for item in li:
            tk.Label(root, text=item[1] +" $"+ str(item[2]),justify='left', width=30).grid(row=row_index, column=1)
            input_FN.append( tk.Entry(root, width=30))
            input_FN[index1].grid(row=row_index, column=2, padx = 5, pady = 5)
            row_index += 2
            index1 +=1
            

        tk.Label(root, text="Bill ($):",justify='left',width=30, height=2, bg='blue').grid(row=36, column=1)
        input_bill= tk.Entry(root, width=30,textvariable=var1)
        
        
        
        button_porder = tk.Button(root,text = "Place Order",justify='center',width=30,height=2,bg='green',\
                command=lambda: self.__calculate_bill(li, input_FN[0].get(),input_FN[1].get(),input_FN[2].get(),\
                                                      input_FN[3].get(),input_FN[4].get(),input_FN[5].get(), \
                                                      input_FN[6].get(), input_FN[7].get(), input_FN[8].get(),\
                                                      input_FN[9].get(),userid,input_FN,input_bill,root))
                                                                                                                     
        button_porder.grid(row= 34, column= 2)
        
        input_bill.grid(row=36, column=2,ipadx = 5, pady = 5)
        
        button_finish = tk.Button(root,text = "Finish ",justify='center',width=30,height=2,bg='green',\
                command=lambda: self.__displayBill(userid,root))
                                                                                                                     
        button_finish.grid(row= 40, column= 2)


                    

        root.mainloop()


 
    def displayLoginForm(self):
        
        
        
        
        root=tk.Tk()
        root.title("Login Form")
        root.geometry("500x300")
        root.resizable(False, False)
        
                
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()
                

        root.protocol("WM_DELETE_WINDOW", on_closing)

        tk.Label(root, text="User-ID",justify='left',width=30, height=2).grid(row=10, column=1)
        input_Userid= tk.Entry(root, width=30)
        input_Userid.grid(row=10, column=2,padx = 5, pady = 5)
        
        tk.Label(text="").pack() 
        
        tk.Label(root, text="Password",justify='left',width=30,height=2).grid(row=13, column=1)
        input_Pwd= tk.Entry(root, width=30, show ="*")
        input_Pwd.grid(row=13, column=2, padx = 5, pady = 5)
                
        tk.Label(text="").pack() 
        

        
        Login = tk.Button(root,text = "Login",justify='center',width=20,height=2,bg='green',\
                command=lambda: self.__validateuser(input_Userid.get(), input_Pwd.get(), root ))
                                                                                                                     
        Login.grid(row=20, column=2)
        
     
        root.mainloop()
        
    
    def displayForm(self):
        
                
        root=tk.Tk()
        root.title("Registration Form")
        root.geometry("750x500")
        root.resizable(False, False)
        
        

        
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_closing)

    
        
        tk.Label(root, text="First Name",justify='left', width=30).grid(row=1, column=1)
        input_FN = tk.Entry(root, width=40)
        input_FN.grid(row=1, column=2, padx = 5, pady = 5)
        
        tk.Label(root, text="Last Name",justify='left', width=30).grid(row=2, column=1)
        input_LN = tk.Entry(root, width=40)
        input_LN.grid(row=2, column=2, padx = 5, pady = 5)
        
        
        tk.Label(root, text="User-ID",justify='left',width=30).grid(row=3, column=1)
        input_Userid= tk.Entry(root, width=40)
        input_Userid.grid(row=3, column=2, padx = 5, pady = 5)
        
       
        tk.Label(root, text="Password",justify='left',width=30).grid(row=4, column=1)
        input_Pwd= tk.Entry(root, width=40, show ="*")
        input_Pwd.grid(row=4, column=2, padx = 5, pady = 5)
        
        
        tk.Label(root, text="Confirm Password",justify='left',width=30).grid(row=5, column=1)
        input_CPwd= tk.Entry(root, width=40, show ="*")
        input_CPwd.grid(row=5, column=2, padx = 5, pady = 5)
        
        tk.Label(root, text="Email-ID",justify='left', width=30).grid(row=6, column=1)
        input_Email = tk.Entry(root, width=40)
        input_Email.grid(row=6, column=2, padx = 5, pady = 5)
        
        tk.Label(root, text="Address Details:",justify='left',width=30,font=('Bold',12)).grid(row=7, column=1)
        tk.Label(text="").pack() 
        
        
        tk.Label(root, text="Apartment no. and Steet",justify='left',width=30).grid(row=8, column=1)
        input_Add= tk.Entry(root, width=40)
        input_Add.grid(row=8, column=2, padx = 5, pady = 5)


        tk.Label(root, text="City",justify='left',width=30).grid(row=9, column=1)
        input_City= tk.Entry(root, width=40)
        input_City.grid(row=9, column=2, padx = 5, pady = 5)

        tk.Label(root, text="State",justify='left',width=30).grid(row=10, column=1)
        input_St= tk.Entry(root, width=40)
        input_St.grid(row=10, column=2, padx = 5, pady = 5)
        
        tk.Label(root, text="Country",justify='left',width=30).grid(row=11, column=1)
        input_Ct= tk.Entry(root, width=40)
        input_Ct.grid(row=11, column=2, padx = 5, pady = 5)        

        ph_label= tk.Label(root, text="Phone No.",justify='left', width=10)
        cc_label= tk.Label(root, text="Country Code",justify='left', width=30)
        
        
        input_Cc= tk.Entry(root, width=20, justify='left')
        input_Ph = tk.Entry(root, width=20, justify='left')
        

        cc_label.grid(row =12, column=1,padx = 2, pady =5)

        input_Cc.grid(row= 12,column=2)

        ph_label.grid(row= 12, column=3,padx = 2, pady = 5)
        input_Ph.grid(row=12, column=4)    


        submit = tk.Button(root,text = "Submit",justify='center',width=30,height=2,bg='green',\
                command=lambda: self.__validate(input_Userid.get(), input_Pwd.get(), input_CPwd.get(),\
                input_FN.get()+" "+input_LN.get(), input_Email.get(),input_Add.get()+", "+input_City.get()+\
                ", " +input_St.get()+ ", "+  input_Ct.get() , input_Cc.get()+ input_Ph.get()  ,root      ))
                                                                                                                     
        submit.grid(row=40, column=2, padx= 5 , pady=5)
        
        
 

        root.mainloop()
        
        
  

