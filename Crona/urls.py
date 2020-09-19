from django.contrib import admin
from django.urls import path
from .Api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home),
    path("Api/",views.GlobalView.as_view()),
    path("Api/<slug:country>/",views.CountryView.as_view())
]
