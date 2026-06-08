'''
문제 설명
나이를 세는 방법은 여러 가지가 있습니다. 그중 한국식 나이는 태어난 순간 1살이 되며 해가 바뀔 때마다 1살씩 더 먹게 됩니다. 연 나이는 태어난 순간 0살이며 해가 바뀔 때마다 1살씩 더 먹게 됩니다. 각각 나이의 계산법은 다음과 같습니다.

한국식 나이 : 현재 연도 - 출생 연도 + 1
연 나이 : 현재 연도 - 출생 연도

출생 연도를 나타내는 정수 year와 구하려는 나이의 종류를 나타내는 문자열 age_type이 주어질 때 2030년에 몇 살인지 출력하도록 빈칸을 채워 코드를 완성해 주세요. age_type이 "Korea"라면 한국식 나이를, "Year"라면 연 나이를 출력합니다.

제한사항
1950 ≤ year ≤ 2030
age_type은 "Korea" 또는 "Year"만 주어집니다.
입출력 예
입력 #1

2000
Korea
출력 #1

31
입력 #2

1999
Year
출력 #2

31
입출력 예 설명
입출력 예 #1

2030년에 2000년생의 한국식 나이는 2030 - 2000 + 1 = 31살입니다.
입출력 예 #2

2030년에 1999년생의 연 나이는 2030 - 1999 = 31살입니다.

빈칸 채우기 문제입니다.

year = int(input())
age_type = input()

if age_type == :
    answer = 

elif age_type == "Year":
    

'''
year = int(input())
age_type = input()

if age_type ==  "Korea":
    answer = 2030 - year + 1

elif age_type == "Year":
    answer = 2030 - year

'''
여기서 포인트는 현재 연도를 어떤 함수로 나타낼 것이냐 이다.
근데 함수가 기억나지 않는다.
근데 문제에서 2030년에 몇 살인지 출력하는 문제였다.
이전 WorkB 프로젝트에서 now_kst() 라는 함수를 만들어 현재 시간대를 가져오고 timedelta(year=4) 를 더 해도 되지 않을까 생각한다.
찾아보니 datetime.now().year + relativedelta(years=4)를 해야 한다고 한다.
timedelta는 hour, minutes, seconds 등이 있다.
'''
