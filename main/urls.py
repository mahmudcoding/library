from django.urls import path
from .views import *

urlpatterns = [
    path('books/', getBooks, name='get_books'),
    path('persons/', getPersons, name='get_persons'),

    path('books/update/', updateBook, name='update_book'),
    path('persons/update/', updatePerson, name='update_person'),

    path('books/add/', addBook, name='add_book'),
    path('persons/add/', addPerson, name='add_person'),

    path('books/delete/', deleteBook, name='delete_book'),
    path('persons/delete/', deletePerson, name='delete_person'),
]