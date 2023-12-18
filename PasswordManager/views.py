from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import PasswordGeneratorSerializer
from rest_framework.response import Response

def index(request):
    return render(request, 'index.html')


from .models import PasswordModel
import random

# men
class PasswordLevel1(APIView):
    queryset = PasswordModel.objects.all()
    serializer = PasswordGeneratorSerializer  # Make sure to replace 'your_app_name' with your actual app name

    def get(self, request):
        elements = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
        parolcha = ''
        for i in range(8):
            parolcha += random.choice(elements)

        return Response({'password': parolcha})

#!@#$%%^&&
class PasswordLevel2(APIView):
    queryset = PasswordModel.objects.all()
    serializer = PasswordGeneratorSerializer  # Make sure to replace 'your_app_name' with your actual app name

    def get(self, request):
        elements = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
        parolcha = ''

        for i in range(6):
            parolcha += random.choice(elements)
        for i in range(2):
            parolcha += str(random.randint(0, 9))
        return Response({'password': parolcha})
# alo
class PasswordLevel3(APIView):
    queryset = PasswordModel.objects.all()
    # Make sure to replace 'your_app_name' with your actual app name
    serializer = PasswordGeneratorSerializer

    def get(self, request):
        elements = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
                   '(', ')', '-', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?', '`', '~', '_', '§', '±', '°', '£', '€', '¥', '¢']
        parolcha = []

        for i in range(9):
            parolcha.append(random.choice(elements))
        for i in range(2):
            parolcha.append(str(random.randint(0, 9)))
        for i in range(5):
            parolcha.append(random.choice(symbols))
        random.shuffle(parolcha)
        parolcha1 = ''
        for i in parolcha:
            parolcha1+=i


        return Response({'password': parolcha1})


# Create your views here.
