from django.urls import path
from . import views
app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='register'),
    path('masters/departments', views.departments, name='departments'),
    path('masters/Places', views.places, name='places'),
    path('masters/Generals', views.generals, name='generals'),
    path('masters/GenTypes', views.genTypes, name='genTypes'),
    path('masters/distypes', views.disType, name='disTypes'),
    path('masters/RegTypes', views.regTypes, name='regtypes'),
    path('masters/Pages', views.pages, name='pages'),
    path('masters/menus', views.menus, name='menus'),
    path('masters/incomeExpenses', views.incomeExpenses, name='incomeExpenses'),
    path('masters/hospitals', views.hospitals, name='hospitals'),
    path('masters/users', views.users, name='users'),
    path('masters/professionals', views.professionals, name='professionals'),
]
