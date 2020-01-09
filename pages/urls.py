from django.urls import path

from .views import HomePageView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('main/', views.index, name= 'main'),
    path('main/save_calorie/', views.save, name= 'save'),
    path('main/delete/<int:caloriedata_id>/', views.delete, name = 'delete'),
]