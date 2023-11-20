from rest_framework.views import APIView
# from rest_framework.generics import ListAPIView
# from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from dj_rest_auth.registration.views import SocialLoginView
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings
from main.agent import send_alert_to_agent

from user import serializers
from user.models import *
from django.shortcuts import render


""" Редактирование статуса сообщений пользователей """
def edit_message_status(request, uuid):
    qs = FeedBackModel.objects.filter(uuid=uuid)
    
    try:
        if len(qs) == 1 and request.headers['Cookie']:
            if qs[0].completed:
                post = f"Вопрос клиента { qs[0].person } кто-то уже взял на себя"
            else:
                qs.update(completed=True)
                post = f"Вопрос клиента { qs[0].person } помечен как закрытый"
                send_alert_to_agent(oth_status = { "client": qs[0].person })
        else:
            post = "Вопрос не найден в системе"

        return render(request, 'questionclosed.html', { 'post': post })
    except:
        post = "Вы не прошли проверку на работа"
        return render(request, 'questionclosed.html', { 'post': post })


class UserTestView(APIView):
    """ Пользователь """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response('SUCCESS')


class UserInfoView(APIView):
    """ Информация о пользователе """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user.username
        return Response(user)


class SubscriberView(APIView):
    """ Подписаться на новости """

    def get(self, request):
        qs = SubscriberModel.objects.get(id=1)
        sr = serializers.SubscriberSerializer(qs)
        return Response(sr.data)

    def post(self, request):
        sr = serializers.SubscriberSerializer(data=request.data)
        exist = SubscriberModel.objects.filter(email=request.data['email']).exists()
        if exist:
            return Response({"success": "Пользователь подписан"})
        else:
            if sr.is_valid():
                sr.save()
                # return Response({"exist": "Пользователь существует"})
                return Response({"success": "Пользователь подписан"})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)



# class GoogleLoginView(SocialLoginView):
#     authentication_classes = [] # disable authentication
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = "http://localhost:3000/login"
#     client_class = OAuth2Client


class LikeProdView(APIView):
    """ Избранные товары пользователя """

    permission_classes = [permissions.IsAuthenticated, ]
    sr_like = serializers.LikesProductsSR
    sr_like_detail = serializers.LikeProductDetailSR

    def action(self, request, format=None):

        request.data['user'] = request.user.id
        serializer = self.sr_like(data=request.data)
        liked_product = LikeProdModel.objects.filter(
            user=request.user.id, product=request.data['product']
        )

        if not liked_product and serializer.is_valid():
            serializer.save()
            return status.HTTP_201_CREATED
        if liked_product and serializer.is_valid():
            liked_product.delete()
            return status.HTTP_200_OK
        return status.HTTP_400_BAD_REQUEST

    def get(self, request):
        like_prod = LikeProdModel.objects.filter(user=request.user.id)
        sr = self.sr_like_detail(like_prod, many=True, context={'request':request})
        return Response(sr.data)

    def post(self, request,):
        return Response(
            status=self.action(request)
        )

    def delete(self, request,):
        return Response(
            status=self.action(request)
        )


class ProductReviewView(APIView):
    """ Отзывы клиентов о товарах """
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        prod_id = self.request.query_params.get('prod_id')
        try:
            reviews = ProductReviewModel.objects.filter(visible=True, product=int(prod_id))
        except ValueError and TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = serializers.ProductReviewSR(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        # request.data['user'] = request.user.id   Подставлять имя из базы юзеров, если пользователь авторизован
        serializer = serializers.MainProductReviewSR(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class FeedbackView(APIView):
    """ Обратная связь с общей формы сообщений """

    def post(self, request):
        
        resp = { "success": "Спасибо за Ваше сообщение! Мы свяжемся с Вами в ближайшее время!" }
        serializer = serializers.FeedBackSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            send_alert_to_agent(message=serializer.data)
        else:
            resp = { "danger": "Что то пошло не так( Попробуте позже." }

        return Response(resp)
    
from user.serializers import UserWatcherSerializer

"""
    def preserved(self, prods):
        return Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(prods)])

    def parse_prods(self, instance):
        products = instance.prods
        qs_prods = ProductModel.objects.filter(id__in = products["viewed"] + products["like"] + products["comp"])
        
        data = render_to_string('admin_prods.html', {
            "viewed": qs_prods.filter(id__in = products["viewed"]).order_by(self.preserved(products["viewed"])),
            "like": qs_prods.filter(id__in = products["like"]).order_by(self.preserved(products["like"])),
            "comp": qs_prods.filter(id__in = products["comp"]).order_by(self.preserved(products["comp"])),
"""
class UserWatcherView(APIView):
    """ Пользовательская статистика """

    def get(self, request):
        """ Возвращаем историю последних просмотров товаров """

        if request.headers.get('Authorization'):
            tmp_qs = UserWatcherModel.objects.filter(tmp_id=request.headers.get('Authorization'))[0]
            tmp_data = tmp_qs.prods
            prods_qs = ProductModel.objects.filter(id__in = tmp_data["viewed"] + tmp_data["like"] + tmp_data["comp"])

            sr = UserWatcherSerializer(
                {
                    "viewed": prods_qs.filter(id__in = tmp_data["viewed"]) , 
                    "like": prods_qs.filter(id__in = tmp_data["like"]), 
                    "comp": prods_qs.filter(id__in = tmp_data["comp"])
                },
                context = { 'request':request }
            )

            return Response(sr.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

    def post(self, request):
        """ Обновляем информацию о просмотренных товарах """

        if request.headers.get('Authorization'):
            qs = UserWatcherModel.objects.filter(tmp_id=request.headers.get('Authorization'))
            
            for key in request.data.keys():
                current_data = qs[0].prods
                current_data[key] = [request.data.get(key),] + current_data[key][0:7] if request.data.get(key) not in current_data[key] else current_data[key]
                qs.update(prods=current_data)

        return Response(status=status.HTTP_201_CREATED)
    

    def delete(self, request):
        if request.headers.get('Authorization'):
            qs = UserWatcherModel.objects.filter(tmp_id=request.headers.get('Authorization'))
            for key in request.data.keys():
                current_data = qs[0].prods
                try:
                    current_data[key].remove(request.data.get(key))
                    qs.update(prods=current_data)
                except ValueError:
                    pass

        return Response(status=status.HTTP_200_OK)


    def put(self, request):
        """ Получаем новый или обновляем временнный идентификатор """

        if request.data.get('tmp_id'):
            tmp_exist = UserWatcherModel.objects.filter(tmp_id=request.data.get('tmp_id')).exists()
            if tmp_exist == False:
                qs = UserWatcherModel.objects.create()
                return Response({ "tmp_id": qs.tmp_id })
            else:
                return Response(status=status.HTTP_200_OK)
        else:
            qs = UserWatcherModel.objects.create()
            return Response({ 'tmp_id': qs.tmp_id })
        

from rest_framework.permissions import IsAuthenticated
class UserSessionView(APIView):
    """ При авторизации пользователя возвращает данные сессии или привязывает к текущей """
    
    permission_classes = [IsAuthenticated,]
    
    def post(self, request):
        user = request.user
        print(request.data.get('tmp_id'))
        profile = User.objects.get(username=user)
        
        print(profile.user_profile.latest_session)
        
        if profile.user_profile.latest_session == None:
            profile = ProfileModel.objects.filter(user=profile).update(latest_session = request.data.get('tmp_id'))

        """
        
        Продумать логику ещё раз
        
        """


        return Response(status=status.HTTP_200_OK)
