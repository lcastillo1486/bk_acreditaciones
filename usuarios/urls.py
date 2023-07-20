from django.urls import path
from usuarios import views

urlpatterns = [
    path('registro/',views.registro),
    path('',views.logear, name='inicial'),
    path('inicio/',views.inicio),
    path('logout/',views.cerrarSesion)

]