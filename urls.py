from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from store import views


urlpatterns = [
  path('',views.index,name='home'),
  path('signups',views.signup,name="signup"),
  path('login', views.login_view, name="login"),
  path('Query_Set/<str:course>', views.Query_Set),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)