from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer
# Create your views here.
@api_view(['GET'])
def getData(request):
    items=Item.objects.all()
    serializer=ItemSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer=ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update(request, id):
    user=Item.objects.get(id=id)
    serializer=ItemSerializer(data=request.data,instance=user)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, id):
    user=Item.objects.get(id=id)
    serializer=ItemSerializer(data=request.data,instance=user)
    
    user.delete()
    return Response(serializer.data)

