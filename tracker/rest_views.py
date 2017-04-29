from rest_framework import permissions, generics, authentication, status
from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Activity
from .serializers import ActivitySerializer


@api_view(["GET", "POST"])
@permission_classes((permissions.IsAuthenticated,))
def activity(request):
    if request.method == "GET":
        activities = Activity.objects.all().order_by("-start")
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        try:
            serializer = ActivitySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(owner_id=request.user.id)
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({"message": "Activity successfully created"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET", ])
@permission_classes((permissions.IsAuthenticated,))
def get_activities_for_user(request, owner_id):
    activities = Activity.objects.filter(owner_id=owner_id).order_by('-start')
    if len(activities) > 0:
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
    else:
        return Response({"message": "No data for that user"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", ])
@permission_classes((permissions.AllowAny,))
def obtain_auth_token(request):
    if (not request.GET["username"]) or (not request.GET["password"]):
        return Response({"message": "Please provide username and password"}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=request.GET["username"], password=request.GET["password"])

    if user:
        if user.is_active:
            try:
                token = Token.objects.get_or_create(user=user)
                return Response({"token": "{}".format(token[0])}, status=status.HTTP_200_OK)
            except Exception:
                return Response({"message": "Could not generate token"})
        else:
            return Response({"message": "This account is not active."}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message": "Incorrect username or password"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST", ])
@permission_classes((permissions.AllowAny,))
def register(request):
    try:
        username = request.data['username']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password = request.data['password']

    except KeyError:  # i.e incorrect details were sent
        return Response({"message": "Please send the correct details"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = get_user_model().objects.get(username=username)
        if user:
            return Response({"message": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)
    except get_user_model().DoesNotExist:
        user = get_user_model().objects.create_user(username=username)
        user.set_password(password)
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return Response({"message": "User successfully added"})
