from django.urls import path
from . import views

app_name = "apitest"
urlpatterns = [
    path("kakao", views.kakao_local_map, name="kakaoLocalMap"),
    path("naver", views.naver_local_map, name="naverLocalMap" ),
]
