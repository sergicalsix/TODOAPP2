from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy
from django.urls import reverse


# Create your views here.
class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel #どのデータベースを参照するか
class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    #fields = ('内容', 'メモ', '優先度', '期日')
    success_url = reverse_lazy('list')


class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    #fields = ('内容', 'メモ', '優先度', '期日')
    success_url = reverse_lazy('list')
