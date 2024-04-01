from django.contrib import admin
from django.urls import path, include
from .views import payment_status
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('menu',views.menu, name='menu'),
    path('reservation',views.reservavtion,name='reservation'),
    path('blog',views.blog,name='blog'),
    path('blog-detail',views.blog_detail,name='blog_detail'),
    path('login',views.login,name='login'),
    path('item',views.item,name='item'),
    path('additem',views.additem,name='additem'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('track',views.track,name='track'),
    path('login',views.login,name='login'),
    path('regs',views.regs,name='regs'),
    path('cart',views.cart,name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('list_items/', views.item, name='list_items'),
    path('add_items/', views.additem, name='add_items'),
    # path('payment',views.payment, name='payment'),
    path('payment-status',views.payment_status, name='payment-status')
    # path('update_items/<str:pk>/', views.update_items, name="update_items"),
    # path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
]


