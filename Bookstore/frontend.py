from tkinter import *
from backend import Database

database=Database("books.db")

def get_selected_row(event):
    global selected_tuple
    if len(booklist.curselection())>0:
        index=booklist.curselection()[0]
        selected_tuple=booklist.get(index)
        titleDisplay.delete(0,END)
        titleDisplay.insert(END,selected_tuple[1])
        authorDisplay.delete(0,END)
        authorDisplay.insert(END,selected_tuple[2])
        yearDisplay.delete(0,END)
        yearDisplay.insert(END,selected_tuple[3])
        isbnDisplay.delete(0,END)
        isbnDisplay.insert(END,selected_tuple[4])

def view_command():
    booklist.delete(0,END)
    for row in database.view():
        booklist.insert(END,row)

def search_command():
    booklist.delete(0,END)
    for row in database.search(titleText.get(),authorText.get(),yearText.get(),isbnText.get()):
        booklist.insert(END,row)

def add_command():
    database.insert(titleText.get(),authorText.get(),yearText.get(),isbnText.get())
    booklist.delete(0,END)
    booklist.insert(END,("#",titleText.get(),authorText.get(),yearText.get(),isbnText.get()))


def update_command():
    database.update(selected_tuple[0],titleText.get(),authorText.get(),yearText.get(),isbnText.get())
    view_command()

def delete_command():
    database.delete(selected_tuple[0])
    view_command()

window=Tk()
window
window.minsize(width=400,height=200)
window.wm_title("BookStore")

title=Label(window,text="Title")
title.grid(row=0,column=0)
titleText=StringVar()
titleDisplay=Entry(window,textvariable=titleText)
titleDisplay.grid(row=0,column=1)

author=Label(window,text="Author")
author.grid(row=0,column=2)
authorText=StringVar()
authorDisplay=Entry(window,textvariable=authorText)
authorDisplay.grid(row=0,column=3)

year=Label(window,text="Year")
year.grid(row=1,column=0)
yearText=StringVar()
yearDisplay=Entry(window,textvariable=yearText)
yearDisplay.grid(row=1,column=1)

isbn=Label(window,text="ISBN")
isbn.grid(row=1,column=2)
isbnText=StringVar()
isbnDisplay=Entry(window,textvariable=isbnText)
isbnDisplay.grid(row=1,column=3)

booklist=Listbox(window,height=6,width=40)
booklist.grid(row=2,column=0,rowspan=6,columnspan=2)

scrollbar=Scrollbar(window)
scrollbar.grid(row=2,column=2,rowspan=6)

booklist.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=booklist.yview)

booklist.bind('<<ListboxSelect>>',get_selected_row)

viewbutton=Button(window,text="View All",width=12,command=view_command)
viewbutton.grid(row=2,column=3)
searchbutton=Button(window,text="Search entry",width=12,command=search_command)
searchbutton.grid(row=3,column=3)
addbutton=Button(window,text="Add entry",width=12,command=add_command)
addbutton.grid(row=4,column=3)
updatebutton=Button(window,text="Update",width=12,command=update_command)
updatebutton.grid(row=5,column=3)
deletebutton=Button(window,text="Delete",width=12,command=delete_command)
deletebutton.grid(row=6,column=3)
closebutton=Button(window,text="Close",width=12,command=window.destroy)
closebutton.grid(row=7,column=3)


window.mainloop()
