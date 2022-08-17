# import os
import uuid


class Cinema:
    def __init__(self, film_name, scheduled_time):
        self.__id = uuid.uuid4()
        self.__film_name = film_name
        self.__scheduled_time = scheduled_time
        self.__cinema_hall = 0

    def __repr__(self):
        res_str = f'ID: {self.__id}\nFilm name: {self.__film_name}\nScheduled time: {self.__scheduled_time}\n' \
                  f'Cinema hall: {self.__cinema_hall}'
        return res_str

    def get_name(self):
        return self.__film_name

    def change_time(self, new_time):
        self.__scheduled_time = new_time


class Hall:
    def __init__(self, hall_name, eco_places, comf_places, vip_places):
        self.__id = uuid.uuid4()
        self.__hall_name = hall_name
        self.__eco_places = eco_places
        self.__comf_places = comf_places
        self.__vip_places = vip_places
        self.cinema_obj_list = [Cinema('Classic film', 'Classic time')]

    def __str__(self):
        res_str = f'ID: {self.__id}\nHall name: {self.__hall_name}\nEconomy places: {self.__eco_places}\n' \
                  f'Comfort places: {self.__comf_places}\n' \
                  f'VIP places: {self.__vip_places}\nPoster of this hall:\n{self.cinema_obj_list}'
        return res_str

    def get_name(self):
        return self.__hall_name

    def add_cinema(self, cinema):
        self.cinema_obj_list.append(cinema)


class Customer:
    def __init__(self, login, password, name, surname, age, email):
        self.__id = uuid.uuid4()
        self.__login = login
        self.__password = password
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__email = email
        self.__orders_obj_list = []

    def __str__(self):
        res_str = f'ID: {self.__id}\nLogin: {self.__login}\nName: {self.__name}\n' \
                  f'Surname: {self.__surname}\nAge: {self.__age}\nE-mail: {self.__email}\n' \
                  f'Orders: {self.__orders_obj_list}'
        return res_str

    def get_login(self):
        return self.__login


customers_obj_list = [Customer('classic_user2000', 'ClassicUser2000', 'Classic', 'User',
                               '20', 'classicuser2000@gmail.com')]
halls_obj_list = [Hall('Classic Hall', 10, 7, 5), Hall('Special Hall', 20, 15, 10)]


# Customer funcs
def add_customer(login, password, name, surname, age, email):
    customers_obj_list.append(Customer(login, password, name, surname, age, email))


def find_customer_index(login):
    for elem in range(len(customers_obj_list)):
        if customers_obj_list[elem].get_login() == login:
            return elem
    return -1


def delete_customer(index):
    customers_obj_list.pop(index)
# ---------


# Hall funcs
def add_hall(hall_name, eco_places, comf_places, vip_places):
    halls_obj_list.append(Hall(hall_name, eco_places, comf_places, vip_places))


def find_hall_index(hall_name):
    for i, v in enumerate(halls_obj_list):
        if v.get_name() == hall_name:
            return i
    return -1
# ----------


# Cinema funcs
# i - index of hall, v - hall. e - index of cinema, l - cinema
def find_cinema_and_hall_index(film_name):
    for i, v in enumerate(halls_obj_list):
        for e, l in enumerate(v.cinema_obj_list):
            if l.get_name() == film_name:
                return e, i
    return -1


def add_cinema(film_name, scheduled_time, hall_name):
    if find_hall_index(hall_name) != -1:
        halls_obj_list[find_hall_index(hall_name)].add_cinema(Cinema(film_name, scheduled_time))
        return 0
    return -1


def edit_scheduled_time(film_name, new_time):
    cinema_index, hall_index = find_cinema_and_hall_index(film_name)[0], find_cinema_and_hall_index(film_name)[1]
    if find_cinema_and_hall_index(film_name)[0] != -1:
        halls_obj_list[hall_index].cinema_obj_list[cinema_index].change_time(new_time)
        return 'Success'
    else:
        return 'Error'

# ---------
