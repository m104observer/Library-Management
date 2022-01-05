from tkinter import *
from tkinter import messagebox
import library_backend

#===========================================FUNCTION DECLARATIONS=====================================
def exit_command():
    exit_message = messagebox.askyesno("Library Management Systems", "Confirm if you want to exit")
    if exit_message > 0:
        root.destroy()
        return



def clear_data_command():

    member_type_entry.delete(0, END)
    reference_no_entry.delete(0, END)
    title_entry.delete(0, END)
    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    address_1_entry.delete(0, END)
    address_2_entry.delete(0, END)
    zipcode_entry.delete(0, END)
    mobile_entry.delete(0, END)
    book_id_entry.delete(0, END)
    book_title_entry.delete(0, END)
    author_entry.delete(0, END)
    date_borrowed_entry.delete(0, END)
    date_due_entry.delete(0, END)
    days_on_loan_entry.delete(0, END)
    late_return_fine__entry.delete(0, END)
    date_overdue_entry.delete(0, END)
    selling_price_entry.delete(0, END)


def add_data():
    if member_type.get() == "" or reference_no.get() == "" or title.get() == "" or firstname.get() == "" or lastname.get() == "":
        messagebox.showerror("Required Fields", "Please include all fields")
        return
    library_backend.insert(member_type.get(), reference_no.get(), title.get(), firstname.get(), lastname.get(),address_1.get(), address_2.get(), zipcode.get(), mobile_no.get(), book_id.get(), book_title.get(), author.get(), date_borrowed.get(), date_due.get(), days_on_loan.get(), late_return_fine.get(), date_due.get(), selling_price.get())
    booklist.delete(0, END)
    booklist.insert(END, (member_type.get(), reference_no.get(), title.get(), firstname.get(), lastname.get(),address_1.get(), address_2.get(), zipcode.get(), mobile_no.get(), book_id.get(), book_title.get(), author.get(), date_borrowed.get(), date_due.get(), days_on_loan.get(), late_return_fine.get(), date_due.get(), selling_price.get()))
    clear_data_command()
    


def display_data():
    booklist.delete(0, END)
    for row in library_backend.view():
        booklist.insert(END, row)


def select_item(event):
    try:
        global selected_tuple
        index = booklist.curselection()[0]
        selected_tuple = booklist.get(index)
        member_type_entry.delete(0, END)
        member_type_entry.insert(END, selected_tuple[1])
        reference_no_entry.delete(0, END)
        reference_no_entry.insert(END, selected_tuple[2])
        title_entry.delete(0, END)
        title_entry.insert(END, selected_tuple[3])
        firstname_entry.delete(0, END)
        firstname_entry.insert(END, selected_tuple[4])
        lastname_entry.delete(0, END)
        lastname_entry.insert(END, selected_tuple[5])
        address_1_entry.delete(0, END)
        address_1_entry.insert(END, selected_tuple[6])
        address_2_entry.delete(0, END)
        address_2_entry.insert(END, selected_tuple[7])
        zipcode_entry.delete(0, END)
        zipcode_entry.insert(END, selected_tuple[8])
        mobile_entry.delete(0, END)
        mobile_entry.insert(END, selected_tuple[9])
        book_id_entry.delete(0, END)
        book_id_entry.insert(END, selected_tuple[10])
        book_title_entry.delete(0, END)
        book_title_entry.insert(END, selected_tuple[11])
        author_entry.delete(0, END)
        author_entry.insert(END, selected_tuple[12])
        date_borrowed_entry.delete(0, END)
        date_borrowed_entry.insert(END, selected_tuple[13])
        date_due_entry.delete(0, END)
        date_due_entry.insert(END, selected_tuple[14])
        days_on_loan_entry.delete(0, END)
        days_on_loan_entry.insert(END, selected_tuple[15])
        late_return_fine__entry.delete(0, END)
        late_return_fine__entry.insert(END, selected_tuple[16])
        date_due_entry.delete(0, END)
        date_due_entry.insert(END, selected_tuple[17])
        selling_price_entry.delete(0, END)
        selling_price_entry.insert(END, selected_tuple[18])
    except IndexError:
        pass

def delete_data():
    library_backend.delete(selected_tuple[0])
    clear_data_command()
    display_data()

def update_data():
    library_backend.update(selected_tuple[0], member_type.get(), reference_no.get(), title.get(), firstname.get(), lastname.get(),address_1.get(), address_2.get(), zipcode.get(), mobile_no.get(), book_id.get(), book_title.get(), author.get(), date_borrowed.get(), date_due.get(), days_on_loan.get(), late_return_fine.get(), date_due.get(), selling_price.get())
    display_data()


def search_data():
    booklist.delete(0, END)
    for row in library_backend.search(member_type.get(), reference_no.get(), title.get(), firstname.get(), lastname.get(),address_1.get(), address_2.get(), zipcode.get(), mobile_no.get(), book_id.get(), book_title.get(), author.get(), date_borrowed.get(), date_due.get(), days_on_loan.get(), late_return_fine.get(), date_due.get(), selling_price.get()):
        booklist.insert(END,row)


root = Tk()
root.title("Library Management Systems")
root.geometry("1350x750+0+0")


#===========================================FRAME==================================================================

main_frame = Frame(root)
main_frame.grid()

title_frame = Frame(main_frame, bd=2, padx=44, pady=8, bg="Cadet Blue", relief=RIDGE)
title_frame.pack(side=TOP)

lbl_title = Label(title_frame, font=("Ubuntu Condensed", 46, "bold"), text="LIBRARY MANAGEMENT SYSTEMS")
lbl_title.grid(sticky=W)

button_frame = Frame(main_frame, bd=2, width=1350, height=100, padx=20, pady=20, bg="Cadet Blue", relief=RIDGE)
button_frame.pack(side=BOTTOM)

frame_detail = Frame(main_frame, bd=0, width=1350, height=50, padx=20, relief=RIDGE)
frame_detail.pack(side=BOTTOM)
        
data_frame = Frame(main_frame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE)
data_frame.pack(side=BOTTOM)

data_frame_left = LabelFrame(data_frame, bd=1, width=800, height=300, padx=20, relief=RIDGE, text="Library Membership Info:", bg="Cadet Blue")
data_frame_left.pack(side=LEFT)
data_frame_right = LabelFrame(data_frame, bd=1, width=450, height=300, padx=20, pady=3, relief=RIDGE, text="Book Details:", bg="Cadet Blue")
data_frame_right.pack(side=RIGHT)



member_type = StringVar()
reference_no = StringVar()
title = StringVar()
firstname = StringVar()
lastname = StringVar()
address_1 = StringVar()
address_2 = StringVar()
zipcode = StringVar()
mobile_no = StringVar()
book_id = StringVar()
book_title = StringVar()
author = StringVar()
date_borrowed = StringVar()
date_due = StringVar()
days_on_loan = StringVar()
late_return_fine = StringVar()
date_over_due = StringVar()
selling_price = StringVar()

#===========================================LABEL AND ENTRY=====================================


        
member_type_lbl = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="Member Type:", padx=2, pady=2, bg="Cadet Blue")
member_type_lbl.grid(row=0, column=0, sticky=W)
member_type_entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=member_type, width=25)
member_type_entry.grid(row=0, column=1)

reference_no_label = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="Reference No:", padx=2, pady=2, bg="Cadet Blue")
reference_no_label.grid(row=1, column=0, sticky=W)
reference_no_entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=reference_no, width=25)
reference_no_entry.grid(row=1, column=1)

title_lbl = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="Title:", padx=2, pady=2, bg="Cadet Blue")
title_lbl.grid(row=2, column=0, sticky=W)
title_entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=title, width=25)
title_entry.grid(row=2, column=1)

firstname_lbl = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="First Name:", padx=2, pady=2, bg="Cadet Blue")
firstname_lbl.grid(row=3, column=0, sticky=W)
firstname_entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=firstname, width=25)
firstname_entry.grid(row=3, column=1)

lastname_lbl = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="Last Name:", padx=2, pady=2, bg="Cadet Blue")
lastname_lbl.grid(row=4, column=0, sticky=W)
lastname_entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=lastname, width=25)
lastname_entry.grid(row=4, column=1)

address_1_lbl = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="Address 1:", padx=2, pady=2, bg="Cadet Blue")
address_1_lbl.grid(row=5, column=0, sticky=W)
address_1_entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=address_1, width=25)
address_1_entry.grid(row=5, column=1)

address_2_lbl = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="Address 2:", padx=2, pady=2, bg="Cadet Blue")
address_2_lbl.grid(row=6, column=0, sticky=W)
address_2_entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=address_2, width=25)
address_2_entry.grid(row=6, column=1)
        
zipcode_lbl = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="Zipcode:", padx=2, pady=2, bg="Cadet Blue")
zipcode_lbl.grid(row=7, column=0, sticky=W)
zipcode_entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=zipcode, width=25)
zipcode_entry.grid(row=7, column=1)

mobile_lbl = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="Telephone No:", padx=2, pady=2, bg="Cadet Blue")
mobile_lbl.grid(row=8, column=0, sticky=W)
mobile_entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=mobile_no, width=25)
mobile_entry.grid(row=8, column=1)
        

book_id_lbl = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="Book ID:", padx=2, pady=2, bg="Cadet Blue")
book_id_lbl.grid(row=0, column=2, sticky=W)
book_id_entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=book_id, width=25)
book_id_entry.grid(row=0, column=3)

book_title_lbl = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="Book Title:", padx=2, pady=2, bg="Cadet Blue")
book_title_lbl.grid(row=1, column=2, sticky=W)
book_title_entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=book_title, width=25)
book_title_entry.grid(row=1, column=3)

author_lbl = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="Author:", padx=2, pady=2, bg="Cadet Blue")
author_lbl.grid(row=2, column=2, sticky=W)
author_entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=author, width=25)
author_entry.grid(row=2, column=3)

date_borrowed_lbl = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="Date Borrowed:", padx=2, pady=2, bg="Cadet Blue")
date_borrowed_lbl.grid(row=3, column=2, sticky=W)
date_borrowed_entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=date_borrowed, width=25)
date_borrowed_entry.grid(row=3, column=3)

date_due_lbl = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="Date Due:", padx=2, pady=2, bg="Cadet Blue")
date_due_lbl.grid(row=4, column=2, sticky=W)
date_due_entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=date_due, width=25)
date_due_entry.grid(row=4, column=3)

days_on_loan_lbl = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="Days on loan:", padx=2, pady=2, bg="Cadet Blue")
days_on_loan_lbl.grid(row=5, column=2, sticky=W)
days_on_loan_entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=days_on_loan, width=25)
days_on_loan_entry.grid(row=5, column=3)

late_return_fine_lbl = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="Late Return Fine:", padx=2, pady=2, bg="Cadet Blue")
late_return_fine_lbl.grid(row=6, column=2, sticky=W)
late_return_fine__entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=late_return_fine, width=25)
late_return_fine__entry.grid(row=6, column=3)

date_overdue_lbl = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="Date over due:", padx=2, pady=2, bg="Cadet Blue")
date_overdue_lbl.grid(row=7, column=2, sticky=W)
date_overdue_entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=date_over_due, width=25)
date_overdue_entry.grid(row=7, column=3)

selling_price_lbl = Label(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), text="Selling Price:", padx=2, pady=2, bg="Cadet Blue")
selling_price_lbl.grid(row=8, column=2, sticky=W)
selling_price_entry = Entry(data_frame_left, font=("Ubuntu Condensed", 12, "bold"), textvariable=selling_price, width=25)
selling_price_entry.grid(row=8, column=3)



#===========================================LISTBOX AND SCROLLBAR=====================================

my_scrollbar = Scrollbar(data_frame_right)
my_scrollbar.grid(row=0, column=1, sticky=NS)

booklist = Listbox(data_frame_right, width=45, height=15, font=("Ubuntu Condensed", 12, "bold"), yscrollcommand=my_scrollbar.set)
booklist.grid(row=0, column=0, padx=8)
my_scrollbar.configure(command=booklist.yview)


booklist.bind('<<ListboxSelect>>', select_item)


    

#===========================================BUTTONS WIDGETS=====================================

add_btn = Button(button_frame, text="Add Data", font=("Ubuntu Condensed", 14, "bold"), width=14, height=2, bd=4,command=add_data)
add_btn.grid(row=0, column=0)

display_btn = Button(button_frame, text="Display Data", font=("Ubuntu Condensed", 14, "bold"), width=14, height=2, bd=4, command=display_data)
display_btn.grid(row=0, column=1)

clear_btn = Button(button_frame, text="Clear Data", font=("Ubuntu Condensed", 14, "bold"), width=14, height=2, bd=4, command=clear_data_command)
clear_btn.grid(row=0, column=2)

delete_btn = Button(button_frame, text="Delete", font=("Ubuntu Condensed", 14, "bold"), width=14, height=2, bd=4, command=delete_data)
delete_btn.grid(row=0, column=3)

update_btn = Button(button_frame, text="Update", font=("Ubuntu Condensed", 14, "bold"), width=14, height=2, bd=4, command=update_data)
update_btn.grid(row=0, column=4)

search_btn = Button(button_frame, text="Search Data", font=("Ubuntu Condensed", 14, "bold"), width=14, height=2, bd=4, command=search_data)
search_btn.grid(row=0, column=5)

exit_btn = Button(button_frame, text="Exit", font=("Ubuntu Condensed", 14, "bold"), width=14, height=2, bd=4, command=exit_command)
exit_btn.grid(row=0, column=6)


root.mainloop()

