from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Accounts
from .serializers import AccountsSerializer
from users.auth import CustomJWTAuthentication

class UserAccountsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]

    def get(self, request):
        user_id = request.user.user_id
        accounts = Accounts.objects.filter(user=user_id)
        accountSerializer = AccountsSerializer(data=accounts)
        print("xxxxxxxxxxxxxxxxxxxxxx",accounts,accountSerializer)

        return Response(accounts)