from tkinter import *
from main import *


def btn_save_customer_info():
    temp_cust = add_customer(entry_login.get(), entry_password.get(), entry_name.get(),
                             entry_surname.get(), entry_age.get(), entry_email.get())
    customersListbox.insert(END, temp_cust)
    entry_login.delete(0, END)
    entry_password.delete(0, END)
    entry_name.delete(0, END)
    entry_surname.delete(0, END)
    entry_age.delete(0, END)
    entry_email.delete(0, END)


def btn_save_hall_info():
    temp_hall = add_hall(entry_hall_name.get(), entry_eco.get(), entry_comf.get(), entry_vip.get())
    hallsListbox.insert(END, temp_hall)
    entry_hall_name.delete(0, END)
    entry_eco.delete(0, END)
    entry_comf.delete(0, END)
    entry_vip.delete(0, END)


def btn_save_cinema_info():
    temp_cin = add_cinema(entry_film_name.get(), entry_sch_time.get(), entry_cinema_hall.get())
    cinemasListbox.insert(END, temp_cin)
    entry_film_name.delete(0, END)
    entry_sch_time.delete(0, END)
    entry_cinema_hall.delete(0, END)


def change_to_main():
    global prev_frame
    main_frame.pack(fill='both', expand=1)
    prev_frame.pack_forget()
    prev_frame = main_frame


def change_to_customer_register():
    global prev_frame
    customer_register.pack(fill='both', expand=1)
    if prev_frame != 0:
        prev_frame.pack_forget()
    prev_frame = customer_register


def change_to_hall_register():
    global prev_frame
    hall_register.pack(fill='both', expand=1)
    if prev_frame != 0:
        prev_frame.pack_forget()
    prev_frame = hall_register


def change_to_cinema_register():
    global prev_frame
    cinema_register.pack(fill='both', expand=1)
    if prev_frame != 0:
        prev_frame.pack_forget()
    prev_frame = cinema_register


win = Tk()
win.title('Cinema Theatre')
win.geometry('640x480')

main_frame = Frame(win)
customer_register = Frame(win)
hall_register = Frame(win)
cinema_register = Frame(win)

# CUSTOMER REGISTER FRAME - START
lbl_login = Label(customer_register, text='Login')
entry_login = Entry(customer_register)

lbl_login.pack()
entry_login.pack()

lbl_password = Label(customer_register, text='Password')
entry_password = Entry(customer_register, show='*')

lbl_password.pack()
entry_password.pack()

lbl_name = Label(customer_register, text='Name')
entry_name = Entry(customer_register)

lbl_name.pack()
entry_name.pack()

lbl_surname = Label(customer_register, text='Surname')
entry_surname = Entry(customer_register)

lbl_surname.pack()
entry_surname.pack()

lbl_age = Label(customer_register, text='Age')
entry_age = Entry(customer_register)

lbl_age.pack()
entry_age.pack()

lbl_email = Label(customer_register, text='Email')
entry_email = Entry(customer_register)

lbl_email.pack()
entry_email.pack()

save_cust_btn = Button(customer_register, text='save', command=lambda: btn_save_customer_info())
save_cust_btn.pack()

customersListbox = Listbox(customer_register, width=100, height=5)
customersListbox.pack()

main_btn = Button(customer_register, text='back to main page', command=lambda: change_to_main())
main_btn.pack(anchor=NW)
# CUSTOMER REGISTER FRAME - END

# HALL REGISTER FRAME - START
lbl_hall_name = Label(hall_register, text='Hall name')
entry_hall_name = Entry(hall_register)

lbl_hall_name.pack()
entry_hall_name.pack()

lbl_eco = Label(hall_register, text='Economy places')
entry_eco = Entry(hall_register)

lbl_eco.pack()
entry_eco.pack()

lbl_comf = Label(hall_register, text='Comfort places')
entry_comf = Entry(hall_register)

lbl_comf.pack()
entry_comf.pack()

lbl_vip = Label(hall_register, text='VIP places')
entry_vip = Entry(hall_register)

lbl_vip.pack()
entry_vip.pack()

save_hall_btn = Button(hall_register, text='save', command=lambda: btn_save_hall_info())
save_hall_btn.pack()

hallsListbox = Listbox(hall_register, width=100, height=5)
hallsListbox.pack()

main_btn = Button(hall_register, text='back to main page', command=lambda: change_to_main())
main_btn.pack(anchor=NW)
# HALL REGISTER FRAME - END

# CINEMA REGISTER FRAME - START
lbl_film_name = Label(cinema_register, text='Film name')
entry_film_name = Entry(cinema_register)

lbl_film_name.pack()
entry_film_name.pack()

lbl_sch_time = Label(cinema_register, text='Scheduled time')
entry_sch_time = Entry(cinema_register)

lbl_sch_time.pack()
entry_sch_time.pack()

lbl_cinema_hall = Label(cinema_register, text='Cinema hall')
entry_cinema_hall = Entry(cinema_register)

lbl_cinema_hall.pack()
entry_cinema_hall.pack()

save_cinema_btn = Button(cinema_register, text='save', command=lambda: btn_save_cinema_info())
save_cinema_btn.pack()

cinemasListbox = Listbox(cinema_register, width=100, height=5)
cinemasListbox.pack()

main_btn = Button(cinema_register, text='back to main page', command=lambda: change_to_main())
main_btn.pack(anchor=NW)
# CINEMA REGISTER FRAME - END

customer_btn = Button(main_frame, text='Customer register', command=lambda: change_to_customer_register())
customer_btn.pack()

hall_btn = Button(main_frame, text='Hall register', command=lambda: change_to_hall_register())
hall_btn.pack()

cin_btn = Button(main_frame, text='Cinema register', command=lambda: change_to_cinema_register())
cin_btn.pack()


main_frame.pack()
prev_frame = main_frame
win.mainloop()

