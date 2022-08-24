from tkinter import *
from main import *


def btn_sign_in():
    global prev_frame
    for elem in workers_obj_list:
        if elem.get_login() == entry_user_login.get():
            if elem.get_pass() == entry_user_password.get():
                if elem.get_title() == 'admin':
                    prev_frame.place_forget()
                    admin_frame.place(x=0, y=0)
                    prev_frame = admin_frame
                elif elem.get_title() == 'cashier':
                    prev_frame.place_forget()
                    cashier_frame.place(x=0, y=0)
                    prev_frame = cashier_frame
            else:
                lbl_signin_result.config(text='Password is incorrect')
                break
    else:
        lbl_signin_result.config(text='Worker login is not existing')


def load_customers():
    for elem in customers_obj_list:
        custListbox.insert(END, elem)


def load_cinemas():
    for elem in halls_obj_list:
        cinemasListbox.insert(END, elem.cinema_obj_list)


def btn_save_worker_info():
    if entry_worker_name.index('end') != 0 and entry_worker_surname.index('end') != 0 and \
       entry_worker_login.index('end') != 0 and entry_worker_pass.index('end') != 0 and \
       entry_worker_title.index('end') != 0:
        temp_worker = Worker(entry_worker_name.get(), entry_worker_surname.get(), entry_worker_login.get(),
                             entry_worker_pass.get(), entry_worker_title.get())
        add_worker(temp_worker)
        workersListbox.insert(END, temp_worker)
        entry_worker_name.delete(0, END)
        entry_worker_surname.delete(0, END)
        entry_worker_login.delete(0, END)
        entry_worker_pass.delete(0, END)
        entry_worker_title.delete(0, END)
    else:
        lbl_worker_result.config(text='Some info is not given, check out all empty entries')


def btn_delete_from_customers_listbox():
    index = customersListbox.curselection()[0]
    customersListbox.delete(index)
    customers_obj_list.pop(index)


def btn_delete_from_halls_listbox():
    index = hallsListbox.curselection()[0]
    hallsListbox.delete(index)
    halls_obj_list.pop(index)


# def btn_delete_from_cinemas_listbox():
#     index = cinemaListbox.curselection()[0]
#     cinemaListbox.delete(index)
#


def btn_edit_time():
    try:
        index = cinemaListbox.curselection()[0]
        edit_frame.place(relx=0.4, rely=0.4)
        print(cinemaListbox.get(index))
    except IndexError:
        lbl_cinema_result.config(text='You did not select the film')


def btn_save_customer_info():
    if entry_login.index('end') != 0 and entry_name.index('end') != 0 and entry_surname.index('end') != 0 and \
            entry_email.index('end') != 0:
        temp_cust = add_customer(entry_login.get(), entry_name.get(),
                                 entry_surname.get(), entry_age.get(), entry_email.get())
        customersListbox.insert(END, temp_cust)
        entry_login.delete(0, END)
        entry_name.delete(0, END)
        entry_surname.delete(0, END)
        entry_age.delete(0, END)
        entry_email.delete(0, END)
    else:
        lbl_cust_result.config(text='Some info is not given, check out all empty entries')


def btn_save_hall_info():
    if entry_hall_name.index('end') != 0 and entry_eco.index('end') != 0 and \
            entry_comf.index('end') != 0 and entry_vip.index('end') != 0:
        temp_hall = add_hall(entry_hall_name.get(), entry_eco.get(), entry_comf.get(), entry_vip.get())
        hallsListbox.insert(END, temp_hall)
        entry_hall_name.delete(0, END)
        entry_eco.delete(0, END)
        entry_comf.delete(0, END)
        entry_vip.delete(0, END)
    else:
        lbl_hall_result.config(text='Some info is not given, check out all empty entries')


def btn_save_cinema_info():
    if entry_film_name.index('end') != 0 and entry_sch_time.index('end') != 0 and \
            entry_cinema_hall.index('end') != 0:
        temp_cin = add_cinema(entry_film_name.get(), entry_sch_time.get(), entry_cinema_hall.get())
        if temp_cin != -1:
            cinemaListbox.insert(END, temp_cin)
            entry_film_name.delete(0, END)
            entry_sch_time.delete(0, END)
            entry_cinema_hall.delete(0, END)
        else:
            lbl_cinema_result.config(text='This hall is not exist, try again')
    else:
        lbl_cinema_result.config(text='Some info is not given, check out all empty entries')


def btn_log_out():
    global prev_frame
    if prev_frame != 0:
        prev_frame.place_forget()
    login_frame.place(x=0, y=0)
    prev_frame = login_frame


def change_to_admin_frame():
    global prev_frame
    prev_frame.place_forget()
    admin_frame.place(x=0, y=0)
    prev_frame = admin_frame


def change_to_cashier_frame():
    global prev_frame
    prev_frame.place_forget()
    cashier_frame.place(x=0, y=0)
    prev_frame = cashier_frame


def change_to_customer_register():
    global prev_frame
    if prev_frame != 0:
        prev_frame.place_forget()
    customer_register.place(x=0, y=0)
    prev_frame = customer_register


def change_to_ticket_frame():
    global prev_frame
    if prev_frame != 0:
        prev_frame.place_forget()
    ticket_frame.place(x=0, y=0)
    prev_frame = ticket_frame


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


def change_to_worker_register():
    global prev_frame
    if prev_frame != 0:
        prev_frame.place_forget()
    worker_register.place(x=0, y=0)
    prev_frame = worker_register


win = Tk()
win.title('Cinema Theatre')
win.geometry('800x800')

login_frame = Frame(width=800, height=800)
login_frame.place(x=0, y=0)
admin_frame = Frame(width=800, height=800)
worker_register = Frame(width=800, height=800)
cashier_frame = Frame(width=800, height=800)
ticket_frame = Frame(width=800, height=800)
customer_register = Frame(width=800, height=800)
hall_register = Frame(width=800, height=800)
cinema_register = Frame(width=800, height=800)
edit_frame = Frame(width=200, height=200)

spec_relh = 0.05
spec_relw = 0.3
lbl_relh = 0.04

# LOGIN FRAME - START
lbl_user_login = Label(login_frame, text='Login')
entry_user_login = Entry(login_frame)

lbl_user_login.place(relx=0.35, rely=0.37, relheight=lbl_relh, relwidth=spec_relw)
entry_user_login.place(relx=0.35, rely=0.41, relheight=spec_relh, relwidth=spec_relw)

lbl_user_password = Label(login_frame, text='Password')
entry_user_password = Entry(login_frame, show='*')

lbl_user_password.place(relx=0.35, rely=0.46, relheight=lbl_relh, relwidth=spec_relw)
entry_user_password.place(relx=0.35, rely=0.5, relheight=spec_relh, relwidth=spec_relw)

signin_save_btn = Button(login_frame, text='sign in', command=lambda: btn_sign_in())
signin_save_btn.place(relx=0.45, rely=0.55, relwidth=0.1, relheight=0.05)
signin_save_btn.bind('<Return>', lambda event: btn_sign_in())

lbl_signin_result = Label(login_frame, text='')
lbl_signin_result.place(relx=0.35, rely=0.62, relheight=lbl_relh, relwidth=spec_relw)
# LOGIN FRAME - END

# WORKER REGISTER FRAME - START
lbl_worker_name = Label(worker_register, text='Name')
entry_worker_name = Entry(worker_register)

lbl_worker_name.place(relx=0.35, rely=0, relheight=lbl_relh, relwidth=spec_relw)
entry_worker_name.place(relx=0.35, rely=0.04, relheight=spec_relh, relwidth=spec_relw)

lbl_worker_surname = Label(worker_register, text='Surname')
entry_worker_surname = Entry(worker_register)

lbl_worker_surname.place(relx=0.35, rely=0.09, relheight=lbl_relh, relwidth=spec_relw)
entry_worker_surname.place(relx=0.35, rely=0.13, relheight=spec_relh, relwidth=spec_relw)

lbl_worker_login = Label(worker_register, text='Login')
entry_worker_login = Entry(worker_register)

lbl_worker_login.place(relx=0.35, rely=0.18, relheight=lbl_relh, relwidth=spec_relw)
entry_worker_login.place(relx=0.35, rely=0.22, relheight=spec_relh, relwidth=spec_relw)

lbl_worker_pass = Label(worker_register, text='Password')
entry_worker_pass = Entry(worker_register)

lbl_worker_pass.place(relx=0.35, rely=0.27, relheight=lbl_relh, relwidth=spec_relw)
entry_worker_pass.place(relx=0.35, rely=0.31, relheight=spec_relh, relwidth=spec_relw)

lbl_worker_title = Label(worker_register, text='Title')
entry_worker_title = Entry(worker_register)

lbl_worker_title.place(relx=0.35, rely=0.36, relheight=lbl_relh, relwidth=spec_relw)
entry_worker_title.place(relx=0.35, rely=0.4, relheight=spec_relh, relwidth=spec_relw)

workersListbox = Listbox(worker_register)
workersListbox.place(relx=0, rely=0.7, relheight=0.1, relwidth=1)

save_worker_btn = Button(worker_register, text='save', command=lambda: btn_save_worker_info())
save_worker_btn.place(relx=0.35, rely=0.48, relwidth=spec_relw)

lbl_worker_result = Label(worker_register, text='')
lbl_worker_result.place(relx=0.25, rely=0.55)

main_btn = Button(worker_register, text='back to main page', command=lambda: change_to_admin_frame())
main_btn.place(relx=0, rely=0.9)
# WORKER REGISTER FRAME - END

# TICKET FRAME - START
custListbox = Listbox(ticket_frame)
custListbox.place(relx=0, rely=0, relheight=1, relwidth=0.3)

load_customers_btn = Button(ticket_frame, text='<-- Load customers', command=lambda: load_customers())
load_customers_btn.place(relx=0.37, rely=0.1, relwidth=0.25)

cinemasListbox = Listbox(ticket_frame)
cinemasListbox.place(relx=0.7, rely=0, relheight=1, relwidth=0.3)

load_cinemas_btn = Button(ticket_frame, text='Load cinemas -->', command=lambda: load_cinemas())
load_cinemas_btn.place(relx=0.37, rely=0.2, relwidth=0.25)

main_btn = Button(ticket_frame, text='back to main page', command=lambda: change_to_cashier_frame())
main_btn.place(relx=0.37, rely=0.9, relwidth=0.25)
# TICKER FRAME - END

# CUSTOMER REGISTER FRAME - START
lbl_login = Label(customer_register, text='Login')
entry_login = Entry(customer_register)

lbl_login.place(relx=0.35, rely=0, relheight=lbl_relh, relwidth=spec_relw)
entry_login.place(relx=0.35, rely=0.04, relheight=spec_relh, relwidth=spec_relw)

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

lbl_cust_result = Label(customer_register, text='')
lbl_cust_result.place(relx=0.25, rely=0.63)

customersListbox = Listbox(customer_register)
customersListbox.place(relx=0, rely=0.7, relheight=0.1, relwidth=1)

delete_from_custList = Button(customer_register, command=lambda: btn_delete_from_customers_listbox(), text='Delete')
delete_from_custList.place(relx=0.9, rely=0.9)

main_btn = Button(customer_register, text='back to main page', command=lambda: change_to_cashier_frame())
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

lbl_hall_result = Label(hall_register, text='')
lbl_hall_result.place(relx=0.25, rely=0.55)

hallsListbox = Listbox(hall_register)
hallsListbox.place(relx=0, rely=0.6, relheight=0.1, relwidth=1)

delete_from_hallsList = Button(hall_register, command=lambda: btn_delete_from_halls_listbox(), text='Delete')
delete_from_hallsList.place(relx=0.9, rely=0.9)

main_btn = Button(hall_register, text='back to main page', command=lambda: change_to_admin_frame())
main_btn.place(relx=0, rely=0.9)
# HALL REGISTER FRAME - END

# CINEMA REGISTER FRAME - START
lbl_film_name = Label(cinema_register, text='Film name')
entry_film_name = Entry(cinema_register)

lbl_film_name.place(relx=0, rely=0.2, relheight=lbl_relh, relwidth=spec_relw)
entry_film_name.place(relx=0, rely=0.24, relheight=spec_relh, relwidth=spec_relw)

lbl_sch_time = Label(cinema_register, text='Scheduled time')
entry_sch_time = Entry(cinema_register)

lbl_sch_time.place(relx=0, rely=0.29, relheight=lbl_relh, relwidth=spec_relw)
entry_sch_time.place(relx=0, rely=0.33, relheight=spec_relh, relwidth=spec_relw)

lbl_cinema_hall = Label(cinema_register, text='Cinema hall')
entry_cinema_hall = Entry(cinema_register)

lbl_cinema_hall.place(relx=0, rely=0.38, relheight=lbl_relh, relwidth=spec_relw)
entry_cinema_hall.place(relx=0, rely=0.42, relheight=spec_relh, relwidth=spec_relw)

save_cinema_btn = Button(cinema_register, text='save', command=lambda: btn_save_cinema_info())
save_cinema_btn.place(relx=0.05, rely=0.47, relwidth=0.2, relheight=0.05)

lbl_cinema_result = Label(cinema_register, text='')
lbl_cinema_result.place(relx=0, rely=0.52)

edit_time_btn = Button(cinema_register, text='edit time', command=lambda: btn_edit_time())
edit_time_btn.place(relx=0.6, rely=0.4, relwidth=0.1)

edit_hall_btn = Button(cinema_register, text='edit hall')
edit_hall_btn.place(relx=0.6, rely=0.45, relwidth=0.1)

cinemaListbox = Listbox(cinema_register)
cinemaListbox.place(relx=0.7, rely=0, relheight=1, relwidth=0.3)

main_btn = Button(cinema_register, text='back to main page', command=lambda: change_to_admin_frame())
main_btn.place(relx=0, rely=0.96)
# CINEMA REGISTER FRAME - END

# ADMIN FRAME - START
hall_btn = Button(admin_frame, text='Hall register', command=lambda: change_to_hall_register())
hall_btn.place(relx=0.5, rely=0.4, anchor=CENTER)

cin_btn = Button(admin_frame, text='Cinema register', command=lambda: change_to_cinema_register())
cin_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

worker_reg_btn = Button(admin_frame, text='Worker register', command=lambda: change_to_worker_register())
worker_reg_btn.place(relx=0.5, rely=0.6, anchor=CENTER)

log_out_btn = Button(admin_frame, text='log out', command=lambda: btn_log_out())
log_out_btn.place(relx=0, rely=0.9)
# ADMIN FRAME - END

# CASHIER FRAME - START
customer_btn = Button(cashier_frame, text='Customer register', command=lambda: change_to_customer_register())
customer_btn.place(relx=0.5, rely=0.3, anchor=CENTER)

ticket_btn = Button(cashier_frame, text='Make an order', command=lambda: change_to_ticket_frame())
ticket_btn.place(relx=0.5, rely=0.4, anchor=CENTER)

log_out_btn = Button(cashier_frame, text='log out', command=lambda: btn_log_out())
log_out_btn.place(relx=0, rely=0.9)
# CASHIER FRAME - END

prev_frame = login_frame
win.mainloop()
