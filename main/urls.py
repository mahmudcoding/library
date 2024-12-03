from django.urls import path
from .views import *

urlpatterns = [
    path('books/', getBooks, name='get_books'),
    path('persons/', getPersons, name='get_persons'),
    path('libraries/', getLibraries, name='get_libraries'),

    path('books/update/', updateBook, name='update_book'),
    path('persons/update/', updatePerson, name='update_person'),
    path('libraries/update/', updateLibrary, name='update_library'),

    path('books/add/', addBook, name='add_book'),
    path('persons/add/', addPerson, name='add_person'),
    path('libraries/add/', addLibrary, name='add_library'),

    path('books/delete/', deleteBook, name='delete_book'),
    path('persons/delete/', deletePerson, name='delete_person'),
    path('libraries/delete/', deleteLibrary, name='delete_library'),
]