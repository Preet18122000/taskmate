from django.contrib import admin
from django.urls import path,include
from todolist import views as todolist_views
from user import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('user.urls')),
    path('task/',include('todolist.urls')),
    path('contact',todolist_views.contact, name='contact'),
    path('about',todolist_views.about, name='about'),
    path('',todolist_views.index, name='index'),
]
