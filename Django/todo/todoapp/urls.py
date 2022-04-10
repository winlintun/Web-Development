from django.urls import path
from . import views

appname = "todoapp"

urlpatterns = [
    path('', views.index, name="index"),
    path('add_todo_item/', views.add_todo_item, name="add_todo_item"),
    path('deleteTodoItem/<int:id>/', views.delete_todo_item, name="delete_todo_item"),
]