from django.urls import path

# from hello import views
#
# app_name = 'hello'
# # urlpatterns = [
# #     #path('', views.index, name="index"),
# #     re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.index, name='index'),
# # ]
# urlpatterns = [
# path('hello/', views.index, name='index'),
# ]
from . import views
urlpatterns = [
    path('', views.index, name='index')
]