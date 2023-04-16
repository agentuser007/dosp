from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    recommended_books = Book.objects.order_by('?')[:3]
    return render(request, 'book_list.html', {'books': books, 'recommended_books': recommended_books})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})
    

def book_edit(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
            #return render(request, 'book_form.html', {'form': form})
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})
    
def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('book_list')
    
def book_recommendation(request):
    books = Book.objects.all().order_by('?')[:3]
    return render(request, 'book_recommendation.html', {'books': books})