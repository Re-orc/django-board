from django.urls import path
from .  import views

app_name='notice'
urlpatterns = [
    path('',views.listview,name='list'),
    path('detail/<int:pk>',views.detailview,name='detail'),
    path('create/',views.createview,name='create'),
    path('update/<int:pk>',views.updateview,name='update'),
    path('delete/<int:pk>',views.deleteview,name='delete'),
    path('signup',views.register,name='register'),

]
