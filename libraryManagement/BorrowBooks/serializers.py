from .models import borrow_book
from rest_framework import serializers


class borrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = borrow_book
        fields = '__all__'
