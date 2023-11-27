from django.urls import path
from accounts.views import login, signup, perfil,update
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/',login, name='login'),
    path('logout/',LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('signup/',signup, name='signup'),
    path('perfil/',perfil, name='perfil'),
    path('perfil/<int:id_user>/update',update, name='update')
]
