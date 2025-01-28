from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Income
from .serializers import IncomeSerializer
from users.auth import CustomJWTAuthentication



# Create your views here.

class IncomeView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]

    def get(self, request):
        incomes = Income.objects.all()
        serializer = IncomeSerializer(incomes,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)