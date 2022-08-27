from classes import *

customers_obj_list = []
halls_obj_list = [Hall('Classic Hall', 10, 7, 5), Hall('Special Hall', 20, 15, 10)]
workers_obj_list = [Worker('Orxan', 'Mamedov', '1', '1', 'cashier'),
                    Worker('Samir', 'Aliyev', '2', '2', 'admin')]
cinemas_obj_list = []


# WORKER FUNCS - START
def add_worker(worker):
    temp_worker = worker
    cur.execute(f"INSERT INTO workers (worker_name, surname, login, password, title) VALUES (?, ?, ?, ?, ?)",
                (temp_worker.get_name(), temp_worker.get_surname(), temp_worker.get_login(), temp_worker.get_pass(), temp_worker.get_title()))
    db.commit()
    return temp_worker


def find_worker_index(worker_name):
    for elem in range(len(workers_obj_list)):
        if workers_obj_list[elem].get_login() == worker_name:
            return elem
    return -1


def delete_worker(index):
    workers_obj_list.pop(index)
# WORKER FUNCS - END


# CUSTOMER FUNCS - START
def add_customer(customer):
    temp_person = customer
    cur.execute(f"INSERT INTO customers (login, customer_name, surname, age, email) VALUES (?, ?, ?, ?, ?)",
                (temp_person.get_login(), temp_person.get_name(), temp_person.get_surname(), temp_person.get_age(),
                 temp_person.get_email()))
    db.commit()
    return temp_person


def find_customer_index(login):
    for elem in range(len(customers_obj_list)):
        if customers_obj_list[elem].get_login() == login:
            return elem
    return -1


def delete_customer(index):
    customers_obj_list.pop(index)
# CUSTOMER FUNCS - END


# HALL FUNCS - START
def add_hall(hall):
    temp_hall = hall
    cur.execute(f"INSERT INTO halls (hall_name, economy, comfort, vip) VALUES (?, ?, ?, ?)",
                (temp_hall.get_name(), temp_hall.get_eco(), temp_hall.get_comf(), temp_hall.get_vip()))
    db.commit()
    return temp_hall


def find_hall_index(hall_name):
    for i, v in enumerate(halls_obj_list):
        if v.get_name() == hall_name:
            return i
    return -1
# HALL FUNCS - END


# CINEMA FUNCS - START
# i - index of hall, v - hall. e - index of cinema, l - cinema
def find_cinema_and_hall_index(film_name):
    for i, v in enumerate(halls_obj_list):
        for e, l in enumerate(v.cinema_obj_list):
            if l.get_name() == film_name:
                return e, i
    return -1


def add_cinema(cinema):
    if find_hall_index(cinema.get_name()) != -1:
        temp_cinema = cinema
        cur.execute(f"INSERT INTO cinemas (film_name, sch_time, hall) VALUES (?, ?, ?)",
                    (temp_cinema.get_name(), temp_cinema.get_time(), temp_cinema.get_hall()))
        db.commit()
        halls_obj_list[find_hall_index(hall_name)].cinema_obj_list.append(temp_cinema)
        cinemas_obj_list.append(temp_cinema)
        return temp_cinema
    return -1


def edit_scheduled_time(film_name, new_time):
    cinema_index, hall_index = find_cinema_and_hall_index(film_name)[0], find_cinema_and_hall_index(film_name)[1]
    if find_cinema_and_hall_index(film_name)[0] != -1:
        halls_obj_list[hall_index].cinema_obj_list[cinema_index].change_time(new_time)
        return 0
    else:
        return -1
# CINEMA FUNCS - END
