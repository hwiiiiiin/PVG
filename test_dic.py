#영어사전 만들기- 리스트 이용

banner = """
┏━━━┓╋╋╋┏┓
┗┓┏┓┃╋╋┏┛┗┓
╋┃┃┃┣┳━┻┓┏╋┳━━┳━┓┏━━┳━┳┓╋┏┓
╋┃┃┃┣┫┏━┫┃┣┫┏┓┃┏┓┫┏┓┃┏┫┃╋┃┃
┏┛┗┛┃┃┗━┫┗┫┃┗┛┃┃┃┃┏┓┃┃┃┗━┛┃
┗━━━┻┻━━┻━┻┻━━┻┛┗┻┛┗┻┛┗━┓┏┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏━┛┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗━━┛
"""
print(banner)
print("나만의 영어사전 만들기")
print("="*35)

voca = ["apple:사과", "book:책", "desk:책상"]

user = 0 # while에서 사용

while user != "4":
#    for i in voca:
#        print(f"{i}")
    print("""
    ===== 사전 수정 모드 =====

    1. 등록된 단어 보기
    2. 단어 추가 하기
    3. 단어 삭제 하기
    4. 사전 수정 모드 종료 하기
    ====================""")
    user = input("숫자만 입력 하세요>>>  ")

    if user == "1":
        print()
        print("=== 등록 된 단어 ===")
        for i in voca:
            print(f"{i}")
    elif user == "2":
        
        new_voca = input("단어와 뜻을 입력 하세요. ex) 단어:뜻 >>>  ")
        voca.append(new_voca)
        for i in voca:
            print(f"{i}")
    elif user == "3":
        try:
            new_voca = input("삭제할 단어를 입력 하세요. ex) 단어:뜻 >>>  ")
        
            voca.remove(new_voca)
            for i in voca:
                print(f"{i}")
            break  
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
