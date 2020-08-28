from django.urls import path

#from .views import message_list
from . import views

urlpatterns = [
    #path('<slug:question>/',views.message_list, name='message-list')
    path('',views.message_list, name='message-list')
]
