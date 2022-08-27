import sqlite3
from tkinter import *
from tkinter import ttk

spec_relh = 0.05
spec_relw = 0.3
lbl_relh = 0.04


class Main(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=TOP, fill=X)

        self.add_img = PhotoImage(file='add_customer.png')
        btn_open_dialog = Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                 compound=TOP, image=self.add_img)
        btn_open_dialog.pack(side=LEFT)

        self.upd_img = PhotoImage(file='update.png')
        btn_edit_dialog = Button(toolbar, text='Редактировать', bg='#d7d8e0',
                                 bd=0, image=self.upd_img, compound=TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=LEFT)

        self.delete_img = PhotoImage(file='delete.png')
        btn_delete_dialog = Button(toolbar, text='Удалить', bg='#d7d8e0',
                                 bd=0, image=self.delete_img, compound=TOP, command=self.delete_records)
        btn_delete_dialog.pack(side=LEFT)

        self.search_img = PhotoImage(file='search.png')
        btn_search_dialog = Button(toolbar, text='Найти позиции', bg='#d7d8e0',
                                   bd=0, image=self.search_img, compound=TOP, command=self.open_search_dialog)
        btn_search_dialog.pack(side=LEFT)

        self.refresh_img = PhotoImage(file='refresh.png')
        btn_refresh_dialog = Button(toolbar, text='Обновить', bg='#d7d8e0',
                                   bd=0, image=self.refresh_img, compound=TOP, command=self.view_records)
        btn_refresh_dialog.pack(side=LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'description', 'costs', 'total'), height=15, show='headings')

        self.tree.column('ID', width=30, anchor=CENTER)
        self.tree.column('description', width=365, anchor=CENTER)
        self.tree.column('costs', width=150, anchor=CENTER)
        self.tree.column('total', width=100, anchor=CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('description', text='Наименование')
        self.tree.heading('costs', text='Доход/расход')
        self.tree.heading('total', text='Итого')

        self.tree.pack(side=LEFT)

        scroll = ttk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=RIGHT, fill=Y)
        self.tree.configure(yscrollcommand=scroll.set)

    def records(self, description, costs, total):
        self.db.insert_data(description, costs, total)
        self.view_records()

    def view_records(self):
        self.db.cur.execute('''SELECT * FROM finance''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def update_record(self, description, costs, total):
        self.db.cur.execute('''UPDATE finance SET description=?, costs=?, total=? WHERE ID=?''',
                            (description, costs, total, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute('''DELETE FROM finance WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, description):
        description = ('%' + description + '%', )
        self.db.cur.execute('''SELECT * FROM finance WHERE description LIKE ?''', description)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    @staticmethod
    def open_dialog():
        Child()

    @staticmethod
    def open_update_dialog():
        Update()

    @staticmethod
    def open_search_dialog():
        Search()


class Child(Toplevel):
    def __init__(self):
        super().__init__(win)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Customer register')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = ttk.Label(self, text='Наименование')
        label_description.place(x=50, y=50)

        label_select = ttk.Label(self, text='Выберите')
        label_select.place(x=50, y=80)

        label_sum = ttk.Label(self, text='Сумма')
        label_sum.place(x=50, y=110)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=110)

        self.combobox = ttk.Combobox(self, values=['Доход', 'Расход'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='OK')
        self.btn_ok.place(x=200, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                  self.combobox.get(),
                                                                  self.entry_money.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
        self.db = db
        self.default_data()

    def init_edit(self):
        self.title('Редактировать позицию')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_money.get()))
        self.btn_ok.destroy()

    def default_data(self):
        self.db.cur.execute('''SELECT * FROM finance WHERE id=?''',
                          (self.view.tree.set(self.view.tree.selection()[0], '#1'),))
        row = self.db.cur.fetchone()
        self.entry_description.insert(0, row[1])
        if row[2] != 'Доход':
            self.combobox.current(1)
        self.entry_money.insert(0, row[3])


class Search(Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('Поиск')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        self.con = sqlite3.connect('finance.db')
        self.cur = self.con.cursor()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS finance(id integer primary key, description text, costs text, total real)''')
        self.con.commit()

    def insert_data(self, description, costs, total):
        self.cur.execute('''INSERT INTO finance (description, costs, total) VALUES (?, ?, ?)''',
                         (description, costs, total))
        self.con.commit()


if __name__ == '__main__':
    win = Tk()
    db = DB()
    app = Main(win)
    app.pack()
    win.title('Cinema Project')
    win.geometry('665x400')
    win.resizable(False, False)
    win.mainloop()
