import sqlite3
from tkinter import *
from tkinter import ttk
from classes import *

eco_price = '5'
comf_price = '8'
vip_price = '10'
spec_relh = 0.05
spec_relw = 0.3
lbl_relh = 0.04
auth_worker_name = ''


class Main(Frame):
    def __init__(self):
        super().__init__()
        self.init_login()
        self.db = db

    def init_login(self):
        login = ttk.Frame(width=800, height=800, style='Card.TFrame')
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
            global auth_worker_name
            self.db.cur.execute(
                f"SELECT worker_name FROM workers WHERE worker_login = '{login1}' AND worker_pass = '{password}'")
            self.db.con.commit()
            auth_worker_name = self.db.cur.fetchone()[0]
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
        admin = ttk.Frame(width=800, height=800, style='Card.TFrame')
        admin.place(x=0, y=0)

        global auth_worker_name
        lbl_auth_worker = ttk.Label(admin, text=f'Welcome, {auth_worker_name}', font=('Comic Sans MS', '16'))
        lbl_auth_worker.place(relx=0.5, rely=0.3, anchor=CENTER)

        hall_btn = ttk.Button(admin, text='Hall register', command=self.open_hall)
        hall_btn.place(relx=0.5, rely=0.4, anchor=CENTER, relwidth=0.16)

        cin_btn = ttk.Button(admin, text='Cinema register', command=self.open_cinema)
        cin_btn.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.16)

        worker_reg_btn = ttk.Button(admin, text='Worker register', command=self.open_worker)
        worker_reg_btn.place(relx=0.5, rely=0.6, anchor=CENTER, relwidth=0.16)

        log_out_btn = ttk.Button(admin, text='log out', command=self.log_out)
        log_out_btn.place(relx=0.01, rely=0.95)

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
        hall = ttk.Frame(width=800, height=800, style='Card.TFrame')
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

        self.save_hall_btn = ttk.Button(hall, text='save')
        self.save_hall_btn.place(relx=0.35, rely=0.5, relwidth=spec_relw)
        self.save_hall_btn.bind('<Button-1>', lambda event: self.hall_record(self.entry_hall_name.get(),
                                                                        self.entry_eco.get(),
                                                                        self.entry_comf.get(),
                                                                        self.entry_vip.get()))

        self.save_edited_info = ttk.Button(hall, text='edit')
        self.save_edited_info.bind('<Button-1>', lambda event: self.edit_record(self.entry_hall_name.get(),
                                                                             self.entry_eco.get(),
                                                                             self.entry_comf.get(),
                                                                                self.entry_vip.get()))

        self.lbl_hall_result = Label(hall, text='', anchor=CENTER)
        self.lbl_hall_result.place(relx=0.25, rely=0.55, relwidth=0.5)

        self.hall_search_img = PhotoImage(file='icons/search.png')
        hall_search = ttk.Button(hall, image=self.hall_search_img, command=self.open_search_hall)
        hall_search.place(relx=0.89, rely=0.6, width=55, height=55)

        self.hall_refresh = PhotoImage(file='icons/refresh.png')
        hall_refresh = ttk.Button(hall, image=self.hall_refresh, command=self.view_halls)
        hall_refresh.place(relx=0.89, rely=0.69, width=55, height=55)

        self.hall_edit_img = PhotoImage(file='icons/clock_update.png')
        cinema_edit_btn = ttk.Button(hall, image=self.hall_edit_img, command=self.default_data)
        cinema_edit_btn.place(relx=0.89, rely=0.78,  width=55, height=55)

        self.delete_hall_img = PhotoImage(file='icons/delete.png')
        delete_hall_btn = ttk.Button(hall, image=self.delete_hall_img, command=self.delete_records)
        delete_hall_btn.place(relx=0.89, rely=0.87, width=55, height=55)

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

        self.tree.place(relx=0.15, rely=0.6)

        self.scroll = ttk.Scrollbar(hall, command=self.tree.yview)
        self.scroll.place(relx=0.88, rely=0.77, relheight=0.33, anchor=E)
        self.tree.configure(yscrollcommand=self.scroll.set)

        main_btn = ttk.Button(hall, text='back to main page', command=self.open_admin)
        main_btn.place(relx=0.01, rely=0.95)

    def hall_record(self, hall_name, economy, comfort, vip):
        if self.entry_hall_name.index('end') != 0 and self.entry_eco.index('end') != 0 and \
                self.entry_comf.index('end') != 0 and self.entry_vip.index('end') != 0:
            self.db.cur.execute(f"SELECT hall_name FROM halls WHERE hall_name= '{self.entry_hall_name.get()}'")
            if self.db.cur.fetchone() is None:
                temp_hall = Hall(hall_name, economy, comfort, vip)
                self.db.insert_hall_data(temp_hall.get_name(), temp_hall.get_eco(),
                                         temp_hall.get_comf(), temp_hall.get_vip())
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

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute('''DELETE FROM halls WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_halls()

    def search_halls(self, hall_name):
        hall_name = ('%' + hall_name + '%', )
        self.db.cur.execute('''SELECT * FROM halls WHERE hall_name LIKE ?''', hall_name)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def default_data(self):
        try:
            self.entry_hall_name.delete(0, END)
            self.entry_eco.delete(0, END)
            self.entry_comf.delete(0, END)
            self.entry_vip.delete(0, END)
            self.db.cur.execute('''SELECT * FROM halls WHERE id=?''',
                                (self.tree.set(self.tree.selection()[0], '#1'), ))
            row = self.db.cur.fetchone()
            self.entry_hall_name.insert(0, row[1])
            self.entry_eco.insert(0, row[2])
            self.entry_comf.insert(0, row[3])
            self.entry_vip.insert(0, row[4])
            self.save_hall_btn.place_forget()
            self.save_edited_info.place(relx=0.35, rely=0.5, relwidth=spec_relw)
        except IndexError:
            self.lbl_hall_result.config(text='You have not selected the hall')

    def edit_record(self, hall_name, economy, comfort, vip):
        if self.entry_hall_name.index('end') != 0 and self.entry_eco.index('end') != 0 and \
                self.entry_comf.index('end') != 0 and self.entry_vip.index('end') != 0:
            self.db.cur.execute('''UPDATE halls SET hall_name=?, economy=?, comfort=?, vip=? WHERE ID=?''',
                                (hall_name, economy, comfort, vip, self.tree.set(self.tree.selection()[0], '#1')))
            self.db.con.commit()
            self.entry_hall_name.delete(0, END)
            self.entry_eco.delete(0, END)
            self.entry_comf.delete(0, END)
            self.entry_vip.delete(0, END)
            self.view_halls()
            self.save_edited_info.place_forget()
            self.save_hall_btn.place(relx=0.35, rely=0.5, relwidth=spec_relw)
        else:
            self.lbl_hall_result.config(text='Some info is not given, check out all empty entries')

    @staticmethod
    def open_admin():
        AdminFrame()

    @staticmethod
    def open_search_hall():
        SearchHall()


class SearchHall(Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search_hall()
        self.hall = HallFrame()

    def init_search_hall(self):
        self.title('Search')
        self.width_window = 300
        self.height_window = 100
        self.width_screen = win.winfo_screenwidth()
        self.height_screen = win.winfo_screenheight()
        self.x_center = int(self.width_screen / 2 - self.width_window / 2)
        self.y_center = int(self.height_screen / 2 - self.height_window / 2)
        self.geometry(f'{self.width_window}x{self.height_window}+{self.x_center}+{self.y_center}')
        self.resizable(False, False)

        label_search = Label(self, text='Search')
        label_search.place(relx=0.166, rely=0.2)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(relx=0.35, rely=0.2, relwidth=0.5)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(relx=0.61, rely=0.6)

        btn_search = ttk.Button(self, text='Search')
        btn_search.place(relx=0.28, rely=0.6)
        btn_search.bind('<Button-1>', lambda event: self.hall.search_halls(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

        self.grab_set()
        self.focus_set()


class CinemaFrame(Frame):
    def __init__(self):
        super().__init__()
        self.init_cinema()
        self.db = db
        self.view_cinemas()

    def init_cinema(self):
        cinema_frame = ttk.Frame(width=800, height=800, style='Card.TFrame')
        cinema_frame.place(x=0, y=0)

        lbl_film_name = Label(cinema_frame, text='Film name')
        self.entry_film_name = ttk.Entry(cinema_frame)

        lbl_film_name.place(relx=0.34, rely=0.19, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_film_name.place(relx=0.34, rely=0.23, relheight=spec_relh, relwidth=spec_relw)

        lbl_sch_time = Label(cinema_frame, text='Scheduled time')
        self.entry_sch_time = ttk.Entry(cinema_frame)

        lbl_sch_time.place(relx=0.34, rely=0.28, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_sch_time.place(relx=0.34, rely=0.32, relheight=spec_relh, relwidth=spec_relw)

        lbl_cinema_hall = Label(cinema_frame, text='Cinema hall')
        self.entry_cinema_hall = ttk.Entry(cinema_frame)

        lbl_cinema_hall.place(relx=0.34, rely=0.37, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_cinema_hall.place(relx=0.34, rely=0.41, relheight=spec_relh, relwidth=spec_relw)

        self.save_cinema_btn = ttk.Button(cinema_frame, text='save')
        self.save_cinema_btn.place(relx=0.39, rely=0.5, relwidth=0.2, relheight=0.05)
        self.save_cinema_btn.bind('<Button-1>', lambda event: self.cinema_record(self.entry_film_name.get(),
                                                                            self.entry_sch_time.get(),
                                                                            self.entry_cinema_hall.get()))

        self.save_edited_info = ttk.Button(cinema_frame, text='edit')
        self.save_edited_info.bind('<Button-1>', lambda event: self.edit_record(self.entry_film_name.get(),
                                                                             self.entry_sch_time.get(),
                                                                             self.entry_cinema_hall.get()))

        self.lbl_cinema_result = Label(cinema_frame, text='', anchor=CENTER)
        self.lbl_cinema_result.place(relx=0.24, rely=0.55, relwidth=0.5)

        self.cinema_search_img = PhotoImage(file='icons/search.png')
        cinema_search = ttk.Button(cinema_frame, image=self.cinema_search_img, command=self.open_search_cinema)
        cinema_search.place(relx=0.875, rely=0.6, width=55, height=55)

        self.cinema_refresh_img = PhotoImage(file='icons/refresh.png')
        cinema_refresh = ttk.Button(cinema_frame, image=self.cinema_refresh_img, command=self.view_cinemas)
        cinema_refresh.place(relx=0.875, rely=0.69, width=55, height=55)

        self.cinema_edit_img = PhotoImage(file='icons/clock_update.png')
        cinema_edit_btn = ttk.Button(cinema_frame, image=self.cinema_edit_img, command=self.default_data)
        cinema_edit_btn.place(relx=0.875, rely=0.78,  width=55, height=55)

        self.delete_cinema_img = PhotoImage(file='icons/delete.png')
        delete_cinema_btn = ttk.Button(cinema_frame, image=self.delete_cinema_img, command=self.delete_records)
        delete_cinema_btn.place(relx=0.875, rely=0.87, width=55, height=55)

        self.tree = ttk.Treeview(cinema_frame, height=10, columns=('ID', 'film_name', 'scheduled_time', 'cinema_hall'),
                                 show='headings')

        self.tree.column('ID', width=30, anchor=CENTER)
        self.tree.column('film_name', width=200, anchor=CENTER)
        self.tree.column('scheduled_time', width=100, anchor=CENTER)
        self.tree.column('cinema_hall', width=200, anchor=CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('film_name', text='Film name')
        self.tree.heading('scheduled_time', text='Scheduled time')
        self.tree.heading('cinema_hall', text='Cinema hall')

        self.tree.place(relx=0.14, rely=0.6)

        self.scroll = ttk.Scrollbar(cinema_frame, command=self.tree.yview)
        self.scroll.place(relx=0.865, rely=0.77, relheight=0.33, anchor=E)
        self.tree.configure(yscrollcommand=self.scroll.set)

        main_btn = ttk.Button(cinema_frame, text='back to main page', command=self.open_admin)
        main_btn.place(relx=0.01, rely=0.95)

    def cinema_record(self, film_name, scheduled_time, cinema_hall):
        if self.entry_film_name.index('end') != 0 and self.entry_sch_time.index('end') != 0 and \
                self.entry_cinema_hall.index('end') != 0:
            db.cur.execute(f"SELECT hall_name FROM halls WHERE hall_name= '{self.entry_cinema_hall.get()}'")
            if db.cur.fetchone() is None:
                self.lbl_cinema_result.config(text='This hall is not exist')
            else:
                temp_cinema = Cinema(film_name, scheduled_time, cinema_hall)
                self.db.insert_cinema_data(temp_cinema.get_name(), temp_cinema.get_time(), temp_cinema.get_hall())
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

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute('''DELETE FROM cinemas WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_cinemas()

    def search_records(self, cinema_name):
        cinema_name = ('%' + cinema_name + '%', )
        self.db.cur.execute('''SELECT * FROM cinemas WHERE film_name LIKE ?''', cinema_name)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def default_data(self):
        try:
            self.entry_film_name.delete(0, END)
            self.entry_sch_time.delete(0, END)
            self.entry_cinema_hall.delete(0, END)
            self.db.cur.execute('''SELECT * FROM cinemas WHERE id=?''',
                                (self.tree.set(self.tree.selection()[0], '#1'), ))
            row = self.db.cur.fetchone()
            self.entry_film_name.insert(0, row[1])
            self.entry_sch_time.insert(0, row[2])
            self.entry_cinema_hall.insert(0, row[3])
            self.save_cinema_btn.place_forget()
            self.save_edited_info.place(relx=0.39, rely=0.57, relwidth=0.2, relheight=0.05)
        except IndexError:
            self.lbl_cinema_result.config(text='You have not selected the film')

    def edit_record(self, film_name, scheduled_time, cinema_hall):
        if self.entry_film_name.index('end') != 0 and self.entry_sch_time.index('end') != 0 and \
                self.entry_cinema_hall.index('end') != 0:
            db.cur.execute(f"SELECT hall_name FROM halls WHERE hall_name= '{self.entry_cinema_hall.get()}'")
            if db.cur.fetchone() is None:
                self.lbl_cinema_result.config(text='This hall is not exist')
            else:
                self.db.cur.execute('''UPDATE cinemas SET film_name=?, scheduled_time=?, cinema_hall=? WHERE ID=?''',
                                    (film_name, scheduled_time, cinema_hall, self.tree.set(self.tree.selection()[0], '#1')))
                self.db.con.commit()
                self.entry_film_name.delete(0, END)
                self.entry_sch_time.delete(0, END)
                self.entry_cinema_hall.delete(0, END)
                self.view_cinemas()
                self.save_edited_info.place_forget()
                self.save_cinema_btn.place(relx=0.39, rely=0.57, relwidth=0.2, relheight=0.05)
        else:
            self.lbl_cinema_result.config(text='Some info is not given, check out all empty entries')

    @staticmethod
    def open_admin():
        AdminFrame()

    @staticmethod
    def open_search_cinema():
        SearchCinema()


class SearchCinema(Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search_cinema()
        self.cinema = CinemaFrame()

    def init_search_cinema(self):
        self.title('Search')
        self.width_window = 300
        self.height_window = 100
        self.width_screen = win.winfo_screenwidth()
        self.height_screen = win.winfo_screenheight()
        self.x_center = int(self.width_screen / 2 - self.width_window / 2)
        self.y_center = int(self.height_screen / 2 - self.height_window / 2)
        self.geometry(f'{self.width_window}x{self.height_window}+{self.x_center}+{self.y_center}')
        self.resizable(False, False)

        label_search = Label(self, text='Search')
        label_search.place(relx=0.166, rely=0.2)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(relx=0.35, rely=0.2, relwidth=0.5)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(relx=0.61, rely=0.6)

        btn_search = ttk.Button(self, text='Search')
        btn_search.place(relx=0.28, rely=0.6)
        btn_search.bind('<Button-1>', lambda event: self.cinema.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

        self.grab_set()
        self.focus_set()


class WorkerFrame(Frame):
    def __init__(self):
        super().__init__()
        self.init_worker()
        self.db = db
        self.view_workers()

    def init_worker(self):
        worker = ttk.Frame(width=800, height=800, style='Card.TFrame')
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

        self.worker_search_img = PhotoImage(file='icons/search.png')
        worker_search = ttk.Button(worker, image=self.worker_search_img, command=self.open_search_worker)
        worker_search.place(relx=0.91, rely=0.6, width=55, height=55)

        self.worker_refresh_img = PhotoImage(file='icons/refresh.png')
        worker_refresh = ttk.Button(worker, image=self.worker_refresh_img, command=self.view_workers)
        worker_refresh.place(relx=0.91, rely=0.69, width=55, height=55)

        self.worker_edit_img = PhotoImage(file='icons/clock_update.png')
        worker_edit_btn = ttk.Button(worker, image=self.worker_edit_img, command=self.default_data)
        worker_edit_btn.place(relx=0.91, rely=0.78,  width=55, height=55)

        self.worker_delete_img = PhotoImage(file='icons/delete.png')
        delete_worker_btn = ttk.Button(worker, image=self.worker_delete_img, command=self.delete_records)
        delete_worker_btn.place(relx=0.91, rely=0.87, width=55, height=55)

        self.tree = ttk.Treeview(worker, height=10, columns=('ID', 'worker_name', 'worker_surname', 'worker_login',
                                 'worker_pass', 'worker_title'),
                                 show='headings')

        self.tree.column('ID', width=30, anchor=CENTER)
        self.tree.column('worker_name', width=150, anchor=CENTER)
        self.tree.column('worker_surname', width=150, anchor=CENTER)
        self.tree.column('worker_login', width=100, anchor=CENTER)
        self.tree.column('worker_pass', width=100, anchor=CENTER)
        self.tree.column('worker_title', width=100, anchor=CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('worker_name', text='Worker name')
        self.tree.heading('worker_surname', text='Worker surname')
        self.tree.heading('worker_login', text='Worker login')
        self.tree.heading('worker_pass', text='Worker pass')
        self.tree.heading('worker_title', text='Worker title')

        self.tree.place(relx=0.042, rely=0.6)

        self.scroll = ttk.Scrollbar(worker, command=self.tree.yview)
        self.scroll.place(relx=0.9, rely=0.77, relheight=0.33, anchor=E)
        self.tree.configure(yscrollcommand=self.scroll.set)

        self.save_worker_btn = ttk.Button(worker, text='save')
        self.save_worker_btn.place(relx=0.35, rely=0.48, relwidth=spec_relw)
        self.save_worker_btn.bind('<Button-1>', lambda event: self.worker_record(self.entry_worker_name.get(),
                                                                            self.entry_worker_surname.get(),
                                                                            self.entry_worker_login.get(),
                                                                            self.entry_worker_pass.get(),
                                                                            self.entry_worker_title.get()))

        self.save_edited_info = ttk.Button(worker, text='edit')
        self.save_edited_info.bind('<Button-1>', lambda event: self.edit_record(self.entry_worker_name.get(),
                                                                            self.entry_worker_surname.get(),
                                                                            self.entry_worker_login.get(),
                                                                            self.entry_worker_pass.get(),
                                                                            self.entry_worker_title.get()))

        self.lbl_worker_result = Label(worker, text='', anchor=CENTER)
        self.lbl_worker_result.place(relx=0.25, rely=0.55, relwidth=0.5)

        main_btn = ttk.Button(worker, text='back to main page', command=self.open_admin)
        main_btn.place(relx=0.01, rely=0.95)

    def worker_record(self, worker_name, worker_surname, worker_login, worker_pass, worker_title):
        if self.entry_worker_name.index('end') != 0 and self.entry_worker_surname.index('end') != 0 and \
                self.entry_worker_login.index('end') != 0 and self.entry_worker_pass.index('end') != 0 and \
                self.entry_worker_title.index('end') != 0:
            db.cur.execute(f"SELECT worker_login FROM workers WHERE worker_login= '{self.entry_worker_login.get()}'")
            if db.cur.fetchone() is None:
                temp_worker = Worker(worker_name, worker_surname, worker_login, worker_pass, worker_title)
                self.db.insert_worker_data(temp_worker.get_name(), temp_worker.get_surname(), temp_worker.get_login(),
                                           temp_worker.get_pass(), temp_worker.get_title())
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
        self.db.cur.execute('''SELECT * FROM workers ORDER BY worker_title ASC''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute('''DELETE FROM workers WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_workers()

    def search_workers(self, worker_login):
        worker_login = ('%' + worker_login + '%', )
        self.db.cur.execute('''SELECT * FROM workers WHERE worker_login LIKE ?''', worker_login)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def default_data(self):
        try:
            self.entry_worker_name.delete(0, END)
            self.entry_worker_surname.delete(0, END)
            self.entry_worker_login.delete(0, END)
            self.entry_worker_pass.delete(0, END)
            self.entry_worker_title.delete(0, END)
            self.db.cur.execute('''SELECT * FROM workers WHERE id=?''',
                                (self.tree.set(self.tree.selection()[0], '#1'), ))
            row = self.db.cur.fetchone()
            self.entry_worker_name.insert(0, row[1])
            self.entry_worker_surname.insert(0, row[2])
            self.entry_worker_login.insert(0, row[3])
            self.entry_worker_pass.insert(0, row[4])
            self.entry_worker_title.insert(0, row[5])
            self.save_worker_btn.place_forget()
            self.save_edited_info.place(relx=0.35, rely=0.48, relwidth=spec_relw)
        except IndexError:
            self.lbl_worker_result.config(text='You have not selected the worker')

    def edit_record(self, worker_name, worker_surname, worker_login, worker_pass, worker_title):
        if self.entry_worker_name.index('end') != 0 and self.entry_worker_surname.index('end') != 0 and \
                self.entry_worker_login.index('end') != 0 and self.entry_worker_pass.index('end') != 0\
                and self.entry_worker_title.index('end') != 0:
            self.db.cur.execute('''UPDATE workers SET worker_name=?, worker_surname=?, worker_login=?, worker_pass=?, worker_title=? WHERE ID=?''',
                                (worker_name, worker_surname, worker_login, worker_pass, worker_title,
                                 self.tree.set(self.tree.selection()[0], '#1')))
            self.db.con.commit()
            self.entry_worker_name.delete(0, END)
            self.entry_worker_surname.delete(0, END)
            self.entry_worker_login.delete(0, END)
            self.entry_worker_pass.delete(0, END)
            self.entry_worker_title.delete(0, END)
            self.view_workers()
            self.save_edited_info.place_forget()
            self.save_worker_btn.place(relx=0.35, rely=0.48, relwidth=spec_relw)
        else:
            self.lbl_worker_result.config(text='Some info is not given, check out all empty entries')

    @staticmethod
    def open_admin():
        AdminFrame()

    @staticmethod
    def open_search_worker():
        SearchWorker()


class SearchWorker(Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search_worker()
        self.worker = WorkerFrame()

    def init_search_worker(self):
        self.title('Search')
        self.width_window = 300
        self.height_window = 100
        self.width_screen = win.winfo_screenwidth()
        self.height_screen = win.winfo_screenheight()
        self.x_center = int(self.width_screen / 2 - self.width_window / 2)
        self.y_center = int(self.height_screen / 2 - self.height_window / 2)
        self.geometry(f'{self.width_window}x{self.height_window}+{self.x_center}+{self.y_center}')
        self.resizable(False, False)

        label_search = Label(self, text='Search')
        label_search.place(relx=0.166, rely=0.2)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(relx=0.35, rely=0.2, relwidth=0.5)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(relx=0.61, rely=0.6)

        btn_search = ttk.Button(self, text='Search')
        btn_search.place(relx=0.28, rely=0.6)
        btn_search.bind('<Button-1>', lambda event: self.worker.search_workers(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

        self.grab_set()
        self.focus_set()


class CashierFrame(Frame):
    def __init__(self):
        super().__init__()
        self.init_cashier()

    def init_cashier(self):
        cashier = ttk.Frame(width=800, height=800, style='Card.TFrame')
        cashier.place(x=0, y=0)

        global auth_worker_name
        lbl_auth_worker = ttk.Label(cashier, text=f'Welcome, {auth_worker_name}', font=('Comic Sans MS', '16'))
        lbl_auth_worker.place(relx=0.5, rely=0.3, anchor=CENTER)

        customer_btn = ttk.Button(cashier, text='Customer register', command=self.open_customer)
        customer_btn.place(relx=0.5, rely=0.4, anchor=CENTER, relwidth=0.16)

        ticket_btn = ttk.Button(cashier, text='Make an order', command=self.open_ticket)
        ticket_btn.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.16)

        bills_btn = ttk.Button(cashier, text='View bills', command=self.open_bills)
        bills_btn.place(relx=0.5, rely=0.6, anchor=CENTER, relwidth=0.16)

        log_out_btn = ttk.Button(cashier, text='log out', command=self.log_out)
        log_out_btn.place(relx=0.01, rely=0.95)

    @staticmethod
    def open_customer():
        CustomerFrame()

    @staticmethod
    def open_ticket():
        TicketFrame()

    @staticmethod
    def open_bills():
        BillsFrame()

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
        customer = ttk.Frame(width=800, height=800, style='Card.TFrame')
        customer.place(x=0, y=0)

        lbl_login = Label(customer, text='Login')
        self.entry_login = ttk.Entry(customer)

        lbl_login.place(relx=0.35, rely=0.04, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_login.place(relx=0.35, rely=0.08, relheight=spec_relh, relwidth=spec_relw)

        lbl_name = Label(customer, text='Name')
        self.entry_name = ttk.Entry(customer)

        lbl_name.place(relx=0.35, rely=0.13, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_name.place(relx=0.35, rely=0.17, relheight=spec_relh, relwidth=spec_relw)

        lbl_surname = Label(customer, text='Surname')
        self.entry_surname = ttk.Entry(customer)

        lbl_surname.place(relx=0.35, rely=0.22, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_surname.place(relx=0.35, rely=0.26, relheight=spec_relh, relwidth=spec_relw)

        lbl_age = Label(customer, text='Age')
        self.entry_age = ttk.Entry(customer)

        lbl_age.place(relx=0.35, rely=0.31, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_age.place(relx=0.35, rely=0.35, relheight=spec_relh, relwidth=spec_relw)

        lbl_email = Label(customer, text='Email')
        self.entry_email = ttk.Entry(customer)

        lbl_email.place(relx=0.35, rely=0.4, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_email.place(relx=0.35, rely=0.44, relheight=spec_relh, relwidth=spec_relw)

        self.save_cust_btn = ttk.Button(customer, text='save')
        self.save_cust_btn.place(relx=0.35, rely=0.53, relwidth=spec_relw)
        self.save_cust_btn.bind('<Button-1>', lambda event: self.customer_record(self.entry_login.get(),
                                                                            self.entry_name.get(),
                                                                            self.entry_surname.get(),
                                                                            self.entry_age.get(),
                                                                            self.entry_email.get()))

        self.save_edited_info = ttk.Button(customer, text='edit')
        self.save_edited_info.bind('<Button-1>', lambda event: self.edit_record(self.entry_login.get(),
                                                                                self.entry_name.get(),
                                                                                self.entry_surname.get(),
                                                                                self.entry_age.get(),
                                                                                self.entry_email.get()))



        self.customer_search_img = PhotoImage(file='icons/search.png')
        customer_search = ttk.Button(customer, image=self.customer_search_img, command=self.open_search_customer)
        customer_search.place(relx=0.91, rely=0.6, width=55, height=55)

        self.customer_refresh_img = PhotoImage(file='icons/refresh.png')
        customer_refresh = ttk.Button(customer, image=self.customer_refresh_img, command=self.view_customers)
        customer_refresh.place(relx=0.91, rely=0.69, width=55, height=55)

        self.customer_edit_img = PhotoImage(file='icons/clock_update.png')
        customer_edit_btn = ttk.Button(customer, image=self.customer_edit_img, command=self.default_data)
        customer_edit_btn.place(relx=0.91, rely=0.78, width=55, height=55)

        self.customer_delete_img = PhotoImage(file='icons/delete.png')
        delete_customer_btn = ttk.Button(customer, image=self.customer_delete_img, command=self.delete_records)
        delete_customer_btn.place(relx=0.91, rely=0.87, width=55, height=55)

        self.lbl_cust_result = Label(customer, text='')
        self.lbl_cust_result.place(relx=0.25, rely=0.49, relwidth=0.5)

        self.tree = ttk.Treeview(customer, height=10, columns=('ID', 'customer_login', 'customer_name',
                                                               'customer_surname', 'customer_age', 'customer_email'),
                                 show='headings')

        self.tree.column('ID', width=30, anchor=CENTER)
        self.tree.column('customer_login', width=110, anchor=CENTER)
        self.tree.column('customer_name', width=110, anchor=CENTER)
        self.tree.column('customer_surname', width=110, anchor=CENTER)
        self.tree.column('customer_age', width=100, anchor=CENTER)
        self.tree.column('customer_email', width=170, anchor=CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('customer_name', text='Customer name')
        self.tree.heading('customer_surname', text='Customer surname')
        self.tree.heading('customer_login', text='Customer login')
        self.tree.heading('customer_age', text='Customer age')
        self.tree.heading('customer_email', text='Customer email')

        self.tree.place(relx=0.042, rely=0.6)

        scroll = ttk.Scrollbar(customer, command=self.tree.yview)
        scroll.place(relx=0.9, rely=0.77, relheight=0.33, anchor=E)
        self.tree.configure(yscrollcommand=scroll.set)

        main_btn = ttk.Button(customer, text='back to main page', command=self.open_cashier)
        main_btn.place(relx=0.01, rely=0.95)

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

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute('''DELETE FROM customers WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_customers()

    def search_customers(self, customer_login):
        customer_login = ('%' + customer_login + '%', )
        self.db.cur.execute('''SELECT * FROM customers WHERE customer_login LIKE ?''', customer_login)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def default_data(self):
        try:
            self.entry_login.delete(0, END)
            self.entry_name.delete(0, END)
            self.entry_surname.delete(0, END)
            self.entry_age.delete(0, END)
            self.entry_email.delete(0, END)
            self.db.cur.execute('''SELECT * FROM customers WHERE id=?''',
                                (self.tree.set(self.tree.selection()[0], '#1'), ))
            row = self.db.cur.fetchone()
            self.entry_login.insert(0, row[1])
            self.entry_name.insert(0, row[2])
            self.entry_surname.insert(0, row[3])
            self.entry_age.insert(0, row[4])
            self.entry_email.insert(0, row[5])
            self.save_cust_btn.place_forget()
            self.save_edited_info.place(relx=0.35, rely=0.53, relwidth=spec_relw)
        except IndexError:
            self.lbl_cust_result.config(text='You have not selected the customer')

    def edit_record(self, customer_login, customer_name, customer_surname, customer_age, customer_email):
        if self.entry_login.index('end') != 0 and self.entry_name.index('end') != 0 and \
                self.entry_surname.index('end') != 0 and self.entry_age.index('end') != 0\
                and self.entry_email.index('end') != 0:
            self.db.cur.execute('''UPDATE customers SET customer_login=?, customer_name=?, customer_surname=?, customer_age=?, customer_email=? WHERE ID=?''',
                                (customer_login, customer_name, customer_surname, customer_age, customer_email,
                                 self.tree.set(self.tree.selection()[0], '#1')))
            self.db.con.commit()
            self.entry_login.delete(0, END)
            self.entry_name.delete(0, END)
            self.entry_surname.delete(0, END)
            self.entry_age.delete(0, END)
            self.entry_email.delete(0, END)
            self.view_customers()
            self.save_edited_info.place_forget()
            self.save_cust_btn.place(relx=0.35, rely=0.53, relwidth=spec_relw)
        else:
            self.lbl_cust_result.config(text='Some info is not given, check out all empty entries')

    @staticmethod
    def open_search_customer():
        SearchCustomer()

    @staticmethod
    def open_cashier():
        CashierFrame()


class SearchCustomer(Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search_customer()
        self.customer = CustomerFrame()

    def init_search_customer(self):
        self.title('Search')
        self.width_window = 300
        self.height_window = 100
        self.width_screen = win.winfo_screenwidth()
        self.height_screen = win.winfo_screenheight()
        self.x_center = int(self.width_screen / 2 - self.width_window / 2)
        self.y_center = int(self.height_screen / 2 - self.height_window / 2)
        self.geometry(f'{self.width_window}x{self.height_window}+{self.x_center}+{self.y_center}')
        self.resizable(False, False)

        label_search = Label(self, text='Search')
        label_search.place(relx=0.166, rely=0.2)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(relx=0.35, rely=0.2, relwidth=0.5)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(relx=0.61, rely=0.6)

        btn_search = ttk.Button(self, text='Search')
        btn_search.place(relx=0.28, rely=0.6)
        btn_search.bind('<Button-1>', lambda event: self.customer.search_customers(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

        self.grab_set()
        self.focus_set()


class TicketFrame(Frame):
    def __init__(self):
        super().__init__()
        self.init_ticket()
        self.db = db
        self.view_customers()
        self.view_cinemas()

    def init_ticket(self):
        ticket = ttk.Frame(width=800, height=800, style='Card.TFrame')
        ticket.place(x=0, y=0)

        self.customers_tree = ttk.Treeview(ticket, height=720, columns='customer_login', show='headings')

        self.customers_tree.column('customer_login', width=150, anchor=CENTER)

        self.customers_tree.heading('customer_login', text='Customer login')

        self.customers_tree.place(relx=0, rely=0, relheight=0.998)

        self.cinemas_tree = ttk.Treeview(ticket, height=720, columns=('id', 'film_name', 'scheduled_time', 'cinema_hall'),
                                         show='headings')

        self.cinemas_tree.column('id', width=40, anchor=CENTER)
        self.cinemas_tree.column('film_name', width=175, anchor=CENTER)
        self.cinemas_tree.column('scheduled_time', width=40, anchor=CENTER)
        self.cinemas_tree.column('cinema_hall', width=95, anchor=CENTER)

        self.cinemas_tree.heading('id', text='id')
        self.cinemas_tree.heading('film_name', text='Film name')
        self.cinemas_tree.heading('scheduled_time', text='Scheduled time')
        self.cinemas_tree.heading('cinema_hall', text='Cinema hall')

        self.cinemas_tree.place(relx=0.5, rely=0, relheight=0.998)

        self.lbl_customer_login = Label(ticket, text='Customer login')
        self.entry_customer_login = ttk.Entry(ticket)

        self.lbl_customer_login.place(relx=0.26, rely=0.06, relwidth=0.225)
        self.entry_customer_login.place(relx=0.26, rely=0.09, relheight=spec_relh, relwidth=0.23)

        lbl_film_name = Label(ticket, text='Film name')
        self.entry_film_name = ttk.Entry(ticket)

        lbl_film_name.place(relx=0.26, rely=0.14, relwidth=0.225)
        self.entry_film_name.place(relx=0.26, rely=0.17, relheight=spec_relh, relwidth=0.23)

        lbl_sch_time = Label(ticket, text='Scheduled time')
        self.entry_sch_time = ttk.Entry(ticket)

        lbl_sch_time.place(relx=0.26, rely=0.22, relwidth=0.225)
        self.entry_sch_time.place(relx=0.26, rely=0.25, relheight=spec_relh, relwidth=0.23)

        lbl_cinema_hall = Label(ticket, text='Cinema hall')
        self.entry_cinema_hall = ttk.Entry(ticket)

        lbl_cinema_hall.place(relx=0.26, rely=0.3, relwidth=0.225)
        self.entry_cinema_hall.place(relx=0.26, rely=0.33, relheight=spec_relh, relwidth=0.23)

        lbl_place_level = Label(ticket, text='Place level')
        self.combo_place_level = ttk.Combobox(ticket, state='readonly', values=('economy', 'comfort', 'vip'))
        self.combo_place_level.bind('<<ComboboxSelected>>', lambda _: self.get_price_by_combobox())

        lbl_place_level.place(relx=0.26, rely=0.38, relwidth=0.225)
        self.combo_place_level.place(relx=0.26, rely=0.41, relheight=0.05, relwidth=0.23)

        lbl_price = Label(ticket, text='Price')
        self.price_stringvar = StringVar()
        self.entry_price = ttk.Entry(ticket, textvariable=self.price_stringvar, state=DISABLED)

        lbl_price.place(relx=0.26, rely=0.46, relwidth=0.225)
        self.entry_price.place(relx=0.26, rely=0.49, relheight=spec_relh, relwidth=0.23)

        lbl_quantity = Label(ticket, text='Quantity')
        self.entry_quantity = ttk.Entry(ticket)

        lbl_quantity.place(relx=0.26, rely=0.54, relwidth=0.225)
        self.entry_quantity.place(relx=0.26, rely=0.57, relheight=spec_relh, relwidth=0.23)

        lbl_total = Label(ticket, text='Total')
        self.total_stringvar = StringVar()
        self.entry_total = ttk.Entry(ticket, state=DISABLED, textvariable=self.total_stringvar)

        lbl_total.place(relx=0.26, rely=0.62, relwidth=0.225)
        self.entry_total.place(relx=0.26, rely=0.65, relheight=spec_relh, relwidth=0.23)

        self.select_for_cust_btn = ttk.Button(ticket, text='select', command=lambda: self.select_from_trees_for_cust())
        self.select_for_cust_btn.place(relx=0.275, rely=0.75, relwidth=0.2)

        self.select_for_guest_btn = ttk.Button(ticket, text='select', command=lambda: self.select_from_trees_for_guest())

        self.buy_as_cust_btn = ttk.Button(ticket, text='buy', state=DISABLED, command=lambda: self.buy_a_ticket_as_cust())
        self.buy_as_cust_btn.place(relx=0.275, rely=0.8, relwidth=0.2)

        self.buy_as_guest_btn = ttk.Button(ticket, text='buy', state=DISABLED, command=lambda: self.buy_a_ticket_as_guest())

        self.lbl_ticket_result = ttk.Label(ticket, text='')
        self.lbl_ticket_result.place(relx=0.275, rely=0.85, relwidth=0.225)

        self.as_guest_btn = ttk.Button(ticket, text='switch to guest', command=lambda: self.switch_to_guest())
        self.as_guest_btn.place(relx=0.275, rely=0.909, relwidth=0.2)

        self.as_cust_btn = ttk.Button(ticket, text='switch to customer', command=lambda: self.switch_to_customer())

        self.reset_entries_btn = ttk.Button(ticket, text='reset', command=lambda: self.reset_entries())
        self.reset_entries_btn.place(relx=0.275, rely=0.01, relwidth=0.2)

        main_btn = ttk.Button(ticket, text='back to main page', command=self.open_cashier)
        main_btn.place(relx=0.275, rely=0.959, relwidth=0.2)

    def view_customers(self):
        self.db.cur.execute('''SELECT customer_login FROM customers''')
        [self.customers_tree.delete(i) for i in self.customers_tree.get_children()]
        [self.customers_tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def view_cinemas(self):
        self.db.cur.execute('''SELECT id, film_name, scheduled_time, cinema_hall FROM cinemas ORDER BY scheduled_time ASC''')
        [self.cinemas_tree.delete(i) for i in self.cinemas_tree.get_children()]
        [self.cinemas_tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def select_from_trees_for_cust(self):
        try:
            self.lbl_ticket_result.config(text='')
            self.entry_customer_login.delete(0, END)
            self.entry_film_name.delete(0, END)
            self.entry_sch_time.delete(0, END)
            self.entry_cinema_hall.delete(0, END)
            self.entry_price.delete(0, END)
            self.db.cur.execute('''SELECT customer_login FROM customers WHERE customer_login=?''',
                                (self.customers_tree.set(self.customers_tree.selection()[0], '#1'), ))
            customer_login_row = self.db.cur.fetchone()[0]
            self.db.cur.execute('''SELECT film_name, scheduled_time, cinema_hall FROM cinemas WHERE id=?''',
                                (self.cinemas_tree.set(self.cinemas_tree.selection()[0], '#1'), ))
            cinema_row = self.db.cur.fetchone()
            self.entry_customer_login.insert(0, customer_login_row)
            self.entry_film_name.insert(0, cinema_row[0])
            self.entry_sch_time.insert(0, cinema_row[1])
            self.entry_cinema_hall.insert(0, cinema_row[2])
            price = int(self.entry_price.get())
            qt = int(self.entry_quantity.get())
            total = price*qt
            self.total_stringvar.set(str(total))
        except (IndexError, ValueError) as e:
            self.lbl_ticket_result.config(text='Some info is not given')

    def get_price_by_combobox(self):
        if self.combo_place_level.get() == 'economy':
            self.entry_price.delete(0, END)
            self.price_stringvar.set(eco_price)
            self.buy_as_cust_btn['state'] = 'normal'
            self.buy_as_guest_btn['state'] = 'normal'
        elif self.combo_place_level.get() == 'comfort':
            self.entry_price.delete(0, END)
            self.price_stringvar.set(comf_price)
            self.buy_as_cust_btn['state'] = 'normal'
            self.buy_as_guest_btn['state'] = 'normal'
        elif self.combo_place_level.get() == 'vip':
            self.entry_price.delete(0, END)
            self.price_stringvar.set(vip_price)
            self.buy_as_cust_btn['state'] = 'normal'
            self.buy_as_guest_btn['state'] = 'normal'

    def select_from_trees_for_guest(self):
        try:
            self.lbl_ticket_result.config(text='')
            self.entry_film_name.delete(0, END)
            self.entry_sch_time.delete(0, END)
            self.entry_cinema_hall.delete(0, END)
            self.entry_price.delete(0, END)
            self.db.cur.execute('''SELECT film_name, scheduled_time, cinema_hall FROM cinemas WHERE id=?''',
                                (self.cinemas_tree.set(self.cinemas_tree.selection()[0], '#1'), ))
            cinema_row = self.db.cur.fetchone()
            self.entry_film_name.insert(0, cinema_row[0])
            self.entry_sch_time.insert(0, cinema_row[1])
            self.entry_cinema_hall.insert(0, cinema_row[2])
            price = int(self.entry_price.get())
            qt = int(self.entry_quantity.get())
            total = price * qt
            self.total_stringvar.set(str(total))
        except (IndexError, ValueError) as e:
            self.lbl_ticket_result.config(text='Some info is not given')

    def switch_to_guest(self):
        self.lbl_customer_login.place_forget()
        self.entry_customer_login.place_forget()
        self.customers_tree.place_forget()
        self.as_guest_btn.place_forget()
        self.buy_as_cust_btn.place_forget()
        self.as_cust_btn.place(relx=0.275, rely=0.909, relwidth=0.2)
        self.select_for_guest_btn.place(relx=0.275, rely=0.75, relwidth=0.2)
        self.buy_as_guest_btn.place(relx=0.275, rely=0.8, relwidth=0.2)
        self.buy_as_guest_btn['state'] = 'disabled'
        self.combo_place_level.set('')

    def switch_to_customer(self):
        self.lbl_customer_login.place(relx=0.26, rely=0.06, relwidth=0.225)
        self.entry_customer_login.place(relx=0.26, rely=0.09, relheight=spec_relh, relwidth=0.23)
        self.customers_tree.place(relx=0, rely=0)
        self.as_cust_btn.place_forget()
        self.buy_as_guest_btn.place_forget()
        self.as_guest_btn.place(relx=0.275, rely=0.909, relwidth=0.2)
        self.select_for_cust_btn.place(relx=0.275, rely=0.75, relwidth=0.2)
        self.buy_as_cust_btn.place(relx=0.275, rely=0.8, relwidth=0.2)
        self.buy_as_cust_btn['state'] = 'disabled'
        self.combo_place_level.set('')

    def reset_entries(self):
        self.entry_customer_login.delete(0, END)
        self.entry_film_name.delete(0, END)
        self.entry_sch_time.delete(0, END)
        self.entry_cinema_hall.delete(0, END)
        self.lbl_ticket_result.config(text='')
        self.combo_place_level.set('')
        self.entry_price['state'] = 'normal'
        self.entry_price.delete(0, END)
        self.entry_price['state'] = 'disabled'
        self.entry_quantity.delete(0, END)
        self.entry_total['state'] = 'normal'
        self.entry_total.delete(0, END)
        self.entry_total['state'] = 'disabled'

    def buy_a_ticket_as_cust(self):
        if self.entry_customer_login.index('end') != 0 and self.entry_film_name.index('end') != 0 \
                    and self.entry_sch_time.index('end') != 0 and self.entry_cinema_hall.index('end') != 0\
                and self.entry_quantity.index('end') != 0 and self.entry_total.index('end') != 0:
            if self.combo_place_level.get() == 'economy':
                self.db.cur.execute(f"SELECT economy FROM cinemas WHERE film_name='{self.entry_film_name.get()}' AND scheduled_time='{self.entry_sch_time.get()}'")
            elif self.combo_place_level.get() == 'comfort':
                self.db.cur.execute(f"SELECT comfort FROM cinemas WHERE film_name='{self.entry_film_name.get()}' AND scheduled_time='{self.entry_sch_time.get()}'")
            elif self.combo_place_level.get() == 'vip':
                self.db.cur.execute(f"SELECT vip FROM cinemas WHERE film_name='{self.entry_film_name.get()}' AND scheduled_time='{self.entry_sch_time.get()}'")
            free_places = self.db.cur.fetchone()[0]
            required_places = int(self.entry_quantity.get())
            if required_places <= free_places:
                free_places -= required_places
                if self.combo_place_level.get() == 'economy':
                    self.db.cur.execute('''UPDATE cinemas SET economy=? WHERE id=?''',
                                        (free_places, self.cinemas_tree.set(self.cinemas_tree.selection()[0], '#1')))
                elif self.combo_place_level.get() == 'comfort':
                    self.db.cur.execute('''UPDATE cinemas SET comfort=? WHERE id=?''',
                                        (free_places, self.cinemas_tree.set(self.cinemas_tree.selection()[0], '#1')))
                elif self.combo_place_level.get() == 'vip':
                    self.db.cur.execute('''UPDATE cinemas SET vip=? WHERE id=?''',
                                        (free_places, self.cinemas_tree.set(self.cinemas_tree.selection()[0], '#1')))
                temp_bill = Bill(self.entry_customer_login.get(), self.entry_film_name.get(), self.entry_sch_time.get(),
                                 self.combo_place_level.get(), self.entry_price.get(), self.entry_quantity.get(),
                                 self.entry_total.get())
                self.db.insert_bill_data(temp_bill.get_login(), temp_bill.get_film_name(), temp_bill.get_time(),
                                         temp_bill.get_place_level(), temp_bill.get_price(), temp_bill.get_quantity(),
                                         temp_bill.get_total())
                self.reset_entries()
            else:
                self.lbl_ticket_result.config(text='There is not enough tickets in this category')
        else:
            self.lbl_ticket_result.config(text='Some entries are empty')

    def buy_a_ticket_as_guest(self):
        if self.entry_film_name.index('end') != 0 and self.entry_sch_time.index('end') != 0\
                and self.entry_cinema_hall.index('end') != 0 and self.entry_quantity.index('end') != 0\
                and self.entry_total.index('end') != 0:
            if self.combo_place_level.get() == 'economy':
                self.db.cur.execute(f"SELECT economy FROM cinemas WHERE film_name='{self.entry_film_name.get()}' AND scheduled_time='{self.entry_sch_time.get()}'")
            elif self.combo_place_level.get() == 'comfort':
                self.db.cur.execute(f"SELECT comfort FROM cinemas WHERE film_name='{self.entry_film_name.get()}' AND scheduled_time='{self.entry_sch_time.get()}'")
            elif self.combo_place_level.get() == 'vip':
                self.db.cur.execute(f"SELECT vip FROM cinemas WHERE film_name='{self.entry_film_name.get()}' AND scheduled_time='{self.entry_sch_time.get()}'")
            free_places = self.db.cur.fetchone()[0]
            required_places = int(self.entry_quantity.get())
            if required_places <= free_places:
                free_places -= required_places
                if self.combo_place_level.get() == 'economy':
                    self.db.cur.execute('''UPDATE cinemas SET economy=? WHERE id=?''',
                                        (free_places, self.cinemas_tree.set(self.cinemas_tree.selection()[0], '#1')))
                elif self.combo_place_level.get() == 'comfort':
                    self.db.cur.execute('''UPDATE cinemas SET comfort=? WHERE id=?''',
                                        (free_places, self.cinemas_tree.set(self.cinemas_tree.selection()[0], '#1')))
                elif self.combo_place_level.get() == 'vip':
                    self.db.cur.execute('''UPDATE cinemas SET vip=? WHERE id=?''',
                                        (free_places, self.cinemas_tree.set(self.cinemas_tree.selection()[0], '#1')))
                temp_bill = Bill('Guest', self.entry_film_name.get(), self.entry_sch_time.get(),
                                 self.combo_place_level.get(), self.entry_price.get(), self.entry_quantity.get(),
                                 self.entry_total.get())
                self.db.insert_bill_data(temp_bill.get_login(), temp_bill.get_film_name(), temp_bill.get_time(),
                                         temp_bill.get_place_level(), temp_bill.get_price(), temp_bill.get_quantity(),
                                         temp_bill.get_total())
                self.reset_entries()
            else:
                self.lbl_ticket_result.config(text='There is not enough tickets')
        else:
            self.lbl_ticket_result.config(text='Some entries are empty')

    @staticmethod
    def open_cashier():
        CashierFrame()


class BillsFrame(Frame):
    def __init__(self):
        super().__init__()
        self.init_bills()
        self.db = db
        self.view_bills()

    def init_bills(self):
        bills = ttk.Frame(width=800, height=800, style='Card.TFrame')
        bills.place(x=0, y=0)

        self.bills_tree = ttk.Treeview(bills, height=720, columns=('id', 'customer_login', 'film_name',
                                                                   'scheduled_time', 'place_level', 'ticket_price',
                                                                   'quantity', 'total'), show='headings')

        self.bills_tree.column('id', width=40, anchor=CENTER)
        self.bills_tree.column('customer_login', width=120, anchor=CENTER)
        self.bills_tree.column('film_name', width=175, anchor=CENTER)
        self.bills_tree.column('scheduled_time', width=40, anchor=CENTER)
        self.bills_tree.column('place_level', width=80, anchor=CENTER)
        self.bills_tree.column('ticket_price', width=75, anchor=CENTER)
        self.bills_tree.column('quantity', width=55, anchor=CENTER)
        self.bills_tree.column('total', width=100, anchor=CENTER)

        self.bills_tree.heading('id', text='id')
        self.bills_tree.heading('customer_login', text='Customer login')
        self.bills_tree.heading('film_name', text='Film name')
        self.bills_tree.heading('scheduled_time', text='Scheduled time')
        self.bills_tree.heading('place_level', text='Place level')
        self.bills_tree.heading('ticket_price', text='Ticket price')
        self.bills_tree.heading('quantity', text='Quantity')
        self.bills_tree.heading('total', text='Total')

        self.bills_tree.place(relx=0.04, rely=0.25, relheight=0.5)

        main_btn = ttk.Button(bills, text='back to main page', command=self.open_cashier)
        main_btn.place(relx=0.01, rely=0.95)

    def view_bills(self):
        self.db.cur.execute('''SELECT id, customer_login, film_name, scheduled_time, place_level, ticket_price, quantity, total FROM bills''')
        [self.bills_tree.delete(i) for i in self.bills_tree.get_children()]
        [self.bills_tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def search_bills(self, customer_login):
        customer_login = ('%' + customer_login + '%', )
        self.db.cur.execute('''SELECT * FROM bills WHERE customer_login LIKE ?''', customer_login)
        [self.bills_tree.delete(i) for i in self.bills_tree.get_children()]
        [self.bills_tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    @staticmethod
    def open_cashier():
        CashierFrame()


class SearchBill(Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search_bill()
        self.bill = BillsFrame()

    def init_search_bill(self):
        self.title('Search')
        self.width_window = 300
        self.height_window = 100
        self.width_screen = win.winfo_screenwidth()
        self.height_screen = win.winfo_screenheight()
        self.x_center = int(self.width_screen / 2 - self.width_window / 2)
        self.y_center = int(self.height_screen / 2 - self.height_window / 2)
        self.geometry(f'{self.width_window}x{self.height_window}+{self.x_center}+{self.y_center}')
        self.resizable(False, False)

        label_search = Label(self, text='Search')
        label_search.place(relx=0.166, rely=0.2)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(relx=0.35, rely=0.2, relwidth=0.5)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(relx=0.61, rely=0.6)

        btn_search = ttk.Button(self, text='Search')
        btn_search.place(relx=0.28, rely=0.6)
        btn_search.bind('<Button-1>', lambda event: self.bill.search_bills(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

        self.grab_set()
        self.focus_set()


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
            cinema_hall text,
            economy integer,
            comfort integer,
            vip integer)''')
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS bills(
            id integer primary key,
            customer_login text,
            film_name text, 
            scheduled_time text, 
            place_level text,
            ticket_price text,
            quantity text,
            total text)''')
        self.con.commit()

    def insert_hall_data(self, hall_name, economy, comfort, vip):
        self.cur.execute('''INSERT INTO halls (hall_name, economy, comfort, vip) VALUES (?, ?, ?, ?)''',
                         (hall_name, economy, comfort, vip))
        self.con.commit()

    def insert_cinema_data(self, film_name, scheduled_time, cinema_hall):
        self.cur.execute(f"SELECT economy, comfort, vip FROM halls WHERE hall_name='{cinema_hall}'")
        row = self.cur.fetchall()[0]
        economy = row[0]
        comfort = row[1]
        vip = row[2]
        self.cur.execute('''INSERT INTO cinemas (film_name, scheduled_time, cinema_hall, economy, comfort, vip) VALUES (?, ?, ?, ?, ?, ?)''',
                         (film_name, scheduled_time, cinema_hall, economy, comfort, vip))
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

    def insert_bill_data(self, customer_login, film_name, scheduled_time, place_level, ticket_price, quantity, total):
        self.cur.execute('''INSERT INTO bills (customer_login, film_name, scheduled_time, place_level, ticket_price, quantity, total) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                         (customer_login, film_name, scheduled_time, place_level, ticket_price, quantity, total))
        self.con.commit()


if __name__ == '__main__':
    win = Tk()
    win.call('source', 'azure.tcl')
    win.call('set_theme', 'dark')
    db = DB()
    app = Main()
    win.title('Cinema Theatre')
    width_window = 800
    height_window = 800
    width_screen = win.winfo_screenwidth()
    height_screen = win.winfo_screenheight()
    x_center = int(width_screen / 2 - width_window / 2)
    y_center = int(height_screen / 2 - height_window / 2)
    win.geometry(f'{width_window}x{height_window}+{x_center}+{y_center}')
    win.resizable(False, False)
    win.mainloop()
