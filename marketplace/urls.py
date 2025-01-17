from django.urls import path
from .views import GarmentListView, GarmentCreateView, GarmentUpdateView, GarmentDeleteView

urlpatterns = [
    path('clothes/', GarmentListView.as_view(), name='garment-list'),
    path('clothes/create/', GarmentCreateView.as_view(), name='garment-create'),
    path('clothes/<int:pk>/update/', GarmentUpdateView.as_view(), name='garment-update'),
    path('clothes/<int:pk>/delete/', GarmentDeleteView.as_view(), name='garment-delete'),
]
