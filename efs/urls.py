from django.contrib import admin
from django.conf.urls import  include,url
from django.urls import path,re_path
from django.contrib.auth import views
from django.contrib.auth.views import LoginView , LogoutView
from django.views.generic import TemplateView

urlpatterns = [

    re_path ( r'^accounts/login/$' , LoginView.as_view ( template_name='registration/login.html' ) , name="login" ) ,
    re_path ( r'^accounts/logout/$' , LogoutView.as_view ( template_name='registration/logout.html' ) ,
              LogoutView.next_page ,
              name="logout" ) ,
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls'))

]
