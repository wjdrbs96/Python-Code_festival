#정렬이 되어있는지 확인하기
#list끼리 비교할 때 list1 ! = list2 이렇게 비교 가능
a= [1,3,2,4,5];
b=a;

if a!=b.sort():
    print("No")
else:
    print("Yes")