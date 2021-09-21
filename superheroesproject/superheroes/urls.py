from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superhero'),
    path('update/<int:superhero_id>/', views.update, name='update_superhero'),
    path('delete/<int:superhero_id>/', views.delete, name='delete')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
