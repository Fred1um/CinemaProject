from tkinter import *
from tkinter import ttk
from classes import *

spec_relh = 0.05
spec_relw = 0.3
lbl_relh = 0.04


class Main(Frame):
    def __init__(self):
        super().__init__()
        self.init_login()
        self.db = db

    def init_login(self):
        login = Frame(width=800, height=800, bd=2)
        login.place(x=0, y=0)

        lbl_user_login = Label(login, text='Login')
        self.entry_user_login = ttk.Entry(login)

        lbl_user_login.place(relx=0.35, rely=0.37, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_user_login.place(relx=0.35, rely=0.41, relheight=spec_relh, relwidth=spec_relw)

        lbl_user_password = Label(login, text='Password')
        self.entry_user_password = ttk.Entry(login, show='*')

        lbl_user_password.place(relx=0.35, rely=0.46, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_user_password.place(relx=0.35, rely=0.5, relheight=spec_relh, relwidth=spec_relw)

        signin_save_btn = ttk.Button(login, text='sign in', command=self.login)
        signin_save_btn.place(relx=0.45, rely=0.565, relwidth=0.1, relheight=0.05)

        self.lbl_signin_result = Label(login, text='')
        self.lbl_signin_result.place(relx=0.35, rely=0.62, relheight=lbl_relh, relwidth=spec_relw)

    def login(self):
        global prev_frame
        login1 = self.entry_user_login.get()
        password = self.entry_user_password.get()
        self.db.cur.execute(
            f"SELECT worker_login, worker_pass FROM workers WHERE worker_login = '{login1}' AND worker_pass = '{password}'")
        self.db.con.commit()
        if not self.db.cur.fetchone():
            self.lbl_signin_result.config(text='Not found')
        else:
            self.db.cur.execute(
                f"SELECT worker_title FROM workers WHERE worker_login = '{login1}' AND worker_pass = '{password}'")
            title = self.db.cur.fetchone()[0]
            if title == 'admin':
                self.open_admin()
            elif title == 'cashier':
                self.open_cashier()

    @staticmethod
    def open_admin():
        AdminFrame()

    @staticmethod
    def open_cashier():
        CashierFrame()


class AdminFrame(Frame):
    def __init__(self):
        super().__init__()
        self.init_admin()

    def init_admin(self):
        admin = Frame(width=800, height=800)
        admin.place(x=0, y=0)

        hall_btn = ttk.Button(admin, text='Hall register', command=self.open_hall)
        hall_btn.place(relx=0.5, rely=0.4, anchor=CENTER)

        cin_btn = ttk.Button(admin, text='Cinema register', command=self.open_cinema)
        cin_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

        worker_reg_btn = ttk.Button(admin, text='Worker register', command=self.open_worker)
        worker_reg_btn.place(relx=0.5, rely=0.6, anchor=CENTER)

        log_out_btn = ttk.Button(admin, text='log out', command=self.log_out)
        log_out_btn.place(relx=0, rely=0.96)

    @staticmethod
    def open_hall():
        HallFrame()

    @staticmethod
    def open_cinema():
        CinemaFrame()

    @staticmethod
    def open_worker():
        WorkerFrame()

    @staticmethod
    def log_out():
        Main()


class HallFrame(Frame):
    def __init__(self):
        super().__init__()
        self.init_hall()
        self.db = db
        self.view_halls()

    def init_hall(self):
        hall = Frame(width=800, height=800)
        hall.place(x=0, y=0)

        lbl_hall_name = Label(hall, text='Hall name')
        self.entry_hall_name = ttk.Entry(hall)

        lbl_hall_name.place(relx=0.35, rely=0.1, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_hall_name.place(relx=0.35, rely=0.14, relheight=spec_relh, relwidth=spec_relw)

        lbl_eco = Label(hall, text='Economy places')
        self.entry_eco = ttk.Entry(hall)

        lbl_eco.place(relx=0.35, rely=0.19, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_eco.place(relx=0.35, rely=0.23, relheight=spec_relh, relwidth=spec_relw)

        lbl_comf = Label(hall, text='Comfort places')
        self.entry_comf = ttk.Entry(hall)

        lbl_comf.place(relx=0.35, rely=0.28, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_comf.place(relx=0.35, rely=0.32, relheight=spec_relh, relwidth=spec_relw)

        lbl_vip = Label(hall, text='VIP places')
        self.entry_vip = ttk.Entry(hall)

        lbl_vip.place(relx=0.35, rely=0.37, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_vip.place(relx=0.35, rely=0.41, relheight=spec_relh, relwidth=spec_relw)

        save_hall_btn = ttk.Button(hall, text='save')
        save_hall_btn.place(relx=0.35, rely=0.5, relwidth=spec_relw)
        save_hall_btn.bind('<Button-1>', lambda event: self.hall_record(self.entry_hall_name.get(),
                                                                        self.entry_eco.get(),
                                                                        self.entry_comf.get(),
                                                                        self.entry_vip.get()))

        self.lbl_hall_result = Label(hall, text='', anchor=CENTER)
        self.lbl_hall_result.place(relx=0.25, rely=0.55, relwidth=0.5)

        self.tree = ttk.Treeview(hall, height=10, columns=('ID', 'hall_name', 'economy', 'comfort', 'vip'),
                                 show='headings')

        self.tree.column('ID', width=30, anchor=CENTER)
        self.tree.column('hall_name', width=200, anchor=CENTER)
        self.tree.column('economy', width=100, anchor=CENTER)
        self.tree.column('comfort', width=100, anchor=CENTER)
        self.tree.column('vip', width=100, anchor=CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('hall_name', text='Hall name')
        self.tree.heading('economy', text='Economy')
        self.tree.heading('comfort', text='Comfort')
        self.tree.heading('vip', text='VIP')

        self.tree.place(relx=0.2, rely=0.6)

        self.scroll = ttk.Scrollbar(hall, command=self.tree.yview)
        self.scroll.place(relx=0.9, rely=0.75, relheight=0.3, anchor=E)
        self.tree.configure(yscrollcommand=self.scroll.set)

        main_btn = ttk.Button(hall, text='back to main page', command=self.open_admin)
        main_btn.place(relx=0, rely=0.96)

    def hall_record(self, hall_name, economy, comfort, vip):
        if self.entry_hall_name.index('end') != 0 and self.entry_eco.index('end') != 0 and \
                self.entry_comf.index('end') != 0 and self.entry_vip.index('end') != 0:
            self.db.cur.execute(f"SELECT hall_name FROM halls WHERE hall_name= '{self.entry_hall_name.get()}'")
            if self.db.cur.fetchone() is None:
                self.db.insert_hall_data(hall_name, economy, comfort, vip)
                self.entry_hall_name.delete(0, END)
                self.entry_eco.delete(0, END)
                self.entry_comf.delete(0, END)
                self.entry_vip.delete(0, END)
                self.lbl_hall_result.config(text='Success!')
                self.view_halls()
            else:
                self.lbl_hall_result.config(text='This hall name is already exists')
        else:
            self.lbl_hall_result.config(text='Some info is not given, check out all empty entries')

    def view_halls(self):
        self.db.cur.execute('''SELECT * FROM halls''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    @staticmethod
    def open_admin():
        AdminFrame()


class CinemaFrame(Frame):
    def __init__(self):
        super().__init__()
        self.init_cinema()
        self.db = db
        self.view_cinemas()

    def init_cinema(self):
        cinema = Frame(width=800, height=800)
        cinema.place(x=0, y=0)

        self.lbl_film_name = Label(cinema, text='Film name')
        self.entry_film_name = ttk.Entry(cinema)

        self.lbl_film_name.place(relx=0.34, rely=0.29, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_film_name.place(relx=0.34, rely=0.33, relheight=spec_relh, relwidth=spec_relw)

        self.lbl_sch_time = Label(cinema, text='Scheduled time')
        self.entry_sch_time = ttk.Entry(cinema)

        self.lbl_sch_time.place(relx=0.34, rely=0.38, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_sch_time.place(relx=0.34, rely=0.42, relheight=spec_relh, relwidth=spec_relw)

        self.lbl_cinema_hall = Label(cinema, text='Cinema hall')
        self.entry_cinema_hall = ttk.Entry(cinema)

        self.lbl_cinema_hall.place(relx=0.34, rely=0.47, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_cinema_hall.place(relx=0.34, rely=0.51, relheight=spec_relh, relwidth=spec_relw)

        save_cinema_btn = ttk.Button(cinema, text='save')
        save_cinema_btn.place(relx=0.39, rely=0.57, relwidth=0.2, relheight=0.05)
        save_cinema_btn.bind('<Button-1>', lambda event: self.cinema_record(self.entry_film_name.get(),
                                                                            self.entry_sch_time.get(),
                                                                            self.entry_cinema_hall.get()))

        self.lbl_cinema_result = Label(cinema, text='', anchor=CENTER)
        self.lbl_cinema_result.place(relx=0.24, rely=0.62, relwidth=0.5)

        self.time_update = PhotoImage(file='icons/clock_update.png')
        edit_time_btn = ttk.Button(cinema, image=self.time_update)
        edit_time_btn.place(relx=0.92, rely=0.69,  width=50, height=50)

        self.hall_update = PhotoImage(file='icons/update.png')
        edit_hall_btn = ttk.Button(cinema, image=self.hall_update)
        edit_hall_btn.place(relx=0.92, rely=0.76, width=50, height=50)

        self.delete_img = PhotoImage(file='icons/delete.png')
        delete_cinema_btn = ttk.Button(cinema, image=self.delete_img)
        delete_cinema_btn.place(relx=0.92, rely=0.83, width=50, height=50)

        self.tree = ttk.Treeview(cinema, height=10, columns=('ID', 'film_name', 'scheduled_time', 'cinema_hall'),
                                 show='headings')

        self.tree.column('ID', width=30, anchor=CENTER)
        self.tree.column('film_name', width=200, anchor=CENTER)
        self.tree.column('scheduled_time', width=100, anchor=CENTER)
        self.tree.column('cinema_hall', width=200, anchor=CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('film_name', text='Film name')
        self.tree.heading('scheduled_time', text='Scheduled time')
        self.tree.heading('cinema_hall', text='Cinema hall')

        self.tree.place(relx=0.175, rely=0.65)

        self.scroll = ttk.Scrollbar(cinema, command=self.tree.yview)
        self.scroll.place(relx=0.87, rely=0.79, relheight=0.3, anchor=E)
        self.tree.configure(yscrollcommand=self.scroll.set)

        main_btn = ttk.Button(cinema, text='back to main page', command=self.open_admin)
        main_btn.place(relx=0, rely=0.96)

    def cinema_record(self, film_name, scheduled_time, cinema_hall):
        if self.entry_film_name.index('end') != 0 and self.entry_sch_time.index('end') != 0 and \
                self.entry_cinema_hall.index('end') != 0:
            self.db.insert_cinema_data(film_name, scheduled_time, cinema_hall)
            self.entry_film_name.delete(0, END)
            self.entry_sch_time.delete(0, END)
            self.entry_cinema_hall.delete(0, END)
            self.lbl_cinema_result.config(text='Success!')
            self.view_cinemas()
        else:
            self.lbl_cinema_result.config(text='Some info is not given, check out all empty entries')

    def view_cinemas(self):
        self.db.cur.execute('''SELECT * FROM cinemas''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    @staticmethod
    def open_admin():
        AdminFrame()


class WorkerFrame(Frame):
    def __init__(self):
        super().__init__()
        self.init_worker()
        self.db = db
        self.view_workers()


    def init_worker(self):
        worker = Frame(width=800, height=800)
        worker.place(x=0, y=0)

        lbl_worker_name = Label(worker, text='Name')
        self.entry_worker_name = ttk.Entry(worker)

        lbl_worker_name.place(relx=0.35, rely=0, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_worker_name.place(relx=0.35, rely=0.04, relheight=spec_relh, relwidth=spec_relw)

        lbl_worker_surname = Label(worker, text='Surname')
        self.entry_worker_surname = ttk.Entry(worker)

        lbl_worker_surname.place(relx=0.35, rely=0.09, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_worker_surname.place(relx=0.35, rely=0.13, relheight=spec_relh, relwidth=spec_relw)

        lbl_worker_login = Label(worker, text='Login')
        self.entry_worker_login = ttk.Entry(worker)

        lbl_worker_login.place(relx=0.35, rely=0.18, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_worker_login.place(relx=0.35, rely=0.22, relheight=spec_relh, relwidth=spec_relw)

        lbl_worker_pass = Label(worker, text='Password')
        self.entry_worker_pass = ttk.Entry(worker)

        lbl_worker_pass.place(relx=0.35, rely=0.27, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_worker_pass.place(relx=0.35, rely=0.31, relheight=spec_relh, relwidth=spec_relw)

        lbl_worker_title = Label(worker, text='Title')
        self.entry_worker_title = ttk.Entry(worker)

        lbl_worker_title.place(relx=0.35, rely=0.36, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_worker_title.place(relx=0.35, rely=0.4, relheight=spec_relh, relwidth=spec_relw)

        self.tree = ttk.Treeview(worker, height=10, columns=('ID', 'worker_name', 'worker_surname', 'worker_login',
                                 'worker_pass', 'worker_title'),
                                 show='headings')

        self.tree.column('ID', width=30, anchor=CENTER)
        self.tree.column('worker_name', width=200, anchor=CENTER)
        self.tree.column('worker_surname', width=200, anchor=CENTER)
        self.tree.column('worker_login', width=100, anchor=CENTER)
        self.tree.column('worker_pass', width=100, anchor=CENTER)
        self.tree.column('worker_title', width=100, anchor=CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('worker_name', text='Worker name')
        self.tree.heading('worker_surname', text='Worker surname')
        self.tree.heading('worker_login', text='Worker login')
        self.tree.heading('worker_pass', text='Worker pass')
        self.tree.heading('worker_title', text='Worker title')

        self.tree.place(relx=0.042, rely=0.65)

        self.scroll = ttk.Scrollbar(worker, command=self.tree.yview)
        self.scroll.place(relx=0.97, rely=0.79, relheight=0.3, anchor=E)
        self.tree.configure(yscrollcommand=self.scroll.set)

        save_worker_btn = ttk.Button(worker, text='save')
        save_worker_btn.place(relx=0.35, rely=0.48, relwidth=spec_relw)
        save_worker_btn.bind('<Button-1>', lambda event: self.worker_record(self.entry_worker_name.get(),
                                                                            self.entry_worker_surname.get(),
                                                                            self.entry_worker_login.get(),
                                                                            self.entry_worker_pass.get(),
                                                                            self.entry_worker_title.get()))

        self.lbl_worker_result = Label(worker, text='', anchor=CENTER)
        self.lbl_worker_result.place(relx=0.25, rely=0.55, relwidth=0.5)

        main_btn = ttk.Button(worker, text='back to main page', command=self.open_admin)
        main_btn.place(relx=0, rely=0.96)

    def worker_record(self, worker_name, worker_surname, worker_login, worker_pass, worker_title):
        if self.entry_worker_name.index('end') != 0 and self.entry_worker_surname.index('end') != 0 and \
                self.entry_worker_login.index('end') != 0 and self.entry_worker_pass.index('end') != 0 and \
                self.entry_worker_title.index('end') != 0:
            db.cur.execute(f"SELECT worker_login FROM workers WHERE worker_login= '{self.entry_worker_login.get()}'")
            if db.cur.fetchone() is None:
                self.db.insert_worker_data(worker_name, worker_surname, worker_login, worker_pass, worker_title)
                self.entry_worker_name.delete(0, END)
                self.entry_worker_surname.delete(0, END)
                self.entry_worker_login.delete(0, END)
                self.entry_worker_pass.delete(0, END)
                self.entry_worker_title.delete(0, END)
                self.lbl_worker_result.config(text='Success!')
                self.view_workers()
            else:
                self.lbl_worker_result.config(text='This login is already exists')
        else:
            self.lbl_worker_result.config(text='Some info is not given, check out all empty entries')

    def view_workers(self):
        self.db.cur.execute('''SELECT * FROM workers''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    @staticmethod
    def open_admin():
        AdminFrame()


class CashierFrame(Frame):
    def __init__(self):
        super().__init__()
        self.init_cashier()

    def init_cashier(self):
        cashier = Frame(width=800, height=800)
        cashier.place(x=0, y=0)

        customer_btn = ttk.Button(cashier, text='Customer register', command=self.open_customer)
        customer_btn.place(relx=0.5, rely=0.475, anchor=CENTER)

        ticket_btn = ttk.Button(cashier, text='Make an order', command=self.open_ticket)
        ticket_btn.place(relx=0.5, rely=0.525, anchor=CENTER)

        log_out_btn = ttk.Button(cashier, text='log out', command=self.log_out)
        log_out_btn.place(relx=0, rely=0.96)

    @staticmethod
    def open_customer():
        CustomerFrame()

    @staticmethod
    def open_ticket():
        TicketFrame()

    @staticmethod
    def log_out():
        Main()


class CustomerFrame(Frame):
    def __init__(self):
        super().__init__()
        self.init_customer()
        self.db = db
        self.view_customers()

    def init_customer(self):
        customer = Frame(width=800, height=800)
        customer.place(x=0, y=0)

        lbl_login = Label(customer, text='Login')
        self.entry_login = ttk.Entry(customer)

        lbl_login.place(relx=0.35, rely=0.09, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_login.place(relx=0.35, rely=0.13, relheight=spec_relh, relwidth=spec_relw)

        lbl_name = Label(customer, text='Name')
        self.entry_name = ttk.Entry(customer)

        lbl_name.place(relx=0.35, rely=0.18, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_name.place(relx=0.35, rely=0.22, relheight=spec_relh, relwidth=spec_relw)

        lbl_surname = Label(customer, text='Surname')
        self.entry_surname = ttk.Entry(customer)

        lbl_surname.place(relx=0.35, rely=0.27, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_surname.place(relx=0.35, rely=0.31, relheight=spec_relh, relwidth=spec_relw)

        lbl_age = Label(customer, text='Age')
        self.entry_age = ttk.Entry(customer)

        lbl_age.place(relx=0.35, rely=0.36, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_age.place(relx=0.35, rely=0.4, relheight=spec_relh, relwidth=spec_relw)

        lbl_email = Label(customer, text='Email')
        self.entry_email = ttk.Entry(customer)

        lbl_email.place(relx=0.35, rely=0.45, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_email.place(relx=0.35, rely=0.49, relheight=spec_relh, relwidth=spec_relw)

        save_cust_btn = ttk.Button(customer, text='save')
        save_cust_btn.place(relx=0.35, rely=0.58, relwidth=spec_relw)
        save_cust_btn.bind('<Button-1>', lambda event: self.customer_record(self.entry_login.get(),
                                                                            self.entry_name.get(),
                                                                            self.entry_surname.get(),
                                                                            self.entry_age.get(),
                                                                            self.entry_email.get()))

        self.lbl_cust_result = Label(customer, text='')
        self.lbl_cust_result.place(relx=0.25, rely=0.55, relwidth=0.5)

        self.tree = ttk.Treeview(customer, height=10, columns=('ID', 'customer_login', 'customer_name',
                                                               'customer_surname', 'customer_age', 'customer_email'),
                                 show='headings')

        self.tree.column('ID', width=30, anchor=CENTER)
        self.tree.column('customer_login', width=100, anchor=CENTER)
        self.tree.column('customer_name', width=150, anchor=CENTER)
        self.tree.column('customer_surname', width=150, anchor=CENTER)
        self.tree.column('customer_age', width=50, anchor=CENTER)
        self.tree.column('customer_email', width=300, anchor=CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('customer_name', text='Customer name')
        self.tree.heading('customer_surname', text='Customer surname')
        self.tree.heading('customer_login', text='Customer login')
        self.tree.heading('customer_age', text='Customer age')
        self.tree.heading('customer_email', text='Customer email')

        self.tree.place(relx=0, rely=0.65)

        scroll = ttk.Scrollbar(customer, command=self.tree.yview)
        scroll.place(relx=0.995, rely=0.795, relheight=0.3, anchor=E)
        self.tree.configure(yscrollcommand=scroll.set)

        main_btn = ttk.Button(customer, text='back to main page', command=self.open_cashier)
        main_btn.place(relx=0, rely=0.96)

    def customer_record(self, customer_login, customer_name, customer_surname, customer_age, customer_email):
        if self.entry_login.index('end') != 0 and self.entry_name.index('end') != 0 and \
                self.entry_surname.index('end') != 0 and self.entry_age.index('end') != 0 and \
                self.entry_email.index('end') != 0:
            db.cur.execute(f"SELECT customer_login FROM customers WHERE customer_login= '{self.entry_login.get()}'")
            if db.cur.fetchone() is None:
                self.db.insert_customer_data(customer_login, customer_name, customer_surname,
                                             customer_age, customer_email)
                self.entry_login.delete(0, END)
                self.entry_name.delete(0, END)
                self.entry_surname.delete(0, END)
                self.entry_age.delete(0, END)
                self.entry_email.delete(0, END)
                self.lbl_cust_result.config(text='Success!')
                self.view_customers()
            else:
                self.lbl_cust_result.config(text='This login is already exists')
        else:
            self.lbl_cust_result.config(text='Some info is not given, check out all empty entries')

    def view_customers(self):
        self.db.cur.execute('''SELECT * FROM customers''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    @staticmethod
    def open_cashier():
        CashierFrame()


class TicketFrame(Frame):
    def __init__(self):
        super().__init__()
        self.init_ticket()

    def init_ticket(self):
        ticket = Frame(width=800, height=800)
        ticket.place(x=0, y=0)

        self.custListbox = Listbox(ticket)
        self.custListbox.place(relx=0, rely=0, relheight=1, relwidth=0.3)

        load_customers_btn = ttk.Button(ticket, text='<-- Load customers')
        load_customers_btn.place(relx=0.37, rely=0.1, relwidth=0.25)

        self.cinemasListbox = Listbox(ticket)
        self.cinemasListbox.place(relx=0.7, rely=0, relheight=1, relwidth=0.3)

        load_cinemas_btn = ttk.Button(ticket, text='Load cinemas -->')
        load_cinemas_btn.place(relx=0.37, rely=0.2, relwidth=0.25)

        main_btn = ttk.Button(ticket, text='back to main page', command=self.open_cashier)
        main_btn.place(relx=0.37, rely=0.9, relwidth=0.25)

    @staticmethod
    def open_cashier():
        CashierFrame()


class DB:
    def __init__(self):
        self.con = sqlite3.connect('cinema.db')
        self.cur = self.con.cursor()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS workers(
            id integer primary key, 
            worker_name text, 
            worker_surname text, 
            worker_login text,
            worker_pass text,
            worker_title text)''')
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS customers(
            id integer primary key,
            customer_login text, 
            customer_name text, 
            customer_surname text, 
            customer_age text,
            customer_email text)''')
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS halls(
            id integer primary key, 
            hall_name text, 
            economy text, 
            comfort text,
            vip text)''')
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS cinemas(
            id integer primary key,
            film_name text, 
            scheduled_time text, 
            cinema_hall text)''')
        self.con.commit()

    def insert_hall_data(self, hall_name, economy, comfort, vip):
        self.cur.execute('''INSERT INTO halls (hall_name, economy, comfort, vip) VALUES (?, ?, ?, ?)''',
                         (hall_name, economy, comfort, vip))
        self.con.commit()

    def insert_cinema_data(self, film_name, scheduled_time, cinema_hall):
        self.cur.execute('''INSERT INTO cinemas (film_name, scheduled_time, cinema_hall) VALUES (?, ?, ?)''',
                         (film_name, scheduled_time, cinema_hall))
        self.con.commit()

    def insert_worker_data(self, worker_name, worker_surname, worker_login, worker_pass, worker_title):
        self.cur.execute('''INSERT INTO workers (worker_name, worker_surname, worker_login, worker_pass,
                            worker_title) VALUES (?, ?, ?, ?, ?)''',
                         (worker_name, worker_surname, worker_login, worker_pass, worker_title))
        self.con.commit()

    def insert_customer_data(self, customer_login, customer_name, customer_surname, customer_age, customer_email):
        self.cur.execute('''INSERT INTO customers (customer_login, customer_name, customer_surname, customer_age,
                            customer_email) VALUES (?, ?, ?, ?, ?)''',
                         (customer_login, customer_name, customer_surname, customer_age, customer_email))
        self.con.commit()


if __name__ == '__main__':
    win = Tk()
    db = DB()
    app = Main()
    app.pack()
    win.title('Cinema Project')
    width_window = 800
    height_window = 800
    width_screen = win.winfo_screenwidth()
    height_screen = win.winfo_screenheight()
    x_center = int(width_screen / 2 - width_window / 2)
    y_center = int(height_screen / 2 - height_window / 2)
    win.geometry(f'{width_window}x{height_window}+{x_center}+{y_center}')
    win.resizable(False, False)
    win.mainloop()
