from .models import Person
from  .serilizers import PersonModelSerializer
from rest_framework import viewsets

class ModelViewSetview(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer


class ModelViewReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer
