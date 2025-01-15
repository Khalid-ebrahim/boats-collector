from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('boats/', views.boats_index, name='index'),
    path('boats/<int:boat_id>/', views.boats_detail, name='detail'),
    path('boats/create/', views.BoatCreate.as_view(), name='boats_create'),
    path('boats/<int:pk>/update/', views.BoatUpdate.as_view(), name='boats_update'),
    path('boats/<int:pk>/delete/', views.BoatDelete.as_view(), name='boats_delete'),
    path('boats/<int:boat_id>/add-servicing', views.add_servicing, name='add_servicing'),

    path('flags/', views.FlagList.as_view(), name='flags_index'),
    path('flags/<int:pk>/', views.FlagDetail.as_view(), name='flags_detail'),
    path('flags/create/', views.FlagCreate.as_view(), name='flags_create'),
    path('flags/<int:pk>/update/', views.FlagUpdate.as_view(), name='flags_update'),
    path('flags/<int:pk>/delete/', views.FlagDelete.as_view(), name='flags_delete'),


    path('boats/<int:boat_id>/assoc_flag/<int:flag_id>/', views.assoc_flag, name='assoc_flag'),


    path('boats/<int:boat_id>/unassoc_flag/<int:flag_id>/', views.unassoc_flag, name='unassoc_flag'),
]