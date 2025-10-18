from django.urls import path

from todoapp import views

urlpatterns = [
    path('create/', views.TodoListCreateAPIView.as_view()),
    path('list/', views.TodoListCreateAPIView.as_view()),
    path('delete/<int:pk>/', views.TodoDestroyAPIView.as_view()),
]
