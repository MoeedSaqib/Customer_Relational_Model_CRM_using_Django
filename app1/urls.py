  
from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views

urlpatterns =[
   
  path('register/', views.registerPage , name="register"),
  path('login/', views.loginPage , name="login"),
  path('logout/', views.logoutUser , name="logout"),
  
  path('', views.home , name="home"),


  path('user/',views.userPage , name="userPage"),
  path('account/',views.accountSettings , name="account"),
  path('products/',views.products , name="products"),
 
  path('customers/<str:pk_test>/',views.customers , name="customers") ,

  path('create_order/<str:pk>', views.createOrder , name="createOrder"),
  path('update_order/<str:pk>/', views.updateOrder , name="updateOrder"),
  path('delete_order/<str:pk>/', views.deleteOrder , name="deleteOrder"),
  path('reset_password/', auth_views.PasswordResetView.as_view(template_name="app1/reset_password.html"), name="reset_password"),
  path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="app1/password_reset_sent.html") ,name="password_reset_done"),
  path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
  path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),





]  
