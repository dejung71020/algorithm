'''
문제 설명
2자리 이상의 정수 number가 주어집니다. 주어진 코드는 이 수를 2자리씩 자른 뒤, 자른 수를 모두 더해서 그 합을 출력하는 코드입니다. 코드가 올바르게 작동하도록 한 줄을 수정해 주세요.

제한사항
10 ≤ number ≤ 2,000,000,000
number의 자릿수는 2의 배수입니다.
입출력 예
입력 #1

4859
출력 #1

107
입력 #2

29
출력 #2

29
입출력 예 설명
입출력 예 #1

입력된 수를 2자리씩 나눠 합치면 다음과 같습니다.
48 + 59 = 107
입출력 예 #2

입력된 수를 2자리씩 나눠 합치면 다음과 같습니다.
29  = 29

디버깅 문제입니다. 아래 코드를 수정하면 되는 문제에요.

number = int(input())

answer = 0

for i in range(1):
    answer += number % 100
    number //= 100

print(answer)
'''
# 대중의 첫 생각
number = input()

answer = 0

for i in range(0, len(number), 2):
    answer += int(number[i:i+2])

print(answer)

# 문제는 한 줄만 수정하는 것이 목표 (재풀이)
number = int(input()) # 아 제발 좀 뜨지 말라고 시발아

answer = 0

for i in range(0, len(str(number)), 2):
    answer += number % 100
    number //= 100

print(answer)

'''
다른 사람들의 풀이를 보고 배웠습니다.

for i in range(5):
너무 사기다.

for i in range(len(str(number))//2):
몫 만큼만 반복한다.

while number > 0:
가장 쉬우면서 직관적이다.

while number:
위랑 같은 거

for i in range(1, int(number**0.5)):
1부터 제곱근까지 반복한다. 이거는 수학 잘해야 될 것 같다.
'''