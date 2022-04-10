from django.shortcuts import render
from .models import  TodoListItem
from django.http import  HttpResponseRedirect
# Create your views here.


def index(request):
    all_todo_item = TodoListItem.objects.all()
    context = {
        'all_items': all_todo_item
    }
    return render(request, 'index.html', context)


def add_todo_item(request):
    content = request.POST['content']
    new_item = TodoListItem(content = content)
    new_item.save()
    return HttpResponseRedirect('/')


def delete_todo_item(request, id):
    data = TodoListItem.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect('/')
