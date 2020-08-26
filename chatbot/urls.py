from django.urls import path

from .views import index

urlpatterns = [
    path('<slug:question>/',index,name='index')
]
