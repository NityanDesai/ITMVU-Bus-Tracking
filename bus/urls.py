from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('validate/', views.validate, name='validate'),
    path('admin/', auth_views.LoginView.as_view(template_name='bus/admin.html'), name='admin'),
    path('admin/welcome_admin/', views.welcome_admin, name='welcome_admin'),
    path('user/', auth_views.LoginView.as_view(template_name='bus/user.html'), name='user'),
    # path('driver/', auth_views.LoginView.as_view(template_name='bus/driver.html'), name='driver'),
    path('welcome_user/', views.welcome_user, name='welcome_user'),
    path('welcome_driver/', views.welcome_driver, name='welcome_driver'),
    path('reset/<int:pk>', views.reset, name='reset'),
    path('add_student/', views.add_student, name='add_student'),
    path('emergency/', views.emergency, name='emergency'),
    path('add_driver/', views.add_driver, name='add_driver'),
    path('change_password/', views.change_password, name='change_password'),
    path('change_pass/<str:username>', views.change_pass, name='change_pass'),
    path('edit_bus_details/<int:pk>', views.edit_bus_details, name='edit_bus_details'),
    path('edit_student_details/<str:pk>', views.edit_student_details, name='edit_student_details'),
    path('delete_bus_details/<int:pk>', views.delete_bus_details, name='delete_bus_details'),
    path('delete_student_details/<str:pk>', views.delete_student_details, name='delete_student_details'),
    path('view_bus_details/', views.view_bus_details, name= 'view_bus_details'),
    path('view_student_details/', views.view_student_details, name= 'view_student_details'),
    path('track_bus', views.track_bus, name='track_bus'),
    path('your_bus_details', views.your_bus_details, name='your_bus_details'),
    path('schedule', views.schedule, name='schedule'),
    path('about', views.about, name='about'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('driver_login', views.driver_login, name='driver_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]