from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note, Customer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ["id","username", "password"]
        extra_kwargs = {"password": {"write_only": True}}
        
    def create(self,validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        customer = Customer.objects.create(user=user)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}