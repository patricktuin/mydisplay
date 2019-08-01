from rest_framework.authentication import BasicAuthentication

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from displays.permissions import IsOwner
from rest_framework.response import Response

from django.db import IntegrityError
from rest_framework.views import APIView

from displays.models import Line, Display, MyDisplayModel
from displays.serializers import DisplaySerializer

app_name = 'displays'

from displays.models import Display


class DisplayDetailAPIView(APIView):
    authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated, IsAdminUser,)

    def get(self, request, serial_number):
        display_obj = Display.objects.get(serial_number=serial_number)
        line_obj = Line.objects.filter(display__serial_number=serial_number)
        json = dict()
        json["display_properties"] = {"font_size": display_obj.font_size}
        for item in line_obj:
            json[item.line] = {
                "topic": item.topic.topic.lower(),
                "user_text": item.user_text
            }
        return Response(json)

    def post(self, request):
        serializer = DisplaySerializer(data=request.data)
        try:
            if serializer.is_valid():
                display = Display.objects.create(
                    serial_number=serializer.data['serial_number'],
                    model=MyDisplayModel.objects.get(pk=serializer.data['display_model'])
                )
            else:
                return Response({"error": "Provided data is invalid"})
        except IntegrityError:
            return Response({"error": "Serial already exists"})
        return Response({"Created display with serial number": display.serial_number})
