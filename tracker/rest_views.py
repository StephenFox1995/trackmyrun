from rest_framework import permissions, generics, authentication, status
from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Activity
from .serializers import ActivitySerializer


class ActivityRetrieveAPI(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ActivitySerializer

    def get_object(self):
        return Activity.objects.get(owner=1)


@api_view(["GET", ])
@permission_classes((permissions.AllowAny,))
def token_login(request):
    if (not request.GET["username"]) or (not request.GET["password"]):
        return Response({"detail": "Please provide username and password"}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=request.GET["username"], password=request.GET["password"])

    if user:
        if user.is_active:
            try:
                my_token = Token.objects.get(user=user)
                return Response({"token": "{}".format(my_token.key)}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({"message": "Could not generate token"})
        else:
            return Response({"detail": "This account is not active."}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"detail": "Incorrect username or password"}, status=status.HTTP_400_BAD_REQUEST)
