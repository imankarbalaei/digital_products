from django.urls import path
from .views import ProductListViews

urlpatterns = [
    path('products/', ProductListViews.as_view()),
]
