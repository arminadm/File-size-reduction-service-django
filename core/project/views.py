from rest_framework.generics import GenericAPIView
from rest_framework.views import Response
from rest_framework import status
from .serializers import UploadSerializer

# Create your views here.
class upload(GenericAPIView):
    serializer_class = UploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)