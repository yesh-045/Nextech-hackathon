from django.urls import path
from django.contrib import admin
from . import views
app_name="projectflow"
urlpatterns = [
    path('', views.index, name='index'),  
    path('base/',views.base,name='base'),
    path('admin/', admin.site.urls),
    path("about/",views.about,name="about"),
    path("alogin/",views.alogin,name="afterlogin"),
    path("profile/",views.profile, name="profile"),
    path("editprofile/",views.editprofile, name="editprofile"),

   
]
