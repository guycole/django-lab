
from django.urls import path

from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.IndexView.as_view(), name='app1-index'),

    path('ok/', views.ok, name='ok'),

    path('alpha/create/', views.AlphaCreate.as_view(), name='alpha-create'),
    path('alpha/<int:pk>/delete/', views.AlphaDelete.as_view(), name='alpha-delete'),
    path('alpha/<int:pk>/update/', views.AlphaUpdate.as_view(), name='alpha-update'),
]