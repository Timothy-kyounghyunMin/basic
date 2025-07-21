# 사용자 입력을 계속 받아서 출력하다가, !quit을 입력하면 종료하는 프로그램

while True:
    user_input = input("아무 내용이나 입력하세요 ('!quit' 입력 시 종료): ")
    if user_input.strip() == '!quit':
        print("프로그램을 종료합니다.")
        break
    print(f"입력한 내용: {user_input}")