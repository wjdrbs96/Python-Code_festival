# count 사용하기
# format 사용법 익히고, count 내장함수 기억하기
l = input("입력").split()
count=0
for i in range(1,len(l)):
    if l.count(l[i-1]) < l.count(l[i]):  # 문제 가장 많이 count 된 사람의 인덱스를 저장
        count = i

print("{}(이)가 총 {}표로 반장이 되었습니다." .format(l[count], l.count(l[count])))