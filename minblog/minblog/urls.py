from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('signup/', views.user_signup,name='signup'),
    path('login/', views.user_login,name='login'),
    path('logout/', views.user_logout,name='logout'),
    path('addPost/', views.addPost,name='addPost'),
    path('updatePost/<int:id>/', views.updatePost,name='updatePost'),
    path('deletePost/<int:id>/', views.deletePost,name='deletePost'),
]
