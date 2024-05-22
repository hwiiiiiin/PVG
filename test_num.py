import random

print()
print("1~10사이의 숫자가 있습니다")
print()

random_num = random.randint(1,10)
user_num = 0
count = 0
while random_num != user_num:
    user_num = int(input("컴퓨터가 뽑은 숫자는 무엇일까요?"))
    count+=1
    if random_num > user_num:
        print("더 큰수 입니다")
    elif random_num < user_num:
        print("더 작은 수 입니다")

    print()
print(f"정답입니다. 컴퓨터가 선택한 숫자는 {random_num}입니다.")
        
    
