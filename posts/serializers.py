from rest_framework import serializers

from .models import Message, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        if self.context.get('request', None):
            validated_data['user'] = self.context['request'].user
        if self.context.get('scope', None):
            validated_data['user'] = self.context['scope']['user']
        return super().create(validated_data)


class MessageSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Message
        fields = '__all__'

    def create(self, validated_data):
        if self.context.get('request', None):
            validated_data['user'] = self.context['request'].user
        if self.context.get('scope', None):
            validated_data['user'] = self.context['scope']['user']
        return super().create(validated_data)
