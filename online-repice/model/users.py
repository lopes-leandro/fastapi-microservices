from datetime import date
from uuid import UUID

from fastapi import Depends

class Login:
    def __init__(self, id: UUID, username: str, password: str, type: any):
        self.id = id
        self.username = username
        self.password = password
        self.type = type

class UserDetails:
    def __init__(self, id: UUID, firstname: str, lastname: str, middle: str, bday: date, pos: str):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.middle = middle
        self.bday = bday
        self.pos = pos

class Profile:
    def __init__(self, id: UUID, date_created: date, login=Depends(Login), user=Depends(UserDetails)):
        self.id = id
        self.date_created = date_created
        self.login = login
        self.user = user