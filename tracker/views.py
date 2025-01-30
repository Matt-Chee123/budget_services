from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Income
from .serializers import IncomeSerializer
from django.db.models import Sum
from users.auth import CustomJWTAuthentication



# Create your views here.
class TotalIncomeView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]

    def get(self,request):
        user_id = request.user.user_id
        incomes = Income.objects.filter(user=request.user)

        total_income = incomes.aggregate(total=Sum('income_amount'))['total'] or 0

        return Response({
            'total_income': total_income
        }, status=status.HTTP_200_OK)

class IncomeView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]

    def get(self, request):
        user_id = request.user.user_id
        incomes = Income.objects.filter(user=request.user)
        serializer = IncomeSerializer(incomes,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)