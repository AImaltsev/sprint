from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DatabaseHandler, PerevalAdded
from .serializers import PerevalSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view


class SubmitDataView(APIView):
    def post(self, request, format=None):
        # Получаем данные из запроса
        beauty_title = request.data.get('beauty_title')
        title = request.data.get('title')
        other_titles = request.data.get('other_titles')
        connect = request.data.get('connect')
        add_time = request.data.get('add_time')
        coords_data = request.data.get('coords_data')
        levels = request.data.get('levels')
        raw_data = request.data.get('raw_data')

        # Создаем экземпляр вашего DatabaseHandler
        db_handler = DatabaseHandler()

        # Вызываем метод добавления перевала
        pereval = db_handler.add_pereval(beauty_title, title, other_titles, connect, add_time, coords_data, levels,
                                         raw_data)

        # Сериализуем созданный объект и возвращаем в ответе
        serializer = PerevalSerializer(pereval)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetPerevalByIdView(APIView):
    def get(self, request, id, format=None):
        # Получаем объект PerevalAdded по id
        pereval = DatabaseHandler().get_pereval_by_id(id)

        # Сериализуем объект и возвращаем в ответе
        serializer = PerevalSerializer(pereval)
        return Response(serializer.data)


class EditPerevalView(APIView):
    def patch(self, request, id, format=None):
        # Получаем данные из запроса
        data = request.data

        # Пытаемся отредактировать запись
        db_handler = DatabaseHandler()
        result = db_handler.edit_pereval(id, data)

        if result:
            return Response({"state": 1}, status=status.HTTP_200_OK)
        else:
            return Response({"state": 0, "message": "Не удалось отредактировать запись"}, status=status.HTTP_400_BAD_REQUEST)


class GetUserPerevalsView(APIView):
    def get(self, request, format=None):
        # Получаем email из параметра запроса
        user_email = request.query_params.get('user__email', '')

        # Получаем все записи пользователя с указанным email
        perevals = DatabaseHandler().get_user_perevals(user_email)

        # Сериализуем записи и возвращаем в ответе
        serializer = PerevalSerializer(perevals, many=True)
        return Response(serializer.data)