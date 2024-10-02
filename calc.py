def add (x,y):
    return x+y

def miu(x,y):
    return x-y

def mul (x,y):
    return x*y

def div(x,y):
    return x/y

num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

print(f"두 수의 합: {add(num1,num2)}")
print(f"두 수의 차: {miu(num1,num2)}")
print(f"두 수의 곱: {mul(num1,num2)}")
print(f"두 수의 나눗셈: {div(num1,num2)}")
