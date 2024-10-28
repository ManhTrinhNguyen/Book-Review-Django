from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Review 
from .forms import BookForm, ReviewForm 

# Create your views here.

# List View 
def list_view(request):
  print(request.headers)
  books = Book.objects.all()
  return render(request, 'book_list.html', {'books': books})

# Detail View
def book_detail_view(request, pk):
  
  book = get_object_or_404(Book, pk=pk)
  reviews = book.reviews.all() # reviews from related name 
  return render(request, 'book_detail.html', {'book': book, 'reviews': reviews})

def add_book_view(request):
  form = BookForm()
  if request.method == 'POST':
    form = BookForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('book_list')
  
  return render(request, 'book_form.html', {'form': form})


def add_review_view(request, pk):
  book = get_object_or_404(Book, pk=pk)
  form = ReviewForm()
  if request.method == 'POST':
    form = ReviewForm(request.POST)
    if form.is_valid():
      review = form.save(commit=False)
      review.book = book 
      review.save()
      return redirect('book_detail', pk=book.pk)
  
  return render(request, 'review_form.html', {'form': form, 'book': book})
