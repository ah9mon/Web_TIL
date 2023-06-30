from django.urls import path
from . import views

app_name = 'scorings'

urlpatterns = [
    path('submits', views.get_user_code, name='get_user_code'),
    path('scorings', views.score_user_code, name = 'score_user_code'),
]
