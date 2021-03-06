#Factory 함수 사용하기
#2제곱, 3제곱, 4제곱을 할 수 있는 Factory 함수를 만들기

def one(n):
    def two(value):
        return value ** n
    # **의 의미는 제곱임
    return two

#return two 를 one 함수에서 하므로 a 는 two 함수의 역할을 할 수 있음
a = one(2)
b = one(3)
c = one(4)
print(a(10))
print(a(10))
print(a(10))