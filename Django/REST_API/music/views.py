from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import MusicListSerializer, MusicSerializer, MusicReviewCntSerializer, ReviewSerializer
from .models import Music, Review


@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        music_all = Music.objects.all()
        serializer = MusicListSerializer(music_all, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 문제 2. MusicSerializer를 이용하여 유효성 검사 후 음악 정보를 생성할 수 있도록 코드를 완성하시오.
    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): # 유효성 검사
            serializer.save() # 데이터 베이스에 저장 

        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def music_detail(request, music_pk):
    # 문제 3. 찾으려는 데이터가 없으면 404 상태 코드를 반환할 수 있도록 아래 코드를 완성하시오.
    try :  # 찾는 데이터가 있으면 
        music = Music.objects.get(pk=music_pk)
        if request.method == 'GET':
            serializer = MusicReviewCntSerializer(music)
            return Response(serializer.data)
        
        # 문제 4. 음악 데이터를 삭제하고 {'delete': 삭제되는음악pk} 형태의 JSON으로 반환하도록 코드를 완성하시오.
        elif request.method == 'DELETE':
            music.delete()
            return Response(data = {'delete':music_pk}) # 음악 정보를 정상적으로 삭제하였다면, key를 ‘delete’, value를 music_pk로 갖는 JSON 데이터를 반환
    
        # 문제 5. 음악 데이터를 수정할 수 있도록 아래 코드를 완성하시오.
        # 수정이 정상적으로 완료되었다면 수정된 데이터를 JSON 형태로 반환합니다.
        elif request.method == 'PUT':
            serializer = MusicSerializer(instance = music, data = request.data) # 기존 데이터 + 요청된 데이터 
            if serializer.is_valid(raise_exception= True): # 유효성 검사 
                serializer.save()
                
            return Response(serializer.data)
    except: # 찾는 데이터가 없으면 
        return Response(status=status.HTTP_404_NOT_FOUND)
        
        


# 문제 7. 모든 리뷰 정보를 반환하도록 review_list 코드를 완성하시오.
@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all() # 모든 리뷰 객체 가져오기 
    serializer = ReviewSerializer(reviews, many = True) # 직렬화 (many=True 로 1개 이상의 리소스 가져오게 하기)
    return Response(serializer.data) 



# 문제 8. 리뷰를 생성할 수 있도록 아래 코드를 완성하시오.
# 유효성 검사를 통과하지 못하면 정보와 400 상태코드를 반환합니다.
# 작성된 리뷰의 JSON과 함께 201 상태 코드를 반환합니다.
@api_view(['POST'])
def review_create(request, music_pk):
    music = Music.objects.get(pk = music_pk)
    serializer = ReviewSerializer(data = request.data)
    if serializer.is_valid(): # 유효성 검사 
        serializer.save(music = music) # music 참조할 수 있도록 
        return Response(serializer.data, status=status.HTTP_201_CREATED) # POST 성공하면 201 상태코드 반환 
    else: 
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST) # 유효성 검사 실패하면 데이터와 함께 400 상태코드 반환
        

    


@api_view(['GET', 'DELETE'])
def review_detail(request, review_pk):
    # 문제 9. 리뷰 정보를 조회할 수 있도록 아래 코드를 완성하시오.
    # 찾는 리뷰가 없으면 404 상태 코드를 반환합니다.
    try : # 찾는 리뷰가 있으면 
        review = Review.objects.get(pk = review_pk)

        if request.method == 'GET':
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
    
                
        
        # 문제 10. DELETE 로 요청오는 경우 해당 리뷰가 삭제될 수 있도록 아래에 코드를 완성하시오.
        # 삭제하려는 리뷰가 없으면 404 상태 코드를 반환합니다.
        # 삭제가 정상적으로 완료되면 {'delete': 삭제된리뷰PK} 형태인 JSON이 204 상태코드와 함께 반환됩니다.
        elif request.method == 'DELETE':
            review.delete()
            return Response(data={'delete':review_pk}, status=status.HTTP_204_NO_CONTENT) # 삭제가 정상적으로 완료되면 {'delete': 삭제된리뷰PK} 형태인 JSON이 204 상태코드와 함께 반환
    
    except : # 찾는 리뷰가 없으면 
        return Response(status=status.HTTP_404_NOT_FOUND) # 리뷰가 없으면 404 상태 코드를 반환
