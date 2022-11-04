from django.urls import path
from . import views
from .views import ArithmeticCalculatorView
app_name = "arithmetic operation"

urlpatterns = [
    path('', ArithmeticCalculatorView.as_view(), name='api_view'),
]
