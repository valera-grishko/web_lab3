from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import RegistrationSerializer, ProfileSerializer


class RegistrationAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer


class ProfileAPIView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
