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

    def find_index(self, film_name):
        for elem in range(len(self.cinema_obj_list)):
            if self.cinema_obj_list[elem].get_name() == film_name:
                return elem


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
halls_obj_list = [Hall('Classic Hall', 10, 7, 5)]


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
# ----------


# Cinema funcs
# def find_cinema_index(film_name):
#     for i in halls_obj_list:


def add_cinema(film_name, scheduled_time, hall_name):
    for elem in halls_obj_list:
        if elem.get_name() == hall_name:
            elem.add_cinema(Cinema(film_name, scheduled_time))


# def edit_scheduled_time(film_name, new_time):
#     halls_obj_list[]

# ---------
print(customers_obj_list[0])
print(halls_obj_list[0])