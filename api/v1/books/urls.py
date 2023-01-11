from django.urls import path
from api.v1.books import views


app_name = 'api_v1_books'

urlpatterns = [
    path('list-all/', views.list_all_books),
    path('views/<int:pk>/', views.single_book_details),
    path('update/<int:pk>/',views.update_book),
    path('delete/<int:pk>/',views.delete_book)

   
]
