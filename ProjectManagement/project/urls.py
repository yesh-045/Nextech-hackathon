from django.contrib import admin
from django.urls import path
from . import views
app_name = 'project'

urlpatterns = [
    path('list/',views.list,name='list' ),
    path("add/",views.add_project,name='add'),
    path('<uuid:pk>/details/',views.details,name='details'),
    path('<uuid:pk>/edit/',views.edit_project,name='edit'),
    path('<uuid:pk>/delete/',views.delete_project,name='delete')
]
