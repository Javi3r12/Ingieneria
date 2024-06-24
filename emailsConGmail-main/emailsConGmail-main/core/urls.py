from django.urls import path
from . import views
from .views import index, contact,solicitud,soliFind

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('solicitudes',solicitud,name='solicitud'),
    path('cambioEstado/<str:pk>',soliFind,name='cambioEstado'),
    path('solicitudUpdate', views.solicitudUpdate, name='solicitudUpdate'),
]