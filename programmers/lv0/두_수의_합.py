# https://school.programmers.co.kr/learn/courses/30/lessons/181846?language=python3#

'''
문제 : 0 이상의 두 정수가 문자열 a, b로 주어질 때, a + b의 값을 문자열로 return 하는 solution 함수를 작성해 주세요.

제한 사항 : 
1 ≤ a의 길이 ≤ 100,000
1 ≤ b의 길이 ≤ 100,000
a와 b는 숫자로만 이루어져 있습니다.
a와 b는 정수 0이 아니라면 0으로 시작하지 않습니다.

입출력 예 : 
a	b	result
"582"	"734"	"1316"
"18446744073709551615"	"287346502836570928366"	"305793246910280479981"
"0"	"0"	"0"
'''

# 직접 구현
def solution(a, b):
    answer = str(int(a) + int(b))
    return answer

# 정답
import sys
# 최대 자릿수 제한을 100,000 이상으로 넉넉하게 설정
sys.set_int_max_str_digits(1000000) 

def solution(a, b):
    answer = str(int(a) + int(b))
    return answer

'''
여기서 포인트는 다른 언어에서는 큰 수를 다룰 기본 자료형이 없어서 문자열을 뒤에서부터 한자리씩 직접 더해서 올림을 처리하는 알고리즘 구현 문제라고 한다.

그러나 파이썬은 int() 사용시 최대 4300자리까지 가능하고, 자릿수를 무한대로 세팅할 수 있다.
따라서 자릿수 세팅 후 int() 변환으로 해결할 수 있다.
'''

