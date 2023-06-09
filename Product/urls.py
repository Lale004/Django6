from django.urls import path
from . import views
urlpatterns =[
    path('list1',views.list1,name='list1'),
     path('list2',views.list2,name='list2'),
]