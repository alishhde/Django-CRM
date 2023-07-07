from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_customer, name='delete_record'),
    path('add_record/', views.add_customer, name='add_record'),
    path('Update_record/<int:pk>', views.update_customer, name='Update_record'),

]
