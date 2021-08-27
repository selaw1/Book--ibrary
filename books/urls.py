from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.HomeView.as_view() ,name='home'),
    path('authors/', views.AuthorListView.as_view() ,name='authors'),
    path('authors/add/', views.AuthorCreateView.as_view() ,name='add_author'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view() ,name='author_detail'),
    path('author/<int:pk>/books/edit/', views.AuthorBooksEditView.as_view() ,name='author_book_edit'),
    
    path('login/', auth_views.LoginView.as_view(), name='login'  ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'  ),
]
