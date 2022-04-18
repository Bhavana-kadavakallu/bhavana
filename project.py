# import tkinter
# from tkinter import*

# m=tkinter.Tk()
# m.title("chat box")
# button = tkinter.Button(m,text="start",width=30,command=m.destroy)
# button.pack()
# m.geometry("500x500")
# my_label=Label(m,text="hii").pack()
# if my_label=="hii":
#     print("hello")
# m.mainloop()

 
import tkinter
from tkinter import*
root=Tk()
root.title("chat box")
root.geometry("500x500")

def my_click():
    my_label=Label(root,text="Hii",fg= "#FF6347").grid(row=1,column=0)
    my_label=Label(root,text="How r u",fg="#FF6347").grid(row=2,column=0)

button = tkinter.Button(root,text="start",width=30,command=my_click,fg="red",bg="green").grid(row=0,column=0)

root.mainloop()