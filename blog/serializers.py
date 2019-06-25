from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    """Serialize article model to json """
    class Meta:
        model = Article
        fields = '__all__'

