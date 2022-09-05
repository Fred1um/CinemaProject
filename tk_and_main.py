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


class AuthFrame(Frame):
    def __init__(self):
        super().__init__()
        self.login_frame_const()
        self.db = db

    def login_frame_const(self):
        login_frame = ttk.Frame(width=800, height=800, style='Card.TFrame')
        login_frame.place(x=0, y=0)

        lbl_user_login = Label(login_frame, text='Login')
        self.entry_user_login = ttk.Entry(login_frame)

        lbl_user_login.place(relx=0.35, rely=0.37, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_user_login.place(relx=0.35, rely=0.41, relheight=spec_relh, relwidth=spec_relw)

        lbl_user_password = Label(login_frame, text='Password')
        self.entry_user_password = ttk.Entry(login_frame, show='*')

        lbl_user_password.place(relx=0.35, rely=0.46, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_user_password.place(relx=0.35, rely=0.5, relheight=spec_relh, relwidth=spec_relw)

        signin_save_btn = ttk.Button(login_frame, text='sign in', command=self.login_func)
        signin_save_btn.place(relx=0.45, rely=0.565, relwidth=0.1, relheight=0.05)

        self.lbl_signin_result = Label(login_frame, text='')
        self.lbl_signin_result.place(relx=0.35, rely=0.62, relheight=lbl_relh, relwidth=spec_relw)

    def login_func(self):
        auth_worker_login = self.entry_user_login.get()
        auth_worker_password = self.entry_user_password.get()
        self.db.cur.execute(
            f"SELECT worker_login, worker_pass FROM workers WHERE worker_login = '{auth_worker_login}' AND worker_pass = '{auth_worker_password}'")
        self.db.con.commit()
        if not self.db.cur.fetchone():
            self.lbl_signin_result.config(text='Not found')
        else:
            self.db.cur.execute(
                f"SELECT worker_title FROM workers WHERE worker_login = '{auth_worker_login}' AND worker_pass = '{auth_worker_password}'")
            auth_worker_title = self.db.cur.fetchone()[0]
            self.db.cur.execute(
                f"SELECT worker_name FROM workers WHERE worker_login = '{auth_worker_login}' AND worker_pass = '{auth_worker_password}'")
            self.db.con.commit()
            global auth_worker_name
            auth_worker_name = self.db.cur.fetchone()[0]
            if auth_worker_title == 'admin':
                self.open_admin_frame()
            elif auth_worker_title == 'cashier':
                self.open_cashier_frame()

    @staticmethod
    def open_admin_frame():
        AdminFrame()

    @staticmethod
    def open_cashier_frame():
        CashierFrame()


class AdminFrame(Frame):
    def __init__(self):
        super().__init__()
        self.admin_frame_const()

    def admin_frame_const(self):
        admin_frame = ttk.Frame(width=800, height=800, style='Card.TFrame')
        admin_frame.place(x=0, y=0)

        global auth_worker_name
        lbl_auth_worker = ttk.Label(admin_frame, text=f'Welcome, {auth_worker_name}', font=('Comic Sans MS', '16'))
        lbl_auth_worker.place(relx=0.5, rely=0.3, anchor=CENTER)

        hall_btn = ttk.Button(admin_frame, text='Hall register', command=self.open_hall_frame)
        hall_btn.place(relx=0.5, rely=0.4, anchor=CENTER, relwidth=0.16)

        cin_btn = ttk.Button(admin_frame, text='Cinema register', command=self.open_cinema_frame)
        cin_btn.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.16)

        worker_reg_btn = ttk.Button(admin_frame, text='Worker register', command=self.open_worker_frame)
        worker_reg_btn.place(relx=0.5, rely=0.6, anchor=CENTER, relwidth=0.16)

        log_out_btn = ttk.Button(admin_frame, text='log out', command=self.log_out)
        log_out_btn.place(relx=0.01, rely=0.95)

    @staticmethod
    def open_hall_frame():
        HallFrame()

    @staticmethod
    def open_cinema_frame():
        CinemaFrame()

    @staticmethod
    def open_worker_frame():
        WorkerFrame()

    @staticmethod
    def log_out():
        AuthFrame()


class HallFrame(Frame):
    def __init__(self):
        super().__init__()
        self.hall_frame_const()
        self.db = db
        self.view_halls()

    def hall_frame_const(self):
        hall_frame = ttk.Frame(width=800, height=800, style='Card.TFrame')
        hall_frame.place(x=0, y=0)

        lbl_hall_name = Label(hall_frame, text='Hall name')
        self.entry_hall_name = ttk.Entry(hall_frame)

        lbl_hall_name.place(relx=0.35, rely=0.1, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_hall_name.place(relx=0.35, rely=0.14, relheight=spec_relh, relwidth=spec_relw)

        lbl_eco = Label(hall_frame, text='Economy places')
        self.entry_eco = ttk.Entry(hall_frame)

        lbl_eco.place(relx=0.35, rely=0.19, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_eco.place(relx=0.35, rely=0.23, relheight=spec_relh, relwidth=spec_relw)

        lbl_comf = Label(hall_frame, text='Comfort places')
        self.entry_comf = ttk.Entry(hall_frame)

        lbl_comf.place(relx=0.35, rely=0.28, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_comf.place(relx=0.35, rely=0.32, relheight=spec_relh, relwidth=spec_relw)

        lbl_vip = Label(hall_frame, text='VIP places')
        self.entry_vip = ttk.Entry(hall_frame)

        lbl_vip.place(relx=0.35, rely=0.37, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_vip.place(relx=0.35, rely=0.41, relheight=spec_relh, relwidth=spec_relw)

        self.save_hall_btn = ttk.Button(hall_frame, text='save')
        self.save_hall_btn.place(relx=0.35, rely=0.5, relwidth=spec_relw)
        self.save_hall_btn.bind('<Button-1>', lambda event: self.hall_record(self.entry_hall_name.get(),
                                                                             self.entry_eco.get(),
                                                                             self.entry_comf.get(),
                                                                             self.entry_vip.get()))

        self.save_edited_info = ttk.Button(hall_frame, text='edit')
        self.save_edited_info.bind('<Button-1>', lambda event: self.edit_record(self.entry_hall_name.get(),
                                                                                self.entry_eco.get(),
                                                                                self.entry_comf.get(),
                                                                                self.entry_vip.get()))

        self.lbl_hall_result = Label(hall_frame, text='', anchor=CENTER)
        self.lbl_hall_result.place(relx=0.25, rely=0.55, relwidth=0.5)

        self.hall_search_img = PhotoImage(file='icons/search.png')
        hall_search = ttk.Button(hall_frame, image=self.hall_search_img, command=self.open_search_hall)
        hall_search.place(relx=0.89, rely=0.6, width=55, height=55)

        self.hall_refresh = PhotoImage(file='icons/refresh.png')
        hall_refresh = ttk.Button(hall_frame, image=self.hall_refresh, command=self.view_halls)
        hall_refresh.place(relx=0.89, rely=0.69, width=55, height=55)

        self.hall_edit_img = PhotoImage(file='icons/clock_update.png')
        cinema_edit_btn = ttk.Button(hall_frame, image=self.hall_edit_img, command=self.hall_data)
        cinema_edit_btn.place(relx=0.89, rely=0.78,  width=55, height=55)

        self.delete_hall_img = PhotoImage(file='icons/delete.png')
        delete_hall_btn = ttk.Button(hall_frame, image=self.delete_hall_img, command=self.delete_halls)
        delete_hall_btn.place(relx=0.89, rely=0.87, width=55, height=55)

        self.halls_tree = ttk.Treeview(hall_frame, height=10, columns=('ID', 'hall_name', 'economy', 'comfort', 'vip'),
                                       show='headings')

        self.halls_tree.column('ID', width=30, anchor=CENTER)
        self.halls_tree.column('hall_name', width=200, anchor=CENTER)
        self.halls_tree.column('economy', width=100, anchor=CENTER)
        self.halls_tree.column('comfort', width=100, anchor=CENTER)
        self.halls_tree.column('vip', width=100, anchor=CENTER)

        self.halls_tree.heading('ID', text='ID')
        self.halls_tree.heading('hall_name', text='Hall name')
        self.halls_tree.heading('economy', text='Economy')
        self.halls_tree.heading('comfort', text='Comfort')
        self.halls_tree.heading('vip', text='VIP')

        self.halls_tree.place(relx=0.15, rely=0.6)

        self.halls_scroll = ttk.Scrollbar(hall_frame, command=self.halls_tree.yview)
        self.halls_scroll.place(relx=0.88, rely=0.77, relheight=0.33, anchor=E)
        self.halls_tree.configure(yscrollcommand=self.halls_scroll.set)

        main_btn = ttk.Button(hall_frame, text='back to main page', command=self.open_admin_frame)
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
        [self.halls_tree.delete(i) for i in self.halls_tree.get_children()]
        [self.halls_tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_halls(self):
        for selection_item in self.halls_tree.selection():
            self.db.cur.execute('''DELETE FROM halls WHERE id=?''', (self.halls_tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_halls()

    def search_halls(self, hall_name):
        hall_name = ('%' + hall_name + '%', )
        self.db.cur.execute('''SELECT * FROM halls WHERE hall_name LIKE ?''', hall_name)
        [self.halls_tree.delete(i) for i in self.halls_tree.get_children()]
        [self.halls_tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def hall_data(self):
        try:
            self.entry_hall_name.delete(0, END)
            self.entry_eco.delete(0, END)
            self.entry_comf.delete(0, END)
            self.entry_vip.delete(0, END)
            self.db.cur.execute('''SELECT * FROM halls WHERE id=?''',
                                (self.halls_tree.set(self.halls_tree.selection()[0], '#1'),))
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
                                (hall_name, economy, comfort, vip, self.halls_tree.set(self.halls_tree.selection()[0], '#1')))
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
    def open_admin_frame():
        AdminFrame()

    @staticmethod
    def open_search_hall():
        SearchHall()


class SearchHall(Toplevel):
    def __init__(self):
        super().__init__()
        self.search_hall_const()
        self.hall = HallFrame()

    def search_hall_const(self):
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
        self.cinema_frame_const()
        self.db = db
        self.view_cinemas()

    def cinema_frame_const(self):
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
        cinema_edit_btn = ttk.Button(cinema_frame, image=self.cinema_edit_img, command=self.cinema_data)
        cinema_edit_btn.place(relx=0.875, rely=0.78,  width=55, height=55)

        self.delete_cinema_img = PhotoImage(file='icons/delete.png')
        delete_cinema_btn = ttk.Button(cinema_frame, image=self.delete_cinema_img, command=self.delete_cinemas)
        delete_cinema_btn.place(relx=0.875, rely=0.87, width=55, height=55)

        self.cinemas_tree = ttk.Treeview(cinema_frame, height=10, columns=('ID', 'film_name', 'scheduled_time', 'cinema_hall'),
                                         show='headings')

        self.cinemas_tree.column('ID', width=30, anchor=CENTER)
        self.cinemas_tree.column('film_name', width=200, anchor=CENTER)
        self.cinemas_tree.column('scheduled_time', width=100, anchor=CENTER)
        self.cinemas_tree.column('cinema_hall', width=200, anchor=CENTER)

        self.cinemas_tree.heading('ID', text='ID')
        self.cinemas_tree.heading('film_name', text='Film name')
        self.cinemas_tree.heading('scheduled_time', text='Scheduled time')
        self.cinemas_tree.heading('cinema_hall', text='Cinema hall')

        self.cinemas_tree.place(relx=0.14, rely=0.6)

        self.cinemas_scroll = ttk.Scrollbar(cinema_frame, command=self.cinemas_tree.yview)
        self.cinemas_scroll.place(relx=0.865, rely=0.77, relheight=0.33, anchor=E)
        self.cinemas_tree.configure(yscrollcommand=self.cinemas_scroll.set)

        main_btn = ttk.Button(cinema_frame, text='back to main page', command=self.open_admin_frame)
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
        [self.cinemas_tree.delete(i) for i in self.cinemas_tree.get_children()]
        [self.cinemas_tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_cinemas(self):
        for selection_item in self.cinemas_tree.selection():
            self.db.cur.execute('''DELETE FROM cinemas WHERE id=?''', (self.cinemas_tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_cinemas()

    def search_cinemas(self, cinema_name):
        cinema_name = ('%' + cinema_name + '%', )
        self.db.cur.execute('''SELECT * FROM cinemas WHERE film_name LIKE ?''', cinema_name)
        [self.cinemas_tree.delete(i) for i in self.cinemas_tree.get_children()]
        [self.cinemas_tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def cinema_data(self):
        try:
            self.entry_film_name.delete(0, END)
            self.entry_sch_time.delete(0, END)
            self.entry_cinema_hall.delete(0, END)
            self.db.cur.execute('''SELECT * FROM cinemas WHERE id=?''',
                                (self.cinemas_tree.set(self.cinemas_tree.selection()[0], '#1'),))
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
                                    (film_name, scheduled_time, cinema_hall, self.cinemas_tree.set(self.cinemas_tree.selection()[0], '#1')))
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
    def open_admin_frame():
        AdminFrame()

    @staticmethod
    def open_search_cinema():
        SearchCinema()


class SearchCinema(Toplevel):
    def __init__(self):
        super().__init__()
        self.search_cinema_const()
        self.cinema = CinemaFrame()

    def search_cinema_const(self):
        self.title('Search')
        self.width_window = 300
        self.height_window = 100
        self.width_screen = win.winfo_screenwidth()
        self.height_screen = win.winfo_screenheight()
        self.x_center = int(self.width_screen / 2 - self.width_window / 2)
        self.y_center = int(self.height_screen / 2 - self.height_window / 2)
        self.geometry(f'{self.width_window}x{self.height_window}+{self.x_center}+{self.y_center}')
        self.resizable(False, False)

        lbl_search = Label(self, text='Search')
        lbl_search.place(relx=0.166, rely=0.2)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(relx=0.35, rely=0.2, relwidth=0.5)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(relx=0.61, rely=0.6)

        btn_search = ttk.Button(self, text='Search')
        btn_search.place(relx=0.28, rely=0.6)
        btn_search.bind('<Button-1>', lambda event: self.cinema.search_cinemas(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

        self.grab_set()
        self.focus_set()


class WorkerFrame(Frame):
    def __init__(self):
        super().__init__()
        self.worker_frame_const()
        self.db = db
        self.view_workers()

    def worker_frame_const(self):
        worker_frame = ttk.Frame(width=800, height=800, style='Card.TFrame')
        worker_frame.place(x=0, y=0)

        lbl_worker_name = Label(worker_frame, text='Name')
        self.entry_worker_name = ttk.Entry(worker_frame)

        lbl_worker_name.place(relx=0.35, rely=0, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_worker_name.place(relx=0.35, rely=0.04, relheight=spec_relh, relwidth=spec_relw)

        lbl_worker_surname = Label(worker_frame, text='Surname')
        self.entry_worker_surname = ttk.Entry(worker_frame)

        lbl_worker_surname.place(relx=0.35, rely=0.09, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_worker_surname.place(relx=0.35, rely=0.13, relheight=spec_relh, relwidth=spec_relw)

        lbl_worker_login = Label(worker_frame, text='Login')
        self.entry_worker_login = ttk.Entry(worker_frame)

        lbl_worker_login.place(relx=0.35, rely=0.18, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_worker_login.place(relx=0.35, rely=0.22, relheight=spec_relh, relwidth=spec_relw)

        lbl_worker_pass = Label(worker_frame, text='Password')
        self.entry_worker_pass = ttk.Entry(worker_frame)

        lbl_worker_pass.place(relx=0.35, rely=0.27, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_worker_pass.place(relx=0.35, rely=0.31, relheight=spec_relh, relwidth=spec_relw)

        lbl_worker_title = Label(worker_frame, text='Title')
        self.entry_worker_title = ttk.Entry(worker_frame)

        lbl_worker_title.place(relx=0.35, rely=0.36, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_worker_title.place(relx=0.35, rely=0.4, relheight=spec_relh, relwidth=spec_relw)

        self.worker_search_img = PhotoImage(file='icons/search.png')
        worker_search = ttk.Button(worker_frame, image=self.worker_search_img, command=self.open_search_worker)
        worker_search.place(relx=0.91, rely=0.6, width=55, height=55)

        self.worker_refresh_img = PhotoImage(file='icons/refresh.png')
        worker_refresh = ttk.Button(worker_frame, image=self.worker_refresh_img, command=self.view_workers)
        worker_refresh.place(relx=0.91, rely=0.69, width=55, height=55)

        self.worker_edit_img = PhotoImage(file='icons/clock_update.png')
        worker_edit_btn = ttk.Button(worker_frame, image=self.worker_edit_img, command=self.worker_data)
        worker_edit_btn.place(relx=0.91, rely=0.78,  width=55, height=55)

        self.worker_delete_img = PhotoImage(file='icons/delete.png')
        delete_worker_btn = ttk.Button(worker_frame, image=self.worker_delete_img, command=self.delete_workers)
        delete_worker_btn.place(relx=0.91, rely=0.87, width=55, height=55)

        self.save_worker_btn = ttk.Button(worker_frame, text='save')
        self.save_worker_btn.place(relx=0.35, rely=0.48, relwidth=spec_relw)
        self.save_worker_btn.bind('<Button-1>', lambda event: self.worker_record(self.entry_worker_name.get(),
                                                                                 self.entry_worker_surname.get(),
                                                                                 self.entry_worker_login.get(),
                                                                                 self.entry_worker_pass.get(),
                                                                                 self.entry_worker_title.get()))

        self.save_edited_info = ttk.Button(worker_frame, text='edit')
        self.save_edited_info.bind('<Button-1>', lambda event: self.edit_worker(self.entry_worker_name.get(),
                                                                                self.entry_worker_surname.get(),
                                                                                self.entry_worker_login.get(),
                                                                                self.entry_worker_pass.get(),
                                                                                self.entry_worker_title.get()))

        self.workers_tree = ttk.Treeview(worker_frame, height=10, columns=('ID', 'worker_name', 'worker_surname', 'worker_login',
                                 'worker_pass', 'worker_title'),
                                         show='headings')

        self.workers_tree.column('ID', width=30, anchor=CENTER)
        self.workers_tree.column('worker_name', width=150, anchor=CENTER)
        self.workers_tree.column('worker_surname', width=150, anchor=CENTER)
        self.workers_tree.column('worker_login', width=100, anchor=CENTER)
        self.workers_tree.column('worker_pass', width=100, anchor=CENTER)
        self.workers_tree.column('worker_title', width=100, anchor=CENTER)

        self.workers_tree.heading('ID', text='ID')
        self.workers_tree.heading('worker_name', text='Worker name')
        self.workers_tree.heading('worker_surname', text='Worker surname')
        self.workers_tree.heading('worker_login', text='Worker login')
        self.workers_tree.heading('worker_pass', text='Worker pass')
        self.workers_tree.heading('worker_title', text='Worker title')

        self.workers_tree.place(relx=0.042, rely=0.6)

        self.workers_scroll = ttk.Scrollbar(worker_frame, command=self.workers_tree.yview)
        self.workers_scroll.place(relx=0.9, rely=0.77, relheight=0.33, anchor=E)
        self.workers_tree.configure(yscrollcommand=self.workers_scroll.set)

        self.lbl_worker_result = Label(worker_frame, text='', anchor=CENTER)
        self.lbl_worker_result.place(relx=0.25, rely=0.55, relwidth=0.5)

        main_btn = ttk.Button(worker_frame, text='back to main page', command=self.open_admin_frame)
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
        [self.workers_tree.delete(i) for i in self.workers_tree.get_children()]
        [self.workers_tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_workers(self):
        for selection_item in self.workers_tree.selection():
            self.db.cur.execute('''DELETE FROM workers WHERE id=?''', (self.workers_tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_workers()

    def search_workers(self, worker_login):
        worker_login = ('%' + worker_login + '%', )
        self.db.cur.execute('''SELECT * FROM workers WHERE worker_login LIKE ?''', worker_login)
        [self.workers_tree.delete(i) for i in self.workers_tree.get_children()]
        [self.workers_tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def worker_data(self):
        try:
            self.entry_worker_name.delete(0, END)
            self.entry_worker_surname.delete(0, END)
            self.entry_worker_login.delete(0, END)
            self.entry_worker_pass.delete(0, END)
            self.entry_worker_title.delete(0, END)
            self.db.cur.execute('''SELECT * FROM workers WHERE id=?''',
                                (self.workers_tree.set(self.workers_tree.selection()[0], '#1'),))
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

    def edit_worker(self, worker_name, worker_surname, worker_login, worker_pass, worker_title):
        if self.entry_worker_name.index('end') != 0 and self.entry_worker_surname.index('end') != 0 and \
                self.entry_worker_login.index('end') != 0 and self.entry_worker_pass.index('end') != 0\
                and self.entry_worker_title.index('end') != 0:
            self.db.cur.execute('''UPDATE workers SET worker_name=?, worker_surname=?, worker_login=?, worker_pass=?, worker_title=? WHERE ID=?''',
                                (worker_name, worker_surname, worker_login, worker_pass, worker_title,
                                 self.workers_tree.set(self.workers_tree.selection()[0], '#1')))
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
    def open_admin_frame():
        AdminFrame()

    @staticmethod
    def open_search_worker():
        SearchWorker()


class SearchWorker(Toplevel):
    def __init__(self):
        super().__init__()
        self.search_worker_const()
        self.worker = WorkerFrame()

    def search_worker_const(self):
        self.title('Search')
        self.width_window = 300
        self.height_window = 100
        self.width_screen = win.winfo_screenwidth()
        self.height_screen = win.winfo_screenheight()
        self.x_center = int(self.width_screen / 2 - self.width_window / 2)
        self.y_center = int(self.height_screen / 2 - self.height_window / 2)
        self.geometry(f'{self.width_window}x{self.height_window}+{self.x_center}+{self.y_center}')
        self.resizable(False, False)

        lbl_search = Label(self, text='Search')
        lbl_search.place(relx=0.166, rely=0.2)

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
        self.cashier_frame_const()

    def cashier_frame_const(self):
        cashier_frame = ttk.Frame(width=800, height=800, style='Card.TFrame')
        cashier_frame.place(x=0, y=0)

        global auth_worker_name
        lbl_auth_worker = ttk.Label(cashier_frame, text=f'Welcome, {auth_worker_name}', font=('Comic Sans MS', '16'))
        lbl_auth_worker.place(relx=0.5, rely=0.3, anchor=CENTER)

        customer_btn = ttk.Button(cashier_frame, text='Customer register', command=self.open_customer_frame)
        customer_btn.place(relx=0.5, rely=0.4, anchor=CENTER, relwidth=0.16)

        ticket_btn = ttk.Button(cashier_frame, text='Make an order', command=self.open_ticket_frame)
        ticket_btn.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.16)

        bills_btn = ttk.Button(cashier_frame, text='View bills', command=self.open_bills_frame)
        bills_btn.place(relx=0.5, rely=0.6, anchor=CENTER, relwidth=0.16)

        log_out_btn = ttk.Button(cashier_frame, text='log out', command=self.log_out)
        log_out_btn.place(relx=0.01, rely=0.95)

    @staticmethod
    def open_customer_frame():
        CustomerFrame()

    @staticmethod
    def open_ticket_frame():
        TicketFrame()

    @staticmethod
    def open_bills_frame():
        BillsFrame()

    @staticmethod
    def log_out():
        AuthFrame()


class CustomerFrame(Frame):
    def __init__(self):
        super().__init__()
        self.customer_frame_const()
        self.db = db
        self.view_customers()

    def customer_frame_const(self):
        customer_frame = ttk.Frame(width=800, height=800, style='Card.TFrame')
        customer_frame.place(x=0, y=0)

        lbl_login = Label(customer_frame, text='Login')
        self.entry_login = ttk.Entry(customer_frame)

        lbl_login.place(relx=0.35, rely=0.04, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_login.place(relx=0.35, rely=0.08, relheight=spec_relh, relwidth=spec_relw)

        lbl_name = Label(customer_frame, text='Name')
        self.entry_name = ttk.Entry(customer_frame)

        lbl_name.place(relx=0.35, rely=0.13, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_name.place(relx=0.35, rely=0.17, relheight=spec_relh, relwidth=spec_relw)

        lbl_surname = Label(customer_frame, text='Surname')
        self.entry_surname = ttk.Entry(customer_frame)

        lbl_surname.place(relx=0.35, rely=0.22, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_surname.place(relx=0.35, rely=0.26, relheight=spec_relh, relwidth=spec_relw)

        lbl_age = Label(customer_frame, text='Age')
        self.entry_age = ttk.Entry(customer_frame)

        lbl_age.place(relx=0.35, rely=0.31, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_age.place(relx=0.35, rely=0.35, relheight=spec_relh, relwidth=spec_relw)

        lbl_email = Label(customer_frame, text='Email')
        self.entry_email = ttk.Entry(customer_frame)

        lbl_email.place(relx=0.35, rely=0.4, relheight=lbl_relh, relwidth=spec_relw)
        self.entry_email.place(relx=0.35, rely=0.44, relheight=spec_relh, relwidth=spec_relw)

        self.save_cust_btn = ttk.Button(customer_frame, text='save')
        self.save_cust_btn.place(relx=0.35, rely=0.53, relwidth=spec_relw)
        self.save_cust_btn.bind('<Button-1>', lambda event: self.customer_record(self.entry_login.get(),
                                                                                 self.entry_name.get(),
                                                                                 self.entry_surname.get(),
                                                                                 self.entry_age.get(),
                                                                                 self.entry_email.get()))

        self.save_edited_info = ttk.Button(customer_frame, text='edit')
        self.save_edited_info.bind('<Button-1>', lambda event: self.edit_customer(self.entry_login.get(),
                                                                                  self.entry_name.get(),
                                                                                  self.entry_surname.get(),
                                                                                  self.entry_age.get(),
                                                                                  self.entry_email.get()))



        self.customer_search_img = PhotoImage(file='icons/search.png')
        customer_search = ttk.Button(customer_frame, image=self.customer_search_img, command=self.open_search_customer)
        customer_search.place(relx=0.91, rely=0.6, width=55, height=55)

        self.customer_refresh_img = PhotoImage(file='icons/refresh.png')
        customer_refresh = ttk.Button(customer_frame, image=self.customer_refresh_img, command=self.view_customers)
        customer_refresh.place(relx=0.91, rely=0.69, width=55, height=55)

        self.customer_edit_img = PhotoImage(file='icons/clock_update.png')
        customer_edit_btn = ttk.Button(customer_frame, image=self.customer_edit_img, command=self.customer_data)
        customer_edit_btn.place(relx=0.91, rely=0.78, width=55, height=55)



        self.lbl_cust_result = Label(customer_frame, text='')
        self.lbl_cust_result.place(relx=0.25, rely=0.49, relwidth=0.5)

        self.customers_tree = ttk.Treeview(customer_frame, height=10, columns=('ID', 'customer_login', 'customer_name',
                                                               'customer_surname', 'customer_age', 'customer_email'),
                                           show='headings')

        self.customers_tree.column('ID', width=30, anchor=CENTER)
        self.customers_tree.column('customer_login', width=110, anchor=CENTER)
        self.customers_tree.column('customer_name', width=110, anchor=CENTER)
        self.customers_tree.column('customer_surname', width=110, anchor=CENTER)
        self.customers_tree.column('customer_age', width=100, anchor=CENTER)
        self.customers_tree.column('customer_email', width=170, anchor=CENTER)

        self.customers_tree.heading('ID', text='ID')
        self.customers_tree.heading('customer_name', text='Customer name')
        self.customers_tree.heading('customer_surname', text='Customer surname')
        self.customers_tree.heading('customer_login', text='Customer login')
        self.customers_tree.heading('customer_age', text='Customer age')
        self.customers_tree.heading('customer_email', text='Customer email')

        self.customers_tree.place(relx=0.042, rely=0.6)

        customers_scroll = ttk.Scrollbar(customer_frame, command=self.customers_tree.yview)
        customers_scroll.place(relx=0.9, rely=0.77, relheight=0.33, anchor=E)
        self.customers_tree.configure(yscrollcommand=customers_scroll.set)

        main_btn = ttk.Button(customer_frame, text='back to main page', command=self.open_cashier_frame)
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
        [self.customers_tree.delete(i) for i in self.customers_tree.get_children()]
        [self.customers_tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_customers(self):
        for selection_item in self.customers_tree.selection():
            self.db.cur.execute('''DELETE FROM customers WHERE id=?''', (self.customers_tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_customers()

    def search_customers(self, customer_login):
        customer_login = ('%' + customer_login + '%', )
        self.db.cur.execute('''SELECT * FROM customers WHERE customer_login LIKE ?''', customer_login)
        [self.customers_tree.delete(i) for i in self.customers_tree.get_children()]
        [self.customers_tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def customer_data(self):
        try:
            self.entry_login.delete(0, END)
            self.entry_name.delete(0, END)
            self.entry_surname.delete(0, END)
            self.entry_age.delete(0, END)
            self.entry_email.delete(0, END)
            self.db.cur.execute('''SELECT * FROM customers WHERE id=?''',
                                (self.customers_tree.set(self.customers_tree.selection()[0], '#1'),))
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

    def edit_customer(self, customer_login, customer_name, customer_surname, customer_age, customer_email):
        if self.entry_login.index('end') != 0 and self.entry_name.index('end') != 0 and \
                self.entry_surname.index('end') != 0 and self.entry_age.index('end') != 0\
                and self.entry_email.index('end') != 0:
            self.db.cur.execute('''UPDATE customers SET customer_login=?, customer_name=?, customer_surname=?, customer_age=?, customer_email=? WHERE ID=?''',
                                (customer_login, customer_name, customer_surname, customer_age, customer_email,
                                 self.customers_tree.set(self.customers_tree.selection()[0], '#1')))
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
    def open_cashier_frame():
        CashierFrame()


class SearchCustomer(Toplevel):
    def __init__(self):
        super().__init__()
        self.search_customer_const()
        self.customer = CustomerFrame()

    def search_customer_const(self):
        self.title('Search')
        self.width_window = 300
        self.height_window = 100
        self.width_screen = win.winfo_screenwidth()
        self.height_screen = win.winfo_screenheight()
        self.x_center = int(self.width_screen / 2 - self.width_window / 2)
        self.y_center = int(self.height_screen / 2 - self.height_window / 2)
        self.geometry(f'{self.width_window}x{self.height_window}+{self.x_center}+{self.y_center}')
        self.resizable(False, False)

        lbl_search = Label(self, text='Search')
        lbl_search.place(relx=0.166, rely=0.2)

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
        self.ticket_frame_const()
        self.db = db
        self.view_customers()
        self.view_cinemas()

    def ticket_frame_const(self):
        ticket_frame = ttk.Frame(width=800, height=800, style='Card.TFrame')
        ticket_frame.place(x=0, y=0)

        self.customers_tree = ttk.Treeview(ticket_frame, height=720, columns='customer_login', show='headings')

        self.customers_tree.column('customer_login', width=150, anchor=CENTER)

        self.customers_tree.heading('customer_login', text='Customer login')

        self.customers_tree.place(relx=0, rely=0, relheight=0.998)

        self.cinemas_tree = ttk.Treeview(ticket_frame, height=720, columns=('id', 'film_name', 'scheduled_time', 'cinema_hall'),
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

        self.lbl_customer_login = Label(ticket_frame, text='Customer login')
        self.entry_customer_login = ttk.Entry(ticket_frame)

        self.lbl_customer_login.place(relx=0.26, rely=0.06, relwidth=0.225)
        self.entry_customer_login.place(relx=0.26, rely=0.09, relheight=spec_relh, relwidth=0.23)

        lbl_film_name = Label(ticket_frame, text='Film name')
        self.entry_film_name = ttk.Entry(ticket_frame)

        lbl_film_name.place(relx=0.26, rely=0.14, relwidth=0.225)
        self.entry_film_name.place(relx=0.26, rely=0.17, relheight=spec_relh, relwidth=0.23)

        lbl_sch_time = Label(ticket_frame, text='Scheduled time')
        self.entry_sch_time = ttk.Entry(ticket_frame)

        lbl_sch_time.place(relx=0.26, rely=0.22, relwidth=0.225)
        self.entry_sch_time.place(relx=0.26, rely=0.25, relheight=spec_relh, relwidth=0.23)

        lbl_cinema_hall = Label(ticket_frame, text='Cinema hall')
        self.entry_cinema_hall = ttk.Entry(ticket_frame)

        lbl_cinema_hall.place(relx=0.26, rely=0.3, relwidth=0.225)
        self.entry_cinema_hall.place(relx=0.26, rely=0.33, relheight=spec_relh, relwidth=0.23)

        lbl_place_level = Label(ticket_frame, text='Place level')
        self.combo_place_level = ttk.Combobox(ticket_frame, state='readonly', values=('economy', 'comfort', 'vip'))
        self.combo_place_level.bind('<<ComboboxSelected>>', lambda _: self.get_price_by_combobox())

        lbl_place_level.place(relx=0.26, rely=0.38, relwidth=0.225)
        self.combo_place_level.place(relx=0.26, rely=0.41, relheight=0.05, relwidth=0.23)

        lbl_price = Label(ticket_frame, text='Price')
        self.price_stringvar = StringVar()
        self.entry_price = ttk.Entry(ticket_frame, textvariable=self.price_stringvar, state=DISABLED)

        lbl_price.place(relx=0.26, rely=0.46, relwidth=0.225)
        self.entry_price.place(relx=0.26, rely=0.49, relheight=spec_relh, relwidth=0.23)

        lbl_quantity = Label(ticket_frame, text='Quantity')
        self.entry_quantity = ttk.Entry(ticket_frame)

        lbl_quantity.place(relx=0.26, rely=0.54, relwidth=0.225)
        self.entry_quantity.place(relx=0.26, rely=0.57, relheight=spec_relh, relwidth=0.23)

        lbl_total = Label(ticket_frame, text='Total')
        self.total_stringvar = StringVar()
        self.entry_total = ttk.Entry(ticket_frame, state=DISABLED, textvariable=self.total_stringvar)

        lbl_total.place(relx=0.26, rely=0.62, relwidth=0.225)
        self.entry_total.place(relx=0.26, rely=0.65, relheight=spec_relh, relwidth=0.23)

        self.select_for_cust_btn = ttk.Button(ticket_frame, text='select', command=lambda: self.select_from_trees_for_cust())
        self.select_for_cust_btn.place(relx=0.275, rely=0.75, relwidth=0.2)

        self.select_for_guest_btn = ttk.Button(ticket_frame, text='select', command=lambda: self.select_from_trees_for_guest())

        self.buy_as_cust_btn = ttk.Button(ticket_frame, text='buy', state=DISABLED, command=lambda: self.buy_a_ticket_as_cust())
        self.buy_as_cust_btn.place(relx=0.275, rely=0.8, relwidth=0.2)

        self.buy_as_guest_btn = ttk.Button(ticket_frame, text='buy', state=DISABLED, command=lambda: self.buy_a_ticket_as_guest())

        self.lbl_ticket_result = ttk.Label(ticket_frame, text='')
        self.lbl_ticket_result.place(relx=0.275, rely=0.85, relwidth=0.225)

        self.as_guest_btn = ttk.Button(ticket_frame, text='switch to guest', command=lambda: self.switch_to_guest())
        self.as_guest_btn.place(relx=0.275, rely=0.909, relwidth=0.2)

        self.as_cust_btn = ttk.Button(ticket_frame, text='switch to customer', command=lambda: self.switch_to_customer())

        self.reset_entries_btn = ttk.Button(ticket_frame, text='reset', command=lambda: self.reset_entries())
        self.reset_entries_btn.place(relx=0.275, rely=0.01, relwidth=0.2)

        main_btn = ttk.Button(ticket_frame, text='back to main page', command=self.open_cashier_frame)
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
    def open_cashier_frame():
        CashierFrame()


class BillsFrame(Frame):
    def __init__(self):
        super().__init__()
        self.bills_frame_const()
        self.db = db
        self.view_bills()

    def bills_frame_const(self):
        bills_frame = ttk.Frame(width=800, height=800, style='Card.TFrame')
        bills_frame.place(x=0, y=0)

        self.bills_search_img = PhotoImage(file='icons/search.png')
        bills_search = ttk.Button(bills_frame, image=self.bills_search_img, command=self.open_search_bills)
        bills_search.place(relx=0.35, rely=0.76, width=55, height=55)

        self.bill_refresh = PhotoImage(file='icons/refresh.png')
        bill_refresh = ttk.Button(bills_frame, image=self.bill_refresh, command=self.view_bills)
        bill_refresh.place(relx=0.45, rely=0.76, width=55, height=55)

        self.bills_delete_img = PhotoImage(file='icons/delete.png')
        delete_bills_btn = ttk.Button(bills_frame, image=self.bills_delete_img, command=self.delete_bills)
        delete_bills_btn.place(relx=0.55, rely=0.76, width=55, height=55)

        self.bills_tree = ttk.Treeview(bills_frame, height=720, columns=('id', 'customer_login', 'film_name',
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

        main_btn = ttk.Button(bills_frame, text='back to main page', command=self.open_cashier_frame)
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

    def delete_bills(self):
        for selection_item in self.bills_tree.selection():
            self.db.cur.execute('''SELECT film_name, scheduled_time, place_level, quantity FROM bills WHERE id=?''', (self.bills_tree.set(selection_item, '#1'),))
            row = self.db.cur.fetchall()[0]
            film_name = row[0]
            scheduled_time = row[1]
            place_level = row[2]
            quantity = int(row[3])
            self.db.cur.execute(f"SELECT  {place_level} FROM cinemas WHERE film_name=? AND scheduled_time=?",
                                (film_name, scheduled_time))
            smth = self.db.cur.fetchone()[0]
            quantity += int(smth)
            self.db.cur.execute(f"UPDATE cinemas SET '{place_level}'=? WHERE film_name=? AND scheduled_time=?", (quantity, film_name, scheduled_time))
            self.db.cur.execute('''DELETE FROM bills WHERE id=?''', (self.bills_tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_bills()

    @staticmethod
    def open_cashier_frame():
        CashierFrame()

    @staticmethod
    def open_search_bills():
        SearchBill()


class SearchBill(Toplevel):
    def __init__(self):
        super().__init__()
        self.search_bills_const()
        self.bill = BillsFrame()

    def search_bills_const(self):
        self.title('Search')
        self.width_window = 300
        self.height_window = 100
        self.width_screen = win.winfo_screenwidth()
        self.height_screen = win.winfo_screenheight()
        self.x_center = int(self.width_screen / 2 - self.width_window / 2)
        self.y_center = int(self.height_screen / 2 - self.height_window / 2)
        self.geometry(f'{self.width_window}x{self.height_window}+{self.x_center}+{self.y_center}')
        self.resizable(False, False)

        lbl_search = Label(self, text='Search')
        lbl_search.place(relx=0.166, rely=0.2)

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
    app = AuthFrame()
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
