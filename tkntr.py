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
    prev_frame.place_forget()
    main_frame.place(x=0, y=0)
    prev_frame = main_frame


def change_to_customer_register():
    global prev_frame
    if prev_frame != 0:
        prev_frame.place_forget()
    customer_register.place(x=0, y=0)
    prev_frame = customer_register


def change_to_hall_register():
    global prev_frame
    if prev_frame != 0:
        prev_frame.place_forget()
    hall_register.place(x=0, y=0)
    prev_frame = hall_register


def change_to_cinema_register():
    global prev_frame
    if prev_frame != 0:
        prev_frame.place_forget()
    cinema_register.place(x=0, y=0)
    prev_frame = cinema_register


win = Tk()
win.title('Cinema Theatre')
win.geometry('500x500')

main_frame = Frame(width=500, height=500)
main_frame.place(x=0, y=0)
customer_register = Frame(width=500, height=500)
hall_register = Frame(width=500, height=500)
cinema_register = Frame(width=500, height=500)

spec_relh = 0.05
spec_relw = 0.3
lbl_relh = 0.04

# CUSTOMER REGISTER FRAME - START
lbl_login = Label(customer_register, text='Login')
entry_login = Entry(customer_register)

lbl_login.place(relx=0.35, rely=0, relheight=lbl_relh, relwidth=spec_relw)
entry_login.place(relx=0.35, rely=0.04, relheight=spec_relh, relwidth=spec_relw)

lbl_password = Label(customer_register, text='Password')
entry_password = Entry(customer_register, show='*')

lbl_password.place(relx=0.35, rely=0.09, relheight=lbl_relh, relwidth=spec_relw)
entry_password.place(relx=0.35, rely=0.13, relheight=spec_relh, relwidth=spec_relw)

lbl_name = Label(customer_register, text='Name')
entry_name = Entry(customer_register)

lbl_name.place(relx=0.35, rely=0.18, relheight=lbl_relh, relwidth=spec_relw)
entry_name.place(relx=0.35, rely=0.22, relheight=spec_relh, relwidth=spec_relw)

lbl_surname = Label(customer_register, text='Surname')
entry_surname = Entry(customer_register)

lbl_surname.place(relx=0.35, rely=0.27, relheight=lbl_relh, relwidth=spec_relw)
entry_surname.place(relx=0.35, rely=0.31, relheight=spec_relh, relwidth=spec_relw)

lbl_age = Label(customer_register, text='Age')
entry_age = Entry(customer_register)

lbl_age.place(relx=0.35, rely=0.36, relheight=lbl_relh, relwidth=spec_relw)
entry_age.place(relx=0.35, rely=0.4, relheight=spec_relh, relwidth=spec_relw)

lbl_email = Label(customer_register, text='Email')
entry_email = Entry(customer_register)

lbl_email.place(relx=0.35, rely=0.45, relheight=lbl_relh, relwidth=spec_relw)
entry_email.place(relx=0.35, rely=0.49, relheight=spec_relh, relwidth=spec_relw)

save_cust_btn = Button(customer_register, text='save', command=lambda: btn_save_customer_info())
save_cust_btn.place(relx=0.35, rely=0.58, relwidth=spec_relw)

customersListbox = Listbox(customer_register)
customersListbox.place(relx=0, rely=0.7, relheight=0.1, relwidth=1)

main_btn = Button(customer_register, text='back to main page', command=lambda: change_to_main())
main_btn.place(relx=0, rely=0.9)
# CUSTOMER REGISTER FRAME - END

# HALL REGISTER FRAME - START
lbl_hall_name = Label(hall_register, text='Hall name')
entry_hall_name = Entry(hall_register)

lbl_hall_name.place(relx=0.35, rely=0.1, relheight=lbl_relh, relwidth=spec_relw)
entry_hall_name.place(relx=0.35, rely=0.14, relheight=spec_relh, relwidth=spec_relw)

lbl_eco = Label(hall_register, text='Economy places')
entry_eco = Entry(hall_register)

lbl_eco.place(relx=0.35, rely=0.19, relheight=lbl_relh, relwidth=spec_relw)
entry_eco.place(relx=0.35, rely=0.23, relheight=spec_relh, relwidth=spec_relw)

lbl_comf = Label(hall_register, text='Comfort places')
entry_comf = Entry(hall_register)

lbl_comf.place(relx=0.35, rely=0.28, relheight=lbl_relh, relwidth=spec_relw)
entry_comf.place(relx=0.35, rely=0.32, relheight=spec_relh, relwidth=spec_relw)

lbl_vip = Label(hall_register, text='VIP places')
entry_vip = Entry(hall_register)

lbl_vip.place(relx=0.35, rely=0.37, relheight=lbl_relh, relwidth=spec_relw)
entry_vip.place(relx=0.35, rely=0.41, relheight=spec_relh, relwidth=spec_relw)

save_hall_btn = Button(hall_register, text='save', command=lambda: btn_save_hall_info())
save_hall_btn.place(relx=0.35, rely=0.5, relwidth=spec_relw)

hallsListbox = Listbox(hall_register)
hallsListbox.place(relx=0, rely=0.6, relheight=0.1, relwidth=1)

main_btn = Button(hall_register, text='back to main page', command=lambda: change_to_main())
main_btn.place(relx=0, rely=0.9)
# HALL REGISTER FRAME - END

# CINEMA REGISTER FRAME - START
lbl_film_name = Label(cinema_register, text='Film name')
entry_film_name = Entry(cinema_register)

lbl_film_name.place(relx=0.35, rely=0.2, relheight=lbl_relh, relwidth=spec_relw)
entry_film_name.place(relx=0.35, rely=0.24, relheight=spec_relh, relwidth=spec_relw)

lbl_sch_time = Label(cinema_register, text='Scheduled time')
entry_sch_time = Entry(cinema_register)

lbl_sch_time.place(relx=0.35, rely=0.29, relheight=lbl_relh, relwidth=spec_relw)
entry_sch_time.place(relx=0.35, rely=0.33, relheight=spec_relh, relwidth=spec_relw)

lbl_cinema_hall = Label(cinema_register, text='Cinema hall')
entry_cinema_hall = Entry(cinema_register)

lbl_cinema_hall.place(relx=0.35, rely=0.38, relheight=lbl_relh, relwidth=spec_relw)
entry_cinema_hall.place(relx=0.35, rely=0.42, relheight=spec_relh, relwidth=spec_relw)

save_cinema_btn = Button(cinema_register, text='save', command=lambda: btn_save_cinema_info())
save_cinema_btn.place(relx=0.35, rely=0.55, relwidth=spec_relw)

cinemasListbox = Listbox(cinema_register)
cinemasListbox.place(relx=0, rely=0.7, relheight=0.1, relwidth=1)

main_btn = Button(cinema_register, text='back to main page', command=lambda: change_to_main())
main_btn.place(relx=0, rely=0.9)
# CINEMA REGISTER FRAME - END

customer_btn = Button(main_frame, text='Customer register', command=lambda: change_to_customer_register())
customer_btn.place(relx=0.5, rely=0.3, anchor=CENTER)

hall_btn = Button(main_frame, text='Hall register', command=lambda: change_to_hall_register())
hall_btn.place(relx=0.5, rely=0.4, anchor=CENTER)

cin_btn = Button(main_frame, text='Cinema register', command=lambda: change_to_cinema_register())
cin_btn.place(relx=0.5, rely=0.5, anchor=CENTER)


prev_frame = main_frame
win.mainloop()
