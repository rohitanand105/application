from django.contrib import admin
from django.urls import path

from .views import home_view, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', home_view.as_view(), name='home'),
    # path('', homePageView, name='home')
]

