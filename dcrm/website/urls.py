from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('records/<int:pk>', views.records, name='records'),
    path('edit_record/<int:pk>', views.edit_record, name='edit_record')

]
