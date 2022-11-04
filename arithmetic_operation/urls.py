from django.urls import path
from . import views
from .views import ArithmeticCreateAPIView
app_name = "arithmetic operation"

urlpatterns = [
    path('', ArithmeticCreateAPIView.as_view(), name='api_view'),
]
