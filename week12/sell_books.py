from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msg

### EVENT HANDLERS ###

### CREATE WINDOW ###
window = Tk()
window.title('Book Store')
window.geometry('500x250')

### CREATE WIDGETS ###
lbl_books = Label(window, text='Books')
lbl_books.grid(row=0, column=0, sticky=W, padx=10)

lst_books = Listbox(window, height=5, selectmode=SINGLE)
lst_books.grid(row=1, column=0, columnspan=2, rowspan=3, sticky=W, padx=10)

lbl_name = Label(window, text='Name')
lbl_name.grid(row=1, column=3, sticky=W)

txt_name = Entry(window, width=20)
txt_name.grid(row=1, column=4, columnspan=2, sticky=W)

lbl_author = Label(window, text='Author')
lbl_author.grid(row=2, column=3, sticky=W)

txt_author = Entry(window, width=20)
txt_author.grid(row=2, column=4, columnspan=2, sticky=W)

lbl_price = Label(window, text='Price')
lbl_price.grid(row=3, column=3, sticky=W)

txt_price = Entry(window, width=20)
txt_price.grid(row=3, column=4, columnspan=2, sticky=W)

lbl_quantity = Label(window, text='Quantity')
lbl_quantity.grid(row=4, column=0, sticky=W, padx=10)

txt_quantity = Entry(window, width=10)
txt_quantity.grid(row=4, column=1, sticky=W)

lbl_delivery = Label(window, text='Delivery', padx=10)
lbl_delivery.grid(row=5, column=0, sticky=W)

cbb_delivery = Combobox(window, width=10)
cbb_delivery['values'] = ('Standard', 'Fast', 'Express')
cbb_delivery.grid(row=5, column=1, sticky=W)

lbl_cover = Label(window, text='Cover')
lbl_cover.grid(row=5, column=3, sticky=W)

rd_cover_yes = Radiobutton(window, text='Yes', value='Yes')
rd_cover_yes.grid(row=5, column=4, sticky=W)

rd_cover_no = Radiobutton(window, text='No', value='No')
rd_cover_no.grid(row=5, column=5, sticky=W)

btn_ok = Button(window, text='OK', width=5)
btn_ok.grid(row=6, column=4, sticky=W)

btn_cancel = Button(window, text='Cancel', width=5)
btn_cancel.grid(row=6, column=5, sticky=W)
### START THE GUI ###
window.mainloop()