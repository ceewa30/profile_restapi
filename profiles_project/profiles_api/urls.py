from django.urls import path, include
from .views import (
    HelloApiView,
)

urlpatterns = [
    path('hello_api', HelloApiView.as_view()),
]