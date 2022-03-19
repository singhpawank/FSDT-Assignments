from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import user, item, booking
from .serializers import userSerializer, itemSerializer, bookingSerializer
from django.db.models import Q

def is_overlap(item_id_, startDate_, endDate_):
    bookings =  booking.objects.filter(item_id=item_id_)
    bookings1 =  bookings.filter(Q(startDate__lte=startDate_) & Q(endDate__gte=startDate_))

    bookings2 =  bookings.filter(Q(startDate__lte=endDate_) & Q(endDate__gte=endDate_))

    if (bookings1.count() == 0 and bookings2.count()==0) :
        return False

    return True


@api_view(['POST', 'GET'])
def userView(request):
    if request.method == 'POST':
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)

    elif request.method == 'GET':
        users = user.objects.all()
        serializer = userSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)



@api_view(['POST', 'GET'])
def itemView(request):
    if request.method == 'POST':
        serializer = itemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)

    elif request.method == 'GET':
        items = item.objects.all()
        serializer = itemSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)



@api_view(['POST', 'GET'])
def bookingView(request):
    if request.method == 'POST':
        serializer = bookingSerializer(data=request.data)
        if serializer.is_valid():
            item_id = serializer.validated_data.get('item_id')
            startDate = serializer.validated_data.get('startDate')
            endDate = serializer.validated_data.get('endDate')
            if(not is_overlap(item_id, startDate, endDate)):
                serializer.save()
                return Response(serializer.data)

            else:
                return JsonResponse({'message':'This booking for the item is overlapping with another booking.'})

        else:
            return Response(serializer.errors)
    
    elif request.method == 'GET':
        bookings = booking.objects.all()
        serializer = bookingSerializer(bookings, many=True)
        return JsonResponse(serializer.data, safe=False)
        

