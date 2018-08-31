# from rest_framework import serializers
#
# from snippets.models import Snippet, LANGUAGE_CHOICES
#
#
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#
#     def create(self, validated_data):
#         '''
#         根据提供的验证过的数据创建并返回一个新的 `Snippet` 实例。
#         '''
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         '''
#         根据提供的验证过的数据更新和返回一个已经存在的 `Snippet` 实例。
#         '''
#         instance.title = validated_data.get('title', instance.title) # instance.title 为默认值
#         instance.code = validated_data.get('code', instance.code)
#         instance.language = validated_data.get('language', instance.language)
#         instance.save()
#         return instance







from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'language', 'owner')

