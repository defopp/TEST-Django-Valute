from django.urls import path

from .views import MainView, RateView



urlpatterns = [
    path('', MainView.as_view(), name='MainView'),
    path('rate/', RateView.as_view(), name='RateView'),
]
