


from django.urls import path

from app import views, adminviews

urlpatterns = [
    path('login_view', views.login_view, name='login_view'),
    path('admin_home', views.image, name='admin_home'),
    path('Add_hospital', adminviews.add_hospital, name='Add_hospital'),
    path('viewhospital', adminviews.view_hospital, name='viewhospital'),

]