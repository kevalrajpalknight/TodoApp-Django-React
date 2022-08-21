from rest_framework.serializers import ModelSerializer
from .models import Task

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    