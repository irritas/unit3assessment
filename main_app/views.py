from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from .models import Item

class ItemList(ListView):
	model = Item

class ItemCreate(CreateView):
	model = Item
	fields = '__all__'

def items_delete(request, item_id):
	Item.objects.get(id=item_id).delete()
	return redirect('home')