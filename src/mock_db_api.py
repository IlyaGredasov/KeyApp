from dataclasses import dataclass
from random import randint, random
from typing import List

from faker import Faker


@dataclass
class PasswordQuery:
    domain: str
    username: str
    password: str
    isAdminProtected: bool = 0


faker = Faker()
n = 15
admin_password = "123"

db = [PasswordQuery(faker.domain_name(), faker.user_name(), faker.password(), bool(randint(0, 1)))
      for i in range(n)]


def refreshMasterKey():
    return True


def getAll() -> List[PasswordQuery]:
    return db


def getByDomain(domain: str) -> PasswordQuery:
    return [query for query in db if query.domain == domain][0]


def addQuery(domain: str, username: str, password: str, is_admin_protected: bool) -> bool:
    db.append(PasswordQuery(domain, username, password, is_admin_protected))
    return True


def deleteQuery(domain: str) -> bool:
    for query in db:
        if query.domain == domain:
            db.remove(query)
            return True
    return False


def changeQuery(domain: str, username: str, password: str, is_admin_protected: bool) -> bool:
    for i in range(len(db)):
        if db[i].domain == domain:
            db[i] = PasswordQuery(domain, username, password, is_admin_protected)
            return True
    return False


def fuzzySearch(domain: str):
    return [query for query in db if random() < 0.6]


def checkAdminPassword(password: str) -> bool:
    return password == admin_password


def checkFlashDriver() -> bool:
    return True
