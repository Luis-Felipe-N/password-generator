from django.urls import path
from generator import views

from generator.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]