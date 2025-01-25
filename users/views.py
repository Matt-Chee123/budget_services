from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            response = JsonResponse({
                'message': 'Login Successful'
            })
            response.set_cookie('access_token',access_token,httponly=True,secure=True,samesite='None',max_age=30*60)
            response.set_cookie('refresh_token',refresh_token,httponly=True,secure=True,samesite='None',max_age=2*60*60)
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response({"message": "Hello, World!"}, status=status.HTTP_200_OK)