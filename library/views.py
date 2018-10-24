from django.shortcuts import render
from django.template import Context , Template
from .models import books , books_in_use
from django.shortcuts import HttpResponse

# Create your views here.
insert_result = ""

def addbook(request):
    return render(request,'insert.html')

def indexresult(request):
    c = Context({'insert_result': insert_result, })
    bookName = request.GET.get('bookName',False)
    boodId = request.GET.get('bookId', False)
    boodNumber = request.GET.get('bookNumber', False)

    a = books(book_name=bookName, book_id=boodId,number_of_books=boodNumber)
    a.save()
    return render(request,'insertResult.html')

def search(request):

    return render(request,'search.html')

def searchresult(request):
    link='http://localhost:8000/library/'
    co = Context({'insert_result': insert_result, })
    bookName = request.GET.get('bookName',False)
    search_result = books.objects.filter(book_name__icontains=bookName)
    return render(request,'searchResult.html',{'search_results': search_result,'link':link })
def theBook(request,bookId):
    global  bookIdd
    bookIdd = bookId

    return render(request,'theBook.html')

def theBookResult(request):

    keeperFirstName = request.GET.get('keeperFirstName',False)
    keeperLastName = request.GET.get('keeperLastName',False)
    keeperStudentId= request.GET.get('keeperStudentId',False)
    tempBook = books.objects.get(book_id=bookIdd)
    tempBook.number_of_books - 1
    book_in_use=books_in_use(book_name=tempBook.book_name , keeper_first_name=keeperFirstName , keeper_last_name=keeperLastName , keeper_id= keeperStudentId)
    book_in_use.save()
    tempBook.save()
    return render(request,'theBookResult.html')
def keepersList(request):
    link='http://localhost:8000/library/keepers/'

    keepers_list = books_in_use.objects.all()
    return render(request,'keeperslist.html',{'keepers_list':keepers_list,'link':link})

def keeperPage(request,id):
    global idd
    idd = id
    theKeptBook =  books_in_use.objects.get(id=idd)

    return render(request,'keeperPage.html' , {'book':theKeptBook})

def keeperPageResult(request):
    book_released = books_in_use.objects.get(id=idd)
    book_released.delete()
    bookplus = books.objects.get(book_name=book_released.book_name)
    bookplus.number_of_books + 1
    bookplus.save()
    return render(request,'keeperPageResult.html')



