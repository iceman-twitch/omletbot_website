from django.urls import path
from . import views
handler404 = 'sites.views.handler404'
app_name="sites"
urlpatterns = [
    path('', views.home, name="home"),
    path('error/', views.error, name="error"),
    path('api/', views.api,name='api'),
    path('shop/', views.shop,name='shop'),
    path('freetrial/',views.freetrial,name='freetrial')
]