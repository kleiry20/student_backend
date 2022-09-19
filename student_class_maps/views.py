
from .models import StudentClassMap
from .serializers import StudentClassMapSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def map_list(request):
    if request.method == 'GET':
        maps = StudentClassMap.objects.all()
        serializer = StudentClassMapSerializer(maps, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = StudentClassMapSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def map_detail(request, id):

    maps = StudentClassMap.objects.filter(studID=id)
    serializer = StudentClassMapSerializer(maps, many=True)
    return Response(serializer.data)
    


