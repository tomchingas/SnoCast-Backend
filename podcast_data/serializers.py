from rest_framework import serializers
from .models import Avalanche_Accident

class Avalanche_AccidentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'Name',
            'Date',
            'State',
            'Lat',
            'Long',
            'pub_date',
        )
        model = Avalanche_Accident