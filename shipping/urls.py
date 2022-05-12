from django.urls import path

# from .views import (
#     PostCreateView,


# )
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('tarif/', views.tarifperkilo, name='tarif'),
    path('gantitarif/', views.ganti_tarif, name='ganti-tarif'),
]
