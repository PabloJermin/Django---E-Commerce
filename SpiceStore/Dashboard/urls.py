from django.urls import path
from item import views as vw
from . import views

app_name = 'Dashboard'


urlpatterns = [
    path('', views.index, name= 'index'),
    path('<int:pk>/', vw.detail, name='delete')
    
]
