from django.urls import path

from . import views
app_name="todolist"
urlpatterns = [
    path('todolist/<uuid:project_id>/add/', views.add, name='add'),  
]