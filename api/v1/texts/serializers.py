from rest_framework import serializers
from texts.models import Tag,TextSnippet
from django.urls import reverse

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = (
            'pk',
            'tag',
        )

class TextSnippetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TextSnippet
        fields = (
            'pk',
            'title',
            'description',
            'timestamp'

        )

    def to_representation(self, instance):
        request = self.context.get('request')

        data = super().to_representation(instance)
        data['creator'] = str(instance.creator)
        data['absolute_url'] = request.build_absolute_uri(reverse('api_v1_texts:text_snippet',kwargs={"pk":instance.pk}))
        data['tag'] = str(instance.tag)

        return data
