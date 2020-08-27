from rest_framework import serializers
from .models import Query

class query_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Query
        fields = '__all__'
