from dataclasses import dataclass
from functools import wraps
from random import random
from typing import List

import requests
import inspect
from functools import wraps


@dataclass
class PasswordQuery:
    domain: str
    username: str
    password: str
    isAdminProtected: bool = 0


def preventiveRequest(url, method="get"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            funcArgs = dict(bound.arguments)

            r = eval(f"requests.{method}")(url=f'http://10.55.0.1:8000/{url}',
                                           json=funcArgs)
            return func(*args, **kwargs, json=r.json())

        return wrapper

    return decorator


@preventiveRequest(url="change_key", method="put")
def refreshMasterKey(json=None) -> bool:
    return json['status'] == "data_key_changed"


@preventiveRequest(url="get_all", method="get")
def getAll(json=None) -> List[PasswordQuery]:
    return [PasswordQuery(username=query['login'], password=query['password'], domain=query['domain']) for query in
            json['data_list']]


@preventiveRequest(url="get_correct", method="get")
def getByDomain(domain: str, json=None) -> PasswordQuery:
    return PasswordQuery(domain=domain, username=json['login'], password=json['password'])


@preventiveRequest(url="add_data", method="post")
def addQuery(domain: str, login: str, password: str, isAdminProtected: bool = 0, json=None) -> bool:
    return json['status'] == "data_added"


@preventiveRequest(url="delete_data", method="delete")
def deleteQuery(domain: str, json=None) -> bool:
    return json['status'] == "data_deleted"


@preventiveRequest(url="change_data", method="post")
def changeQuery(domain: str, username: str, password: str, isAdminProtected: bool = 0, json=None) -> bool:
    return json['status'] == "data_changed"


def fuzzySearch(domain: str, json=None) -> List[PasswordQuery]:
    return [query for query in getAll() if random() < 0.6]


def checkAdminPassword(password: str, json=None) -> bool:
    return True


@preventiveRequest(url="check_token", method="get")
def checkFlashDriver(json=None) -> bool:
    return json['status'] == "Token is found"
