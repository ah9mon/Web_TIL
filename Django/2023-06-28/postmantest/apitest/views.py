from django.http import JsonResponse
import requests
# Create your views here.

KAKAO_API_KEY = ""
KAKAO_BASE_URL = "https://dapi.kakao.com/v2/local/search/keyword?query="
NAVER_CLIENT_ID = ""
NAVER_CLIENT_SECRET = ""
NAVER_BASE_URL = "https://openapi.naver.com/v1/search/local.json?query="

def get_location_data(url, headers):
        response = requests.get(url, headers=headers)
        print(response.json())
        return JsonResponse(response.json())

def kakao_local_map(request):
    if (request.method == "GET"):
        query = request.GET.get("query") #멀티캠퍼스
        print(query)
        headers = {
            "Authorization" : f"KakaoAK {KAKAO_API_KEY}"
        }
        url = f"{KAKAO_BASE_URL}{query}"
        return get_location_data(url, headers)

def naver_local_map(request):
    if (request.method == "GET"):
        query = request.GET.get("query") #멀티캠퍼스
        print(query)
        headers = {
            "X-Naver-Client-Id" : NAVER_CLIENT_ID,
            "X-Naver-Client-Secret" : NAVER_CLIENT_SECRET
        }
        url = f"{NAVER_BASE_URL}{query}"
        return get_location_data(url,headers)