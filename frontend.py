# Created on 28/5/2018

from tkinter import *
import backend


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backend.search(title.get(), author.get(), year.get(), isbn.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(title.get(), author.get(), year.get(), isbn.get())
    list1.delete(0, END)
    list1.insert(END,(title.get() , author.get(), year.get(), isbn.get()))


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0], title.get(), author.get(), year.get(), isbn.get())

# window with icon and title
window = Tk()
window.title("BookStore")
window.iconbitmap("Book.ico")

# lable widget declaration
l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = Label(window, text='Author')
l2.grid(row=0, column=2)

l3 = Label(window, text='Year')
l3.grid(row=1, column=0)

l4 = Label(window, text='ISBN')
l4.grid(row=1, column=2)

# entry widget declaration
title = StringVar()
e1 = Entry(window, textvariable=title)
e1.grid(row=0, column=1)

author = StringVar()
e2 = Entry(window, textvariable=author, width=25)
e2.grid(row=0, column=3)

year = StringVar()
e3 = Entry(window, textvariable=year)
e3.grid(row=1, column=1)

isbn = StringVar()
e4 = Entry(window, textvariable=isbn, width=25)
e4.grid(row=1, column=3)

# list box declaration
list1 = Listbox(window, height=8, width=40)
list1.grid(row=2, column=0, rowspan=5, columnspan=2)

# scrollbar declaration both horizontal and vertical for listbox
v_bar = Scrollbar(window, orient='vertical')
v_bar.grid(row=2, column=2, rowspan=6)

h_bar = Scrollbar(window, orient='horizontal')
h_bar.grid(row=7, column=0, columnspan=2)

# configuring scrollbar & event handler
list1.configure(yscrollcommand=v_bar.set, xscrollcommand=h_bar.set)
v_bar.configure(command=list1.yview)
h_bar.configure(command=list1.xview)
list1.bind('<<ListboxSelect>>', get_selected_row)

# button declaration
b1 = Button(window, text="View All", width=25, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=25, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=25, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update Selected", width=25, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Selected", width=25, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=25, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()  # run mainloop
