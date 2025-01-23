from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Income
from .serializers import IncomeSerializer


# Create your views here.

class IncomeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user_id = request.query_params.get("user_id")
        incomes = Income.objects.filter(user_id=user_id)
        serializer = IncomeSerializer(incomes,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)