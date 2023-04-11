# image 처리 
Django에는 이미지 처리 방식 2가지가 있음
1. 이미지 축소해서 저장 
2. 원본 서버에 저장 
   
- 사용자가 올린 모든 사진을 서버에 올리면 과부하 올 수 있음  
- 이미지 등들을 매번 서버에서 가져오면 과부하 올 수 있음

따라서, 이미지들을 한번 로드하고 버리는게 아니고 웹브라우저에 저장해 둬서 다시 필요할 때 또 다시 서버에서 가져오는 것을 방지  

`pip install django-imagekit` 
- 이러한 이미지 조작 및 처리에 사용하는 라이브러리 

`pip freeze > requirements.txt ` 
- 외부 라이브러리 추가할 때마다 꼭 신경써서 pip list 업데이트 해주자

## Thumbnail
```python
from imagekit.processors import Thumbnail
from imagekit.models import ImageSpecField

thumbnail_img = ImageSpecField(
    source = 'image', 
    processors = [Thumbnail(200,300)], # 200X300 으로 줄이자 
    format = 'JPEG',
    options = {'quality':80},
)
```
