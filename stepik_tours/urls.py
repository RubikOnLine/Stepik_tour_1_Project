"""stepik_tours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from tours.views import MainView, DepartureView, TourView

urlpatterns = [
    path('', MainView.as_view(), name='Main_page_all_tours'),
    path('departure/<str:city_id>/', DepartureView.as_view(), name='Departure_from_city'),
    path('tour/<int:id>/', TourView.as_view(), name='Tour_description_page'),
]
