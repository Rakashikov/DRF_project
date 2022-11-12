from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Woman
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdminOrReadOnly
from .serializers import WomanSerializer
from .pagination import WomanAPIListPagination


class WomanAPIListCreateView(generics.ListCreateAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
    permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    pagination_class = WomanAPIListPagination


class WomanAPIUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]


class WomanAPIDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
    permission_classes = [IsAdminOrReadOnly]
