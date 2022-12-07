from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('sign_in', views.LoginFormView.as_view(), name='sign_in'),
    path('download', views.download, name='download'),
    path('register', views.RegisterFormView.as_view(), name='register'),
    path('log_out1', views.log_out1, name='log_out1'),
    path('log_out', views.LogoutView.as_view(), name='log_out'),
    path('sug_edit', views.sug_edit, name='sug_edit')

]