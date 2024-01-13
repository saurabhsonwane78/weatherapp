from . import views
from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [
    re_path('signup', views.signup),
    re_path('login', views.login),
    re_path('admin/', admin.site.urls),
    re_path('app/', include('app.urls')),
]