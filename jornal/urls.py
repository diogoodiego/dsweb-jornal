from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name='jornal'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login_view.as_view(), name='login'),
    path('register',views.register_view.as_view(), name='register'),
    path('logout',views.logout_view, name='logout'),

    #path('home',views.home.as_view(), name='home'),
    #path('noticia',views.noticia_view.as_view(), name='noticia'),
    #path('noticia/<int:noticia_id>/', views.noticia_detalhe.as_view(), name='noticia_detalhe')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)