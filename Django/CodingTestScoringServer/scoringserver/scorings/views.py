import logging
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Testcase, Usercode
from .serializers import UsercodeSerializer
from rest_framework.decorators import api_view
from django.contrib.sessions.backends.db import SessionStore
import subprocess

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@api_view(['POST'])
def get_user_code(request):
    if request.method == "POST":
        user_id = request.POST.get("User ID")
        user_code = request.POST.get("Source Code")
        problem_number = request.POST.get("Problem Number")
        
        data = {
            "problem_number": problem_number,
            "user_id": user_id,
            "user_code": user_code
        }

        # 유저 코드 저장
        serializer = UsercodeSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            existed_code = Usercode.objects.filter(user_id=user_id, problem_number=problem_number)
            if existed_code:
                logger.info('기존 코드 삭제')
                existed_code.delete()

            serializer.save()

        # 채점을 위한 리다이렉트
        url = "http://127.0.0.1:8000/codingtest/scorings"
        
        # 세션에 데이터 저장
        session = SessionStore(request.COOKIES.get('sessionid'))
        session['user_id'] = user_id
        session['user_code'] = user_code
        session['problem_number'] = problem_number
        session.save()

        # 채점을 위한 리다이렉트
        url = "http://127.0.0.1:8000/codingtest/scorings"
        response = redirect(url)

        # 세션 쿠키를 응답에 추가
        response.set_cookie('sessionid', session.session_key)

        return response

def score_user_code(request):
    # 세션에서 데이터 가져오기
    session = SessionStore(request.COOKIES.get('sessionid'))
    user_id = session.get('user_id')
    user_code = session.get('user_code')
    problem_number = session.get('problem_number')
    testcases = Testcase.objects.filter(problem_number=problem_number)

    # 테스트케이스에 대한 유저 코드 검사
    testcase_number = 0
    response_data = {}
    for testcase in testcases:
        testcase_number += 1

        test_input = testcase.test_input 
        test_output = testcase.test_output

        # 유저 코드 실행
        result = subprocess.run(['python', '-c', user_code], input=test_input, capture_output=True, text=True)

        stdout = result.stdout.rstrip()
        stderr = result.stderr

        logger.info("결과: %s", stdout)
        logger.info("에러: %s", stderr)

        data = {}
        if stderr:  # 에러 발생 시
            data['error'] = stderr
            
        else:
            if stdout == test_output:
                data['result'] = "성공"
            else:
                data['result'] = "실패"
        
        response_data[f'{testcase_number}'] = data

    # 결과와 에러를 JSON 형식으로 반환
    return JsonResponse(response_data)
