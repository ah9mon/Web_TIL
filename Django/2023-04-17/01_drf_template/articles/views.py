from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article, Comment
from .serializers import ArticleListSerializer, CommentSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST": # GET, POST외에도 많은 HTTPmethod 있으니까 elif로 확실히 나눔 
        serializer = ArticleListSerializer(data = request.data) # 역직렬화
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 직렬화
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 에러가 낫을 때 에러를 담아서 줄지 빈객체를 줄지 클라이언트 개발자랑 협의하는 거임


@api_view(['GET', 'DELETE','PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "GET":
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)
    
    elif request.method == "DELETE": 
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        # 입력 데이터 가져오고 save
        serializer = ArticleListSerializer(article, data = request.data) # 역직렬화
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data) # 직렬화
    

@api_view(['GET'])
def comment_list(request):
    if request.method == "GET":
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def comment_detail(request, comment_pk):
    if request.method == "GET":
        comments = Comment.objects.get(pk = comment_pk)
        print(comments)
        serializer = CommentSerializer(comments)
        return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    serializer = CommentSerializer(data = request.data) # article 없어서 아래 if문 통과 못함 따라서 article은 무시하도록 해야함 -> read_only_fields
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)