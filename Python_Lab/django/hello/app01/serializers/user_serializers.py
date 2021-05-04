from rest_framework import serializers
from app01.models import User as app01user

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = app01user
        fields = '__all__'
        