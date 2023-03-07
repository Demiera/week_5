from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from user.serializers import TopicsSerializer

@api_view(['GET'])
def api_home(request, format=None):
    return Response(
        {
            'Login': reverse("token_obtain_pair", request=request, format=format),
            'User Register': reverse("UserRegister", request=request, format=format),
            "Users": reverse("User_Read_API", request=request, format=format),
            f"topics of {request.user.username}": reverse("Read_API", request=request, format=format),
        }
    )