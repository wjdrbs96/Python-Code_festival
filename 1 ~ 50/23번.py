# 몸무게 제한이 있는 놀이기구에 몇명까지 탈 수 있는지?
num = int(input("총 무게를 입력"))
cot = int(input("총 인원입력"))
l = []
for i in range(cot):
    a = int(input("몸무게입력"))
    l.append(a)

count = 0;
sum = 0
for j in range(cot):
    sum += l[j]
    if sum > num:
        break;
    count += 1

print(count)

