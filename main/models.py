from django.db.models import *

class Book(Model):
    title = CharField(max_length = 1000)
    author = CharField(max_length = 1000)
    isAvailable = BooleanField()
    rack_number = IntegerField()
    subject = CharField(max_length = 1000, default="")
    publication_date = IntegerField(default = 0)
    isBorrowed = BooleanField()
    borrowed_person_id = IntegerField()
    return_date = CharField(max_length = 1000)
    isReserved = BooleanField()
    reserved_person_id = IntegerField()

class Person(Model):
    name = CharField(max_length = 1000)
    age = IntegerField()
    login = CharField(max_length = 1000)
    password = CharField(max_length = 1000)
    role = CharField(max_length = 1000)