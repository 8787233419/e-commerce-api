from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Member
from .serializers import MemberSerializer

@api_view(['POST'])
def Register(request):
    serializer = MemberSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    else :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Login(request):
    user_id = request.data.get('user_id')
    password = request.data.get('password')

    try:
        member = Member.objects.get(user_id=user_id)
        if member.password == password:
            return Response({'message': 'Successfully logged in'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    except Member.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Logout(request):
    request.session.flush()