from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('records/<int:pk>', views.records, name='records'),
    path('edit_record/<int:pk>', views.edit_record, name='edit_record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('create_record/', views.create_record, name='create_record')

]
