from django.contrib import admin
from django.urls import path,include
from .views import home,signup,login,back,cart,checkout,ordersv
from .views.login import logout
from django.conf.urls.static import static
from .middlewares.auth import auth_middleware


urlpatterns = [
    path('',home.Index.as_view(),name='homepage'),
    path('signup',signup.Signup.as_view(),name = 'signup'),
    path('login', login.Login.as_view(), name='login'),
    path('back',back.Store.as_view(), name = 'back'),
    path('logout',logout, name = 'logout'),
    path('cart',cart.Cart.as_view(), name = 'cart'),
    path('check-out',checkout.Check.as_view(),name='checkout'),
    path('orders', auth_middleware(ordersv.OrdersV.as_view()), name='orders')
]
