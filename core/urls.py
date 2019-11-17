from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt import views as jwt_views

# from djoser.contrib

urlpatterns = [
    path('admin/', admin.site.urls),

    # In-Build Auth related Urls
    path('auth/', include('djoser.urls')),

    # For TOKEN based urls
    path('auth/', include('djoser.urls.authtoken')),

    # for JWT Bearer TOKEN based urls
    path('auth/', include('djoser.urls.jwt')),

    path('auth/login/', jwt_views.obtain_jwt_token,
         name="auth"),  # Customize login
    # url(r'^auth/login/', jwt_views.obtain_jwt_token, name='auth'),


]
