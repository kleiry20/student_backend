from django.http import JsonResponse
from .models import Standard
from .serializers import StandardSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET', 'POST'])
def standard_list(request):
    if request.method == 'GET':
        standards = Standard.objects.all()
        serializer = StandardSerializer(standards, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = StandardSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def standard_detail(request, id):

    try:
        standard = Standard.objects.get(pk=id)
    except Standard.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        standards = Standard.objects.all()
        serializer = StandardSerializer(standards, many=True)
        return Response(serializer.data)    

    elif request.method == 'PUT':
        serializer = StandardSerializer(standard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:    
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        standard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

