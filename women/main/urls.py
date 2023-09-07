from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('showpost/<int:post_id>/', showpost, name='showpost'),
    path('addpost/', addpost, name='addpost')
]
