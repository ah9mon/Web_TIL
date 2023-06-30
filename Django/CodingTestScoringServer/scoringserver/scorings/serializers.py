from rest_framework import serializers
from .models import Usercode

class UsercodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usercode
        fields = "__all__"