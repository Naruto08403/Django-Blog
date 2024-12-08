from django.urls import path
from . import views

app_name = 'vlog'

urlpatterns = [
    path('', views.VlogListView.as_view(), name='vlog_list'),
    path('<int:pk>/', views.VlogDetailView.as_view(), name='vlog_detail'),
    path('new/', views.VlogCreateView.as_view(), name='vlog_create'),
    path('edit/<int:pk>/', views.VlogUpdateView.as_view(), name='vlog_edit'),
]
