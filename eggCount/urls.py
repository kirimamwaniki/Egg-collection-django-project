from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('rooms', views.room_register, name='room_register'),
    path('records', views.view_records, name='records'),
    path('details/<int:id>', views.room_details, name='details'),
    path('<int:id>', views.pdf_format, name='pdf')
]