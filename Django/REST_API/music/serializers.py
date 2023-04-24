from rest_framework import serializers
from .models import Music, Review


# 문제 1. title 과 release_date 정보만 보이게 MusicListSerializer를 수정하시오.
class MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('title', 'release_date') # title과 release_date만 JSON에 담겨지도록 필드 설정


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'


# 문제 11. 각 음악 정보에 몇 개의 리뷰가 있는지 확인할 수 있도록 review_count 필드를 아래 클래스에 추가하시오. 
# 이 때, review_count 필드는 읽기 전용(read_only)이 되도록 설정합니다.
class MusicReviewCntSerializer(serializers.ModelSerializer):
    review_count = serializers.SerializerMethodField() # 빈 필드 생성
    
    def get_review_count(self, music): 
        review = music.review_set.all() # 음악에서 리뷰 역참조 
        return [{'review_count':len(review)}] # 빈필드에 리뷰의 개수 할당 
    
    class Meta:
        model = Music
        fields = '__all__'
        


# 문제 6. 리뷰 정보와 N:1 관계를 갖고 있는 Music 의 모든 정보를 music 필드에 나타낼 수 있도록 아래 클래스에 추가하시오.
# 이 때, music 필드는 읽기 전용(read_only)이 되도록 설정합니다.
class ReviewSerializer(serializers.ModelSerializer):
    music = MusicSerializer(read_only=True)
    class Meta:
        model = Review
        # fields = ('content', 'created_at', 'updated_at')
        fields = '__all__'
        read_only_fields = ('music',)

