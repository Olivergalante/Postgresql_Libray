
from rest_framework import viewsets
from .serializers import LibraySerializer
from .models import Libray

# Create your views here.


class LibrayViewSet(viewsets.ModelViewSet):
    queryset = Libray.objects.all().order_by('title')
    serializer_class = LibraySerializer
