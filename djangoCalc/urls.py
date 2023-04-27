from django.contrib import admin
from django.urls import path, include
from calc import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calc/', include("calc.urls")),
    path('', views.index),
    path("__reload__/", include("django_browser_reload.urls")),
]
