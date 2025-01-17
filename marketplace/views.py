from rest_framework import generics, permissions
from .models import Garment
from .serializers import GarmentSerializer

class GarmentListView(generics.ListAPIView):
    queryset = Garment.objects.all()
    serializer_class = GarmentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        garment_type = self.request.query_params.get('type')
        if garment_type:
            queryset = queryset.filter(type=garment_type)
        return queryset

class GarmentCreateView(generics.CreateAPIView):
    queryset = Garment.objects.all()
    serializer_class = GarmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)

class GarmentUpdateView(generics.UpdateAPIView):
    queryset = Garment.objects.all()
    serializer_class = GarmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(publisher=self.request.user)

class GarmentDeleteView(generics.DestroyAPIView):
    queryset = Garment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(publisher=self.request.user)
