from dataclasses import dataclass
from random import randint, random
from typing import List, Callable
from faker import Faker


@dataclass
class PasswordQuery:
    domain: str
    username: str
    password: str
    is_admin_protected: bool


faker = Faker()
n = 15
admin_password = "123"

db = [PasswordQuery(faker.domain_name(), faker.user_name(), faker.password(), bool(randint(0, 1)))
      for i in range(n)]


def print_decorator(func: Callable):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} has been called")
        return func(*args, **kwargs)

    return wrapper


@print_decorator
def refresh_master_key():
    return True


@print_decorator
def get_all() -> List[PasswordQuery]:
    return db


@print_decorator
def get_correct(domain: str) -> PasswordQuery:
    return [query for query in db if query.domain == domain][0]


@print_decorator
def add_data(domain: str, username: str, password: str, is_admin_protected: bool) -> bool:
    db.append(PasswordQuery(domain, username, password, is_admin_protected))
    return True


@print_decorator
def delete_data(domain: str) -> bool:
    for query in db:
        if query.domain == domain:
            db.remove(query)
            return True
    return False


@print_decorator
def key_change(domain: str, username: str, password: str, is_admin_protected: bool) -> bool:
    for i in range(len(db)):
        if db[i].domain == domain:
            db[i] = PasswordQuery(domain, username, password, is_admin_protected)
            return True
    return False


@print_decorator
def fuzzy_search(domain: str):
    return [query for query in db if random() < 0.6]
