from django.db.models import Q

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.contrib.auth.models import User

from home.models import Appointment




@api_view(['GET', 'POST'])
def bookAppointment(request):
   name = request.data['name']
   contact = request.data['contact']
   feel = request.data['feel']
   print(name, contact, feel)

   if request.method == "POST":
      appointment1 = Appointment.objects.create(
         name = name,
         contact = contact,
         feel = feel
      )
      print(appointment1)
   
   return Response([])