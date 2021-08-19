
# Object Oriented Programming Language
import calendar

class Demo:
    
    y=2021
    m=6
    
    def display(self):
        print(calendar.month(self.y,self.m))
        
        
class DemoName:

    name= "poonam"      
    x=0
    
    def displayreverse(self,p):
        self.name=p
        print(self.name[::-1])
        
    def displayeven(self,p):
        self.x =p
        for i in range(1,self.x):
            print(i)
        



class CarDemo:
   
    wheels=4
    brake=1
    
    def moving(self):
         print("car can move using",self.wheels, "wheels")

    def tostop(self):
        print("car can stop using",self.brake,"brakes")
        
        
        
        
""" 
Demo class Misc is having five methods

Method 1 - takes dic and returns li
Method 2 - takes list and returns dic
Method 3 - generators
method 4 : list comprehension
method 5 : dic comprehension


"""       
        
class Misc:
    
    def __init__(self, path):
        self.path=path
        print(self.path)        
        
    def method1(self,dic):
        
        li_k=[k for k in dic.keys()]
        li_v=[v for v in dic.values()]
        
#        dic[1]=99
        yield li_k
        yield li_v
        
        
        
    def method2(self,li1,li2):
        dic={k:v for k,v in zip(li1,li2)}
        dic1= dict(zip(li1,li2))
        yield dic
        yield dic1
        
        
    def method3(self,path, option):


        f=open(path,'r')        
        lines=f.readlines()
        for i in lines:
            print(i)
        print(path,"option->", option)        
                
        if int(option) == 1:
            no_rec_found=0
            print("hello")
            city=input("Please enter city")
            for line in lines:
                words=line.split("|")
                for word in words:
                    if word[0:3].lower()==city[0:3].lower():
                        no_rec_found +=1
                        yield line
        
            if no_rec_found ==0:
                print("Sorry: No record found in this city")
                    
            
        elif int(option) == 2:
            no_rec_found=0
            str_ch=input("Please enter the starting character")
            for line in lines:
                if line is not "":
                    words=line.split("|")
                    if words[1].upper().startswith(str_ch) or \
                        words[1].lower().startswith(str_ch) :
                            no_rec_found +=1
                            yield line
                
            if no_rec_found ==0:
                print("Sorry: No record found with this starting character")
                            
            
            
            
    
        f.close()
        
        
        
        
        
        
        
        
        
        
        
        
        