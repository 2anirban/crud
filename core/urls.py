
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.list_clients,name="clients_list"),
    path("new",views.new_clients),
    path("update/<int:id>",views.update_client,name="client_update"),
    path("delete/<int:id>", views.delete_client, name="client_delete"),

]
