from django.urls import path
from app3 import views

urlpatterns = [
    path('var/', views.var),
    path('for_label/', views.for_label),
    path('filter/', views.filter),
    path('html_filter/', views.html_filter),
    path('diy_filter/', views.diy_filter),
    path('diy_tags/', views.diy_tags),
    path('show_info/', views.show_info),
    path('welcome/', views.welcome),
    path('welcome_include/', views.welcome_include),
]