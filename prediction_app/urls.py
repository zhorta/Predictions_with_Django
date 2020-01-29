from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('postures/', views.i_want_a_list, name='list_of_postures'),
    path('predict/', views.predict, name='to_predict')
]