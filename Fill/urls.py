from django.urls import path
from .views import post_view

app_name = "Fill"

urlpatterns = [
    path('form/', post_view, name='form_post'),
]
