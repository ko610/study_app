from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('home/', views.PostQuestionListView.as_view(), name='index')
]