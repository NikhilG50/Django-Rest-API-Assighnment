from django.urls import path
from .views import author_list, book_list,book_detail, author_detail


urlpatterns = [
    path('author/', author_list),
    path('book/', book_list),
    path('book_detail/<int:pk>/',book_detail),
    path('author_detail/<int:pk>/',author_detail),
]