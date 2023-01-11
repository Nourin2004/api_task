from books.models import Books
from api.v1.books.serializers import BookListingSerializer , BookDetailSerializer, DeleteBookSerializer , AddContentserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated


@api_view(['GET'])
@permission_classes((AllowAny,))
def list_all_books(request):
    instances = Books.objects.filter(is_deleted = False)
    context = {
        "request":request
    }
    serializer = BookDetailSerializer(instances, many=True, context=context, )

    response_data = {
        "StatusCode":6000,
        "data": serializer.data
    }

    return Response(response_data)



@api_view(['GET'])
@permission_classes((AllowAny,))
def single_book_details(request, pk):
    if Books.objects.filter(pk=pk).exists():
        instance = Books.objects.get(pk=pk)
        serializer = BookDetailSerializer(instance)

        response_data = {
            "StatusCode":6000,
            "data": serializer.data
        }

    else:
        response_data = {
                "StatusCode": 6001,
                "data":{
                    "message":"Book Not Found !!"
                }
            }
    return Response(response_data)



@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def delete_book(request, pk):
    if Books.objects.filter(pk=pk).exists():
        instance = Books.objects.get(pk=pk)
        serializer = DeleteBookSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            response_data = {
                "StatusCode":6000,
                "data": {
                    "message": "deleted the book successfully",
                    "status": "success"
                }
            }
        else:
            response_data = {
                "StatusCode": 6001,
                "data": {
                    "message": "Validation Error",
                    "data": serializer.errors
                }
            }
        return Response(response_data)
    
    else:
        response_data = {
             "StatusCode": 6001,
             "data": {
                 "message": "Book Not Found !!",
                }
            }
    return Response(response_data)
    

@api_view(['POST'])    
@permission_classes((IsAuthenticated,)) 
def update_book(request, pk):
    if Books.objects.filter(pk=pk).exists():
        instance = Books.objects.get(pk=pk)
        serializer = BookDetailSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
           serializer.save()

           response_data = {
                 "StatusCode": 6000,
                 "data": {
                     "message": "Updated The Book Successfully",
                     "status": "Success"
                }
           }
        else:
            response_data = {
                "StatusCode": 6001,
                "data": {
                    "message": "Validation Error",
                    "data": serializer.errors
                }
            }

    else:
        response_data = {
             "StatusCode": 6001,
             "data": {
                 "message": "Book Not Found !!",
                }
            }
    return Response(response_data)
