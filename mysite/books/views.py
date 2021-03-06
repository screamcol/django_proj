from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from books.models import Book

# Create your views here.

#def search_form(request):
#    return render_to_response('search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Введите поисковой запрос')
        elif len(q)>20:
            errors.append('Введите не более 20 символов')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'books':books, 'query':q})
    return render_to_response('search_form.html', {'errors':errors})


