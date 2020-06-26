from django.urls import path
from . import views

urlpatterns = [
	path('', views.ItemList.as_view(), name='home'),
	path('add/', views.ItemCreate.as_view(), name='items_create'),
	path('<int:item_id>/delete/', views.items_delete, name='items_delete'),
]