from tkinter import *
import ast

root=Tk()
entry=Entry(root)
entry.grid(row=1,columnspan=6,sticky="ew")

i=0
def button_pressed(num):
    global i
    entry.insert(i,num) 
    i+=1

def get_operator(operator):
    global i
    length=len(operator)
    entry.insert(i,operator)
    i+=length   

def clearall():
    entry.delete(0,END)

def calculate():
    entirestring=entry.get()
    try: 
        node=ast.parse(entirestring,mode="eval")  
        result= eval(compile(node,"<string>",'eval'))  
        clearall()
        entry.insert(0,result)
    except:
        clearall()
        entry.insert(0,"An Error Occured")

def undo():
    entirestring=entry.get()
    if len(entirestring):
        newstring=entirestring[:-1]       
        clearall()
        entry.insert(0,newstring)
    else:
        clearall()
        entry.insert(0,"")

count=1
for x in range(3):
    for y in range(3):
        button=Button(root,text=count,height=4,width=8,highlightbackground="#546979",padx=2,pady=2,command=lambda value=count:button_pressed(value))
        button.grid(row=x+2,column=y)
        count+=1

button=Button(root,text=".",height=4,width=8,highlightbackground="#546979",padx=2,pady=2, command=lambda: button_pressed("."))
button.grid(row=5,column=1)

button=Button(root,text="0",height=4,width=8,highlightbackground="#546979",padx=2,pady=2,command=lambda: button_pressed(0))
button.grid(row=5,column=0)

button=Button(root,text="AC",height=4,width=8,highlightbackground="#546979",padx=2,pady=2,command=clearall)
button.grid(row=2,column=5)
button=Button(root,text="<---",height=4,width=8,highlightbackground="#546979",padx=2,pady=2,command=undo)
button.grid(row=3,column=5)

button=Button(root,text="=",height=4,width=8,highlightbackground="#546979",padx=2,pady=2,command=calculate)
button.grid(row=5,column=2)

oper=['+',"-",'*','/']
for i in range(len(oper)):
    button=Button(root,text=oper[i],height=4,width=8,highlightbackground="#546979",padx=2,pady=2,command= lambda text=oper[i]:get_operator(text))
    button.grid(row=i+2,column=3)

root.mainloop()
