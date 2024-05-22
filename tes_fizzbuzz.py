j=0
for i in range (1,101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
        j+=1
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i) #나머지는 숫자 그 자체 출력
print(f"100까지 FizzBuzz갯수는 {j}개입니다. ")        
