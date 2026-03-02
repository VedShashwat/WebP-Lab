from django.urls import path
from . import views

urlpatterns = [
    path('', views.promotion_view, name='promotion_check'),
]