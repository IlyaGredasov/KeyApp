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


def preventiveRequest(url, method):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            funcArgs = dict(bound.arguments)
            del funcArgs['json']
            if 'isAdminProtected' in funcArgs.keys():
                del funcArgs['isAdminProtected']
            print(funcArgs)
            print(wrapper.__name__)
            try:
                r = eval(f"requests.{method}")(url=f'http://10.55.0.1:8000/{url}',
                                               json=funcArgs)
                print(r.json())
                return func(*args, **kwargs, json=r.json())
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return False

        return wrapper

    return decorator


@preventiveRequest(url="check_token", method="get")
def checkToken(json=None) -> bool:
    return json['status'] == "Token is found"


def preventiveCheckToken(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if checkToken():
            return func(*args, **kwargs)

    return wrapper


@preventiveCheckToken
@preventiveRequest(url="change_key", method="put")
def refreshMasterKey(json=None) -> bool:
    return json['status'] == "data_key_changed"


@preventiveCheckToken
@preventiveRequest(url="get_all", method="get")
def getAll(json=None) -> List[PasswordQuery]:
    return [PasswordQuery(username=query['login'], password=query['password'], domain=query['domain']) for query in
            json['data_list']]


@preventiveCheckToken
@preventiveRequest(url="get_correct", method="post")
def getByDomain(domain: str, login: str = "", password: str = "", json=None) -> PasswordQuery:
    return PasswordQuery(domain=domain, username=json['login'], password=json['password'])


@preventiveCheckToken
@preventiveRequest(url="add_data", method="post")
def addQuery(domain: str, login: str, password: str, isAdminProtected: bool = 0, json=None) -> bool:
    return json['status'] == "data_added"


@preventiveCheckToken
@preventiveRequest(url="delete_data", method="post")
def deleteQuery(domain: str, login: str = "", password: str = "", json=None) -> bool:
    return json['status'] == "data_deleted"


@preventiveCheckToken
@preventiveRequest(url="change_data", method="post")
def changeQuery(domain: str, login: str, password: str, isAdminProtected: bool = 0, json=None) -> bool:
    return json['status'] == "data_changed"


@preventiveCheckToken
@preventiveRequest(url="get_fuzzy", method="post")
def fuzzySearch(domain: str, login: str = "", password: str = "", json=None) -> List[PasswordQuery]:
    return [PasswordQuery(username=query['login'], password=query['password'], domain=query['domain']) for query in
            json['data_list']]


def checkAdminPassword(password: str, json=None) -> bool:
    return True
