from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('<int:question_id>/user/', views.user, name='user'),

    path('<int:question_id>/status', views.status, name='status'),

    path('<int:question_id>/update', views.update, name='update'),
    

    path('order_confirmed', views.order),


]
