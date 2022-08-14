from django.urls import path

from .views import aboutPageView, homePageView, roboPageView

urlpatterns = [
    path('', homePageView.as_view() , name='home'),
    path('about/' , aboutPageView.as_view(), name='about'),
    path('robo/', roboPageView.as_view(), name='robo'),
]