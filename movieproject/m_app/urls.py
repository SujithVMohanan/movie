from django.urls import path
from . import views
app_name = 'm_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:mid>/', views.details, name='details'),
    path('add/', views.add_movie, name='add'),
    path('update/<int:sid>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]

