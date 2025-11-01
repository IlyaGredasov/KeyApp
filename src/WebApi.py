import inspect
import requests
import time
from dataclasses import dataclass
from functools import wraps
from typing import List


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
            try:
                print(func.__name__, funcArgs)
                start = time.perf_counter()
                r = eval(f"requests.{method}")(url=f'http://10.55.0.1:8000/{url}',
                                               json=funcArgs,
                                               timeout=(10 if func.__name__ == "fuzzySearch" else 1, 10))
                end = time.perf_counter()
                print(f"Request {method} took {end - start:.6f} seconds")
                return func(*args, **kwargs, json=r.json())
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return False

        return wrapper

    return decorator


@preventiveRequest(url="check_token", method="get")
def checkToken(json=None) -> bool:
    return json['status'] == "Token is found"


def preventiveCheckToken(onFailure=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if checkToken():
                return func(*args, **kwargs)
            elif onFailure:
                onFailure()

        return wrapper

    return decorator


@preventiveRequest(url="change_key", method="put")
def refreshMasterKey(json=None) -> bool:
    return json['status'] == "data_key_changed"


@preventiveRequest(url="get_all", method="get")
def getAll(json=None) -> int:
    return int(json['password_count'])


@preventiveRequest(url="get_correct", method="post")
def getById(id: int, json=None) -> PasswordQuery:
    return PasswordQuery(domain=json["domain"], username=json['login'], password=json['password'])


@preventiveRequest(url="add_data", method="post")
def addQuery(domain: str, login: str, password: str, json=None) -> bool:
    return json['status'] == "data_added"


@preventiveRequest(url="delete_data", method="post")
def deleteQuery(domain: str, login: str = "", password: str = "", json=None) -> bool:
    return json['status'] == "data_deleted"


@preventiveRequest(url="change_data", method="post")
def changeQuery(domain: str, login: str, password: str, json=None) -> str:
    return json['status']


@preventiveRequest(url="get_fuzzy", method="post")
def fuzzySearch(domain: str, login: str = "", password: str = "", json=None) -> List[PasswordQuery]:
    return [PasswordQuery(username=query['login'], password=query['password'], domain=query['domain']) for query in
            json['data_list']]


def checkAdminPassword(password: str, json=None) -> bool:
    return True
