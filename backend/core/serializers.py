from rest_framework.serializers import ModelSerializer
from .models import Car


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        # fields = ["vendor", "model", "year", "volume "] 
        fields = "__all__"