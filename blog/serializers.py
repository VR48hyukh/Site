from rest_framework import serializers
from .models import Post, Comment, Recipe

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

class CommentSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('name', instance.content)
        instance.created = validated_data.get('message', instance.created)
        return instance