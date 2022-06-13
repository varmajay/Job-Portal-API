from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import *
from .serializers import *
from .models import *  
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import *
from rest_framework.decorators import api_view
#Generate Token manually

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }




# Create your views here.
@api_view(['GET'])
def index(request):
    url_pattern = {
        "Admin":'admin-profile/',
        "View HR":'hr-view/',
        "Edit HR":'hr-edit/id',
        "Delete HR":'hr-delete/id',
        "View Application for Admin":'admin-app',
        "Register":'register/',
        "HR Profile":'hr-profile/id',
        "Post Job":'job-post/',
        "View Job":'job-view/',
        "Edit Job":'job-edit/id',
        "Delete Job":'job-delete/id',
        "View Appliction for HR":'hr-app/',
        "Apply for Application":'apply/'
    }
    return Response(url_pattern)

class LoginAPI(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request, fromat=None):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token, 'msg':'login Sucessfully'},status=status.HTTP_200_OK)
            else:
                return Response({'msg':"invalid username and password "},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# --------------------------admin-------------------------------
class ProfileViewAPI(ListAPIView):
    queryset = User.objects.filter(role='admin')
    serializer_class = UserViewSerializer
    permission_classes = [IsAdminUser]



class HrviewAPI(ListAPIView):
    queryset = User.objects.filter(role='hr')
    serializer_class = UserViewSerializer
    permission_classes = [IsAdminUser]



class HrEditAPI(RetrieveUpdateAPIView):
    queryset = User.objects.filter(role='hr')
    serializer_class = UserViewSerializer
    permission_classes =[IsAdminUser]


class HrDeleteAPI(GenericAPIView):
    permission_classes =[IsAdminUser]
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserViewSerializer(user)
        return Response(serializer.data)

    def delete(self,request,pk):
        user = self.get_object(pk)
        user.delete()
        return Response('data deleted sucessfully')


class ApplicationAPI(ListAPIView):
    permission_classes =[IsAdminUser]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

# ----------------------------HR---------------------------------- #


class RegisterAPI(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    def post(self,request):
        serializer = UserCreateSerializer(data = request.data)
        if serializer.is_valid():
            # subject = 'welcome to Job Portal'
            # message = f"""Hi {request.data['name']}, thank you for registering in Job Portal ."""
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [request.data['email'], ]
            # send_mail( subject, message, email_from, recipient_list )
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class HrProfileAPI(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

class JobPostAPI(CreateAPIView):
    serializer_class = JobSerializer



class JobViewAPI(ListAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer



class JobEditAPI(RetrieveUpdateAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer


class JobDeleteAPI(GenericAPIView):
    def get_object(self, pk):
        try:
            return Jobs.objects.get(pk=pk)
        except Jobs.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = JobSerializer(user)
        return Response(serializer.data)

    def delete(self,request,pk):
        user = self.get_object(pk)
        user.delete()
        return Response('data deleted sucessfully')
    

class ApplicationHr(ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
# ---------------------------Job-seeker-----------------------------------

class ApplyAPI(CreateAPIView):
    serializer_class = ApplicationSerializer