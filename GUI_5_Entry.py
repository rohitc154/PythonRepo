from tkinter import *

def getval():
    global v1, v2
    v1 = val1.get()
    v2 = val2.get()
    print(v1)
    print(v2)
    print("Information is Submitted!")


root = Tk()
root.geometry("700x500")

root.title("Login Page")

val1 = StringVar()
val2 = StringVar()

lab1 = Label(root,text="Enter Username : ").grid()
lab2 = Label(root,text="Enter Password : ").grid(row=1,column=0)

uentry = Entry(root,textvariable=val1).grid(row=0,column=1)
upwd = Entry(root,textvariable=val2).grid(row=1,column=1)

B1 = Button(root,text="Submit",command=getval).grid(row=2)
B2 = Button(root,text="Exit",command=root.destroy).grid(row=2,column=1)

root.mainloop()

f1 = open("gtest.txt","w")
f1.writelines(f"Username : {v1}, Password : {v2}\n")
f1.close()

f1 = open("gtest.txt","r")
text = f1.read()
for txt in text:
    print(txt,end="")