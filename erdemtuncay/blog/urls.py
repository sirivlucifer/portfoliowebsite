from django.urls import path
from . import views

urlpatterns = [    #name="" kısmının içini adres cubugunda göreceğiz. istediğimiz gibi değiştrebiliyoruz. kaynak: https://tutorial.djangogirls.org/en/django_urls/
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
]