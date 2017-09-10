from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, {'template_name': 'authentication/index.html'}, name='index'),
    url(r'^home/', views.home, {'template_name': 'authentication/home.html'}, name='home'),
    url(r'^login/', views.login_view, {'template_name': 'authentication/login.html'}, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^sign_up/', views.sign_up, {'template_name': 'authentication/sign_up.html'},
        name='sign_up'),
]
