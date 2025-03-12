from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Accounts
from .models import Investment
from .serializers import AccountsSerializer
from .serializers import InvestmentSerializer
from users.auth import CustomJWTAuthentication

class UserAccountsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]

    def get(self, request):
        user_id = request.user.user_id
        accounts = Accounts.objects.filter(user=user_id)
        serializer = AccountsSerializer(accounts, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class InvestmentsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]

    def get(self, request):
        account_uid = request.GET.get("account_uid")  # Fetch from query parameters

        if not account_uid:
            return Response({"error": "account_uid is required"}, status=400)

        investments = Investment.objects.filter(account__uid=account_uid)
        serializer = InvestmentSerializer(investments, many=True)
        return Response(serializer.data)
