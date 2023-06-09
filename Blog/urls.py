from django.urls import path
from . import views
urlpatterns =[
    path('',views.list,name='list'),
    path('list/<int:id>',views.blog,name='blog' ),
    path('blog_create',views.blog_create,name='blog_create'),
    path('product_create',views.product_create,name='product_create')
]