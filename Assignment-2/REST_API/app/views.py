from django.http import JsonResponse
from .models import User, Event
from .serializers import UserSerializer, UserViewSerializer, EventSerializer, EventViewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view # To avoid csrf token error


@api_view(['GET', 'POST'])
def userView(request): 
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == 'GET':

        Users = User.objects.all()
        serializer = UserViewSerializer(Users, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def eventView(request):   
    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == 'GET':

        Events = Event.objects.all()
        serializer = EventViewSerializer(Events, many=True)
        return JsonResponse(serializer.data, safe=False)
