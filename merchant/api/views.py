from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from merchant.api.serializers import ApplicationSerializer, ChannelSerializer


class ApplicationAPIAPIView(APIView):
    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    
    
class ChannelAPIAPIView(APIView):
    def post(self, request):
        serializer = ChannelSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response("Başvurunuz Tamamlandı", status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    