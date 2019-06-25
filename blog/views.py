from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
import re


class ArticleList(APIView):
    """ List all articles or create a new one """
    
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
        

class ArticleManageView(APIView):
    """Editing articles class """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """Adding new article """
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            obj = Article(**serializer.validated_data)
            obj.save()
            print(obj)
            return Response(serializer.validated_data)
        else:
            
            return Response(serializer.errors)

    def put(self, request ):
        """Update an article data """
        try:
            serializer = ArticleSerializer(data=request.data)
        except:
            Response({"message": 'error while parsing request data', "error": True})

        if serializer.is_valid():   
            validated_data = serializer.validated_data
            article = get_object_or_404(Article, pk=request.data['id'])
            article.title = validated_data.get('title')
            article.content = validated_data.get('content')
            article.author = validated_data.get('author')
            article.save()

            return Response(serializer.validated_data)
        else:
            return Response({"message":serializer.errors, "error" : True})
            

        

    def delete(self, request):
        """Delete an article """
        try:
            pk = request.GET.get('pk')
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


        article.delete()
        return Response(data="Deleted",status=status.HTTP_204_NO_CONTENT)



class ArticleSearch(APIView):
    """Return articles that had the same text in filters """

    def post(self, request):
        """Return Articles from Article table that had the same title 
                or content as filters """

        try: 
            text = str(request.data['text'])
        except:
            return Response({'message': "Your request must contains a text key", 'error': True})   

        pattern = re.compile("^[A-z|0-9]+$")
        
        if text.strip() == '':
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data)
            

        if pattern.match(text):
            articles = Article.objects.filter( Q(title__contains=text) | Q(content__contains=text))
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "Filtering text is not accepted", 'error':True})
        