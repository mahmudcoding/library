from rest_framework.decorators import api_view
from django.http import JsonResponse
from main.models import *

@api_view(['GET'])
def getBooks(request):
    books = {} 
    for book in Book.objects.all():
        books[str(book.id)] = {
            'title': book.title,
            'author': book.author,
            'isAvailable': book.isAvailable,
            'rackNumber': book.rack_number,
            'subject': book.subject,
            'publicationDate': book.publication_date,
            'isBorrowed': book.isBorrowed,
            'borrowedPersonId': book.borrowed_person_id,
            'returnDate': book.return_date,
            'isReserved': book.isReserved,
            'reservedPersonId': book.reserved_person_id
            }
        
    return JsonResponse(books)

@api_view(['GET'])
def getPersons(request):
    persons = {}
    for person in Person.objects.all():
        persons[str(person.id)] = {
            'name': person.name,
            'age': person.age,
            'login': person.login,
            'password': person.password,
            'role': person.role,
        }
        
    return JsonResponse(persons)

@api_view(['POST'])
def updateBook(request):
    data = request.POST.dict()
    
    try:
        book = Book.objects.get(id=int(data['id']))
        book.title = data['title']
        book.author = data['author']
        book.isAvailable = data['isAvailable'].lower() == 'true'
        book.rack_number = int(data['rackNumber'])
        book.subject = data['subject']
        book.publication_date = int(data['publicationDate'])
        book.isBorrowed = data['isBorrowed'].lower() == 'true'
        book.borrowed_person_id = int(data['borrowedPersonId'])
        book.return_date = data['returnDate']
        book.isReserved = data['isReserved'].lower() == 'true'
        book.reserved_person_id = int(data['reservedPersonId'])
        book.save()

        return JsonResponse({'status': 'success'})
    except Book.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Book not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@api_view(['POST'])
def updatePerson(request):
    data = request.POST.dict()
    
    try:
        person = Person.objects.get(id=int(data['id']))
        person.name = data['name']
        person.age = int(data['age'])
        person.login = data['login']
        person.password = data['password']          
        person.role = data['role']
        person.save()

        return JsonResponse({'status': 'success'})
    except Person.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Person not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@api_view(['POST'])
def addBook(request):
    data = request.POST.dict()
    try:
        book = Book.objects.create(
            title=data['title'],
            author=data['author'],
            isAvailable=data['isAvailable'].lower() == 'true',
            rack_number=int(data['rackNumber']),
            subject=data['subject'],
            publication_date=int(data['publication_date']),
            isBorrowed=data['isBorrowed'].lower() == 'true',
            borrowed_person_id=int(data['borrowedPersonId']),
            return_date=data['returnDate'],
            isReserved=data['isReserved'].lower() == 'true',
            reserved_person_id=int(data['reservedPersonId'])
        )
        return JsonResponse({'status': 'success', 'id': book.id})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@api_view(['POST'])
def addPerson(request):
    data = request.POST.dict()
    try:
        person = Person.objects.create(
            name=data['name'],
            age=int(data['age']),
            login=data['login'],
            password=data['password'],
            role=data['role'],
        )
        return JsonResponse({'status': 'success', 'id': person.id})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@api_view(['POST'])
def deleteBook(request):
    data = request.POST.dict()
    try:
        book = Book.objects.get(id=int(data['id']))
        book.delete()
        return JsonResponse({'status': 'success'})
    except Book.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Book not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@api_view(['POST'])
def deletePerson(request):
    data = request.POST.dict()
    try:
        person = Person.objects.get(id=int(data['id']))
        person.delete()
        return JsonResponse({'status': 'success'})
    except Person.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Person not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)