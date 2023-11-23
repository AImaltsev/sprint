from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Coords, PerevalAdded, DatabaseHandler
from .serializers import PerevalSerializer


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
        pereval = db_handler.add_pereval(beauty_title, title, other_titles, connect, add_time, coords_data, levels, raw_data)

        # Сериализуем созданный объект и возвращаем в ответе
        serializer = PerevalSerializer(pereval)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
