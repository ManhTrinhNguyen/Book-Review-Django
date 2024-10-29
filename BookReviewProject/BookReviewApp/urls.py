from django.urls import path 
from . import views 

urlpatterns = [
  path('', views.list_view, name='book_list'),
  path('book/<int:pk>/', views.book_detail_view, name = 'book_detail'),
  path('book/add/', views.add_book_view, name = 'add_book'),
  path('book/<int:pk>/review/', views.add_review_view, name = 'add_review'),
  path('book/<int:book_pk>/review/<int:review_id>/edit/', views.edit_book_review, name='edit_review'),
]