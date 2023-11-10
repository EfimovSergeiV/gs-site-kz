# Определение местоположения пользователя по ip адресу
# pip install geoip2
# mkdir geoip-db
# Upload database 'GeoLite2 City' from (https://www.maxmind.com/en/accounts/639907/geoip/downloads) to geoip-db dir

import json, requests, random

from django.contrib.auth.models import User
from django.http import response
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from serializers.main import *

from main.verification import *
from main.models import UserIdentificationServiceModel
from main.settings import BASE_DIR

from ipware import get_client_ip
import geoip2.database



class MainPageView(APIView):
    """ Главная страница API """

    def get(self, request):
        html = "<html><body><h1>Скоро тут будет интернет-магазин</h1></body></html>"
        return HttpResponse(html)


class AuthTokenView(ObtainAuthToken):
    """Отдаём токен и информацию о пользователе"""
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'userid': user.pk,
            'user': user.username,
            'email': user.email,
            })
    

class LogoutView(APIView):
    def post(self, request):
        return Response(status=status.HTTP_200_OK)


class SignUpView(APIView):
    """ Стандартная регистрация пользователей """
    
    def post(self, request, format=None):
        serializer_user = UserSerializer(data=request.data)
        
        check_email = User.objects.filter(email=request.data['email']).exists()

        if serializer_user.is_valid() and not check_email:
            user = User.objects.create(
                username= serializer_user.initial_data['username'],
                first_name = serializer_user.initial_data['first_name'],
                last_name = serializer_user.initial_data['last_name'],
                email= serializer_user.initial_data['email'],
            )
            user.set_password(serializer_user.initial_data['password'])
            user.save()
            # mail_list = [
            #     serializer_user.data['email'],
            #     ]
            # SugnUpMails.send_notice(email=mail_list, data=serializer_user.data)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# class SubscriebeUserView(APIView):
#     """ Быстрая регистрация пользователей """
    
#     def post(self, request):        
#         try:
#             email = request.data["email"]
#             check_email = User.objects.filter(email=email).exists()

#             if check_email:
#                 return Response(status=status.HTTP_400_BAD_REQUEST)

#             else:
#                 gen_pass = random.randrange(00000000, 19999999)
#                 html_content = render_to_string('subscriebe.html', {'gen_pass': gen_pass})
                
#                 serializer = UserSerializer(
#                     data = { "username": email, "email": email, "password": gen_pass }
#                 )

#                 if serializer.is_valid():
#                     user = User.objects.create(
#                         username= serializer.data['username'],
#                         email= serializer.data['email'],
#                     )
#                     user.set_password(serializer.data['password'])
#                     user.save()

#                     send_mail(
#                         'Благодарим за регистрацию на нашем сайте',
#                         message=html_content,
#                         from_email= 'shop@glsvar.ru',
#                         recipient_list= [email],
#                         fail_silently=False,
#                         html_message=html_content
#                         )
#                     print("Создан новый пользователь")
#                 else:
#                     print("Serializer not valid")


                
#                 return Response(status=status.HTTP_201_CREATED)

#         except KeyError:
#             return Response(status=status.HTTP_400_BAD_REQUEST)


class ChangeUserView(APIView):
    """ Изменить информацию о пользователе """

    pass

    # permission_classes = [IsAuthenticated,]

    # def post(self, request):
    #     user = request.user.username
    #     print(user)
        
    #     return Response(status=status.HTTP_201_CREATED)


class RestoreUserPassword(APIView):
    """ Восстановить пароль пользователя """

    def post(self, request):
        """
        TASK: Добавить предварительное уведомление перед сменой пароля
        пользователю
        """
        try:
            email = request.data["email"]
            check_email = User.objects.filter(email=email).exists()
            if check_email:
                gen_pass = random.randrange(00000000, 19999999)    

                try:
                    user = User.objects.get(email=email)
                    user.set_password(str(gen_pass))
                    user.save()
                    html_content = render_to_string('restore-pass.html', {'gen_pass': gen_pass})
                    send_mail(
                        'Сброс пароля пользователя',
                        message=html_content,
                        from_email= 'shop@glsvar.ru',
                        recipient_list= [email],
                        fail_silently=False,
                        html_message=html_content
                        )
                
                except:
                    pass

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)   #({ "error": 'UserNotFound'})

            return Response(status=status.HTTP_200_OK)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    """ Информация о пользователе """

    permission_classes = [IsAuthenticated,]

    def get(self, request):
        user = request.user
        profile = User.objects.get(username=user)

        try:
            prof_custom = ProfileModel.objects.get(user=user)
        except:
            prof_custom = { "phone": None, "adress": None}

        username = profile.username if profile.username else 'не указано'
        first_name = profile.first_name if profile.first_name else 'не указано'
        last_name = profile.last_name if profile.last_name else 'не указано'
        email = profile.email if profile.email else 'не указано'

        try:
            phone = prof_custom.phone if prof_custom.phone else 'не указано'
            adress = prof_custom.adress if prof_custom.adress else 'не указано'
        except:
            phone = 'не указано'
            adress = 'не указано'


        return Response(
            {
                "username" : username,
                "first_name" : first_name,
                "last_name" : last_name,
                "email" : email,
                "phone" : phone,
                "adress" : adress,
            }
        )
    
    def post(self, request):
        resp = { "msg": "Данные сохранены", "variant": "success" }
        user = request.user

        user_data = {}
        prof_data = {}

        for item in request.data:
            if item in ['phone', 'adress',]:
                if request.data[item] != None and len(request.data[item]) > 3:
                    prof_data[item] = request.data[item]
            if item in ['username', 'first_name', 'last_name', 'email']:
                if request.data[item] != None and len(request.data[item]) > 3:
                    user_data[item] = request.data[item]

        try:
            # Update user profile
            ProfileModel.objects.get(user=user)
            ProfileModel.objects.filter(user=user).update(**prof_data)

        except ProfileModel.DoesNotExist:
            # Create user profile
            ProfileModel.objects.create(user=user, **prof_data)

        User.objects.filter(username=user).update(**user_data)


        # print(
        #     'UserData: ', user_data, '\n',
        #     'ProfData: ', prof_data,
        #     )

        try:
            password = request.data["password"]
            if len(password) == 0:
                pass
            elif 20 > len(password) > 8:
                user = User.objects.get(username=user.username)
                user.set_password(password)
                user.save()
            else:
                resp = { "msg": "Слишком короткий пароль", "variant": "danger" }
        except KeyError:
            pass

        return Response(resp)


class LocationFromIPView(APIView):
    """ Определение местоположения пользователя по IP """
    
    def get(self, request):
        client_ip = get_client_ip(request)[0]

        with geoip2.database.Reader('main/geoip-db/GeoLite2-City.mmdb') as reader:
            city = 'Рудный'
            try: 
                response = reader.city(client_ip)
                city = response.city.names.get('ru')

                if city is None:
                    city = response.city.names.get('en')
            
            except geoip2.errors.AddressNotFoundError:
                pass

        return Response(city)



from geopy.geocoders import Nominatim
# from random import randint        # FOR TESTS
class LocationFromCoordinateView(APIView):
    """ Обработка координат браузера и определение населённого пунка пользователя """

    def post(self, request):
        geolocator = Nominatim(user_agent="MainWelderKZ")

        # random_locations = [
        #     {'lat': 52.532217, 'long': 62.480951},
        #     {'lat': 51.101132, 'long': 71.436903},
        #     {'lat': 49.782178, 'long': 73.092549},
        #     {'lat': 48.316274, 'long': 74.979561},
        #     {'lat': 50.795532, 'long': 75.708293},

        #     {'lat': 52.470917, 'long': 37.446319},
        #     {'lat': 57.200711, 'long': 31.893509},
        #     {'lat': 57.231756, 'long': 25.845449},
        #     {'lat': 52.462501, 'long': 16.657015},
        #     {'lat': 50.180667, 'long': 65.193575},
        # ]

        location = geolocator.reverse(
            f"{str(request.data['lat'])},{str(request.data['long'])}",
            # f"{str(random_locations[randint(0, 7)]['lat'])},{str(random_locations[randint(0, 7)]['long'])}",
            exactly_one=True, 
            addressdetails=True,
            language="ru"
        )

        # Возвращает необходимый список названий из полученной локации
        full_addr = list(filter(lambda x: x is not None,[
            location.raw['address'].get(item) for item in [
                'town', 'village', 'city', 'suburb', 'county', 'state', 'country'
            ] 
        ]))

        # print(full_addr)

        return Response(full_addr)