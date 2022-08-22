from uuid import uuid4


class Worker:
    def __init__(self, worker_name, worker_surname, worker_login, worker_pass, title):
        self.__id = uuid4()
        self.__worker_name = worker_name
        self.__worker_surname = worker_surname
        self.__worker_login = worker_login
        self.__worker_pass = worker_pass
        self.__title = title

    def __repr__(self):
        res_str = f' ID: {self.__id}\n Worker name: {self.__worker_name}\n Worker surname: {self.__worker_surname}\n ' \
                  f'Worker login: {self.__worker_login}\n Worker title: {self.__title}\n '
        return res_str

    def get_login(self):
        return self.__worker_login

    def get_pass(self):
        return self.__worker_pass

    def get_title(self):
        return self.__title


class Cinema:
    def __init__(self, film_name, scheduled_time):
        self.__id = uuid4()
        self.__film_name = film_name
        self.__scheduled_time = scheduled_time
        self.__cinema_hall = 0

    def __repr__(self):
        res_str = f' ID: {self.__id}\n Film name: {self.__film_name}\n Scheduled time: {self.__scheduled_time}\n ' \
                  f'Cinema hall: {self.__cinema_hall}\n '
        return res_str

    def get_name(self):
        return self.__film_name

    def change_time(self, new_time):
        self.__scheduled_time = new_time


class Hall:
    def __init__(self, hall_name, eco_places, comf_places, vip_places):
        self.__id = uuid4()
        self.__hall_name = hall_name
        self.__eco_places = eco_places
        self.__comf_places = comf_places
        self.__vip_places = vip_places
        self.cinema_obj_list = [Cinema('Classic film', 'Classic time')]

    def __str__(self):
        res_str = f' ID: {self.__id}\n Hall name: {self.__hall_name}\n Economy places: {self.__eco_places}\n ' \
                  f'Comfort places: {self.__comf_places}\n ' \
                  f'VIP places: {self.__vip_places}\n Poster of this hall:\n {self.cinema_obj_list}'
        return res_str

    def get_name(self):
        return self.__hall_name

    def add_cinema(self, cinema):
        self.cinema_obj_list.append(cinema)


class Customer:
    def __init__(self, login, password, name, surname, age, email):
        self.__id = uuid4()
        self.__login = login
        self.__password = password
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__email = email
        self.__orders_obj_list = []

    def __str__(self):
        res_str = f' ID: {self.__id}\n Login: {self.__login}\n Name: {self.__name}\n ' \
                  f'Surname: {self.__surname}\n Age: {self.__age}\n E-mail: {self.__email}\n ' \
                  f'Orders: {self.__orders_obj_list}'
        return res_str

    def get_login(self):
        return self.__login
