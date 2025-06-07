




from django.urls import path
from . import views
urlpatterns= [path('',views.saludo),

    path('saludo/<str:nombre>/', views.saludar_usuario),
    
 
    path('numero/<int:numero>/', views.mostrar_numero),
    ]
