from django.urls import path
from . import views

urlpatterns = [
    path('create-account-step1/', views.create_account_step1, name='create_account_step1'),
    path('create-account-step2/', views.create_account_step2, name='create_account_step2'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard_view, name='admin-dashboard'),
    path('logs/add/', views.add_log, name='add-log'),
    path('logs/delete/<int:log_id>/', views.delete_log, name='delete-log'),
]