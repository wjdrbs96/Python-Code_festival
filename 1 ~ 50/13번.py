# 대문자만 통과시키기
# ord 함수는 숫자로 변환 시켜줌, 아스키 코드 참고하기
str1 = input()
if ord(str1) >= 65 and ord(str1) <= 90:
    print("Yes")
else:
    print("No")

