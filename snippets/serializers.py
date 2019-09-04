from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Snippet 
		fields = ['id','title', 'code', 'linenos','language','style']
		

	def create(self, validated_data):
		return Snippet.objects.create(**validated_data)


	def update(self, instance, validated_data):

		instance.tiltle = validated_data.get('title', instance.tiltle)
		instance.code  = validated_data.get('code', instance.code)
		instance.linenos = validated_data.get('linenos', instance.linenos)
		instance.language = validated_data.get('language', instance.language)
		instance.style = validated_data.get('style',  instance.style)
		instance.save()
		return instance
	
		