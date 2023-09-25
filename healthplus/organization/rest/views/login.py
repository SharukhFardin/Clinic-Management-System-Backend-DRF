from rest_framework import generics
from rest_framework.response import Response

from ..serializers.login import UserLoginSerializer


class UserLoginView(generics.CreateAPIView):
    ''' Login View for all kind of users '''
    permission_classes = []
    serializer_class = UserLoginSerializer