# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 18:56:22 2021

@author: Prisha
"""

#import pymysql, os

import pymysql

class Database:
    
    def __init__(self):
        
        self.conn= pymysql.connect(host="localhost",port=3306 ,user="root",password="poonamsql",db="surya_assignment")
        self.cur  = self.conn.cursor()
    

    def createtable(self,query):
        self.cur.execute(query)
        self.conn.commit()
        
    def getpid(self,pname):
        self.cur.execute("select * from products where pname='{0}'".format(pname)) 
        li= self.cur.fetchall()
#        print(li)
        
        return(li)
        

    def getphone(self,userid):
        self.cur.execute("select * from registration_detail where userid='{0}'".format(userid))
        li= self.cur.fetchall()
#        print(li)
        
        return(li)
        
    def delorderrecord(self,customer_id):
        self.cur.execute("delete from order_detail where order_id={0}".format(customer_id))
        self.conn.commit()
        


    def insertregrecord(self,userid, pwd,name,email,add,ph):

             
        query="insert into registration_detail values('{0}','{1}','{2}','{3}','{4}','{5}')".\
                 format(name,userid,pwd,email,add,ph)
                     

        self.cur.execute(query)
        self.conn.commit()
 

    def insertorderrecord(self,orderid, order_date, userid, ph,pid,pname,qty, price,bill):
        
             
        query="insert into order_detail values({0},'{1}','{2}','{3}',{4},'{5}',{6}, '{7}','{8}')".\
                 format(orderid, order_date, userid, ph,pid,pname,qty, price,bill)
                     

        self.cur.execute(query)
        self.conn.commit()
                     

    def showrecord(self, table_name,uid):
        
        
#        self.cur.execute("select * from {0} where userid={1}".format(table_name, uid))

        self.cur.execute("select * from {0}".format(table_name))
        li= self.cur.fetchall()
        
        return(li)
        

        
    def closeconn(self):
        self.cur.close()
        self.conn.close()
        
