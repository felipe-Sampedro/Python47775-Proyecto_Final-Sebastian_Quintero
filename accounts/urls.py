from django.urls import path
from accounts.views import login, signup, perfil,update,CamnbioPassword
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/',login, name='login'),
    path('logout/',LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('signup/',signup, name='signup'),
    path('perfil/',perfil, name='perfil'),
    path('perfil/<int:id_user>/update',update, name='update'),
    path('perfil/update/password',CamnbioPassword.as_view(), name='cambiar_password')
]
