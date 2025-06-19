




from django.urls import path
from . import views
urlpatterns= [
    path('default/',views.default),

    path('saludo/<str:nombre>/', views.saludar_usuario),
    
    path('numero/<int:numero>/', views.mostrar_numero),
    
    path('curriculum/', views.mostrar_curriculum),
    
    path('',views.inicio, name='inicio'),
    ]