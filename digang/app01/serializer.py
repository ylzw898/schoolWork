# python manage.py inspectdb > app01/models.py
# 在books文件夹中创建serializer.py文件，并写对应序列化器BooksSerializer：

from rest_framework import serializers

from .models import App01Book
from .models import App01Rent
from .models import App01HousePrice
from .models import App01UserInformation
from .models import App01Check


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = App01Book
        fields = '__all__'


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = App01Rent
        fields = '__all__'


class HousePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = App01HousePrice
        fields = '__all__'


class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = App01UserInformation
        fields = '__all__'


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = App01Check
        fields = '__all__'
