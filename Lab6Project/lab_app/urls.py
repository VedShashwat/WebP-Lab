from django.urls import path
from . import views

urlpatterns = [
    path('arithmetic/', views.arithmetic_view, name='arithmetic'),
    path('magazine/', views.magazine_view, name='magazine'),
    # We will add other paths here later
]