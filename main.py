# import os
from classes import *

customers_obj_list = [Customer('classic_user2000', 'ClassicUser2000', 'Classic', 'User',
                               '20', 'classicuser2000@gmail.com')]
halls_obj_list = [Hall('Classic Hall', 10, 7, 5), Hall('Special Hall', 20, 15, 10)]


# Customer funcs
def add_customer(login, password, name, surname, age, email):
    temp_person = Customer(login, password, name, surname, age, email)
    customers_obj_list.append(temp_person)
    return temp_person


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
    temp_hall = Hall(hall_name, eco_places, comf_places, vip_places)
    halls_obj_list.append(temp_hall)
    return temp_hall


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
        temp_cinema = Cinema(film_name, scheduled_time)
        halls_obj_list[find_hall_index(hall_name)].add_cinema(temp_cinema)
        return temp_cinema
    return -1


def edit_scheduled_time(film_name, new_time):
    cinema_index, hall_index = find_cinema_and_hall_index(film_name)[0], find_cinema_and_hall_index(film_name)[1]
    if find_cinema_and_hall_index(film_name)[0] != -1:
        halls_obj_list[hall_index].cinema_obj_list[cinema_index].change_time(new_time)
        return 0
    else:
        return -1
# ---------


