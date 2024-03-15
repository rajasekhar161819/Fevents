from django.urls import path
from .views import ListEvent, ListEventParticularUser, CreateEvent, LoginAPIView, SignupAPIView


urlpatterns = [

    path('', ListEvent.as_view()),
    path('particularuser', ListEventParticularUser.as_view()),
    path('createevent', CreateEvent.as_view()),
    path('login', LoginAPIView.as_view()),
    path('signup', SignupAPIView.as_view()),

]
