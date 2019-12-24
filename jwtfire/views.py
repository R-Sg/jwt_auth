from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from jwtfire.serializers import StudentSerializer
from jwtfire.models import *
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        breakpoint()
        content = {'message': 'Hello, World!'}
        return Response(content)
