from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Person
from .serilizers import PersonModelSerializer

# This class has read and create a object
class PersonListCreate(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer

# This class manage Retrieve update and destroy a object
class PersonRetDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class= PersonModelSerializer

