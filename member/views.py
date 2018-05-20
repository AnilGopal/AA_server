from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Member
from rest_framework import status

class Login(APIView):

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        try:
            username = str(request.data.get('user'))
            pwd = str(request.data.get('password'))
            member = Member.objects.get(name=username)
            if member.password == pwd:
                response = Response({'status':True})
            else:
                response = Response({'status':False, 'msg':"Incorrect Credentials"})
            return response
        except Exception as e:
            return Response({'status':False,'msg':"Incorrect Credentials"})