from .models import Dishes
from rest_framework import serializers

class Dishser(serializers.ModelSerializer):
    class Meta:
        model=Dishes
        fields="__all__"