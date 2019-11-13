from django.urls import path
from . import views


app_name = 'Dappajyeo'
urlpatterns = [
    path('', views.index, name='index'),
    path('training/', views.training, name='training'),
    path('fatCalculator/', views.calculator, name='calculator'),
]