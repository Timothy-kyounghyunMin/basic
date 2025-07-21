import re

def check_password(password):
    conditions = {
        "소문자": r"[a-z]",
        "대문자": r"[A-Z]",
        "숫자": r"\d",
        "기호": r"[!@#$%^&*(),.?\":{}|<>_\-\[\]\\\/'`~+=;]"
    }

    missing_conditions = []

    for condition_name, pattern in conditions.items():
        if not re.search(pattern, password):
            missing_conditions.append(condition_name)

    if missing_conditions:
        print("비밀번호가 다음 조건을 충족하지 않습니다:")
        for cond in missing_conditions:
            print(f"- 최소 하나 이상의 {cond} 포함")
        return False
    else:
        print("비밀번호가 모든 조건을 충족합니다.")
        return True

if __name__ == "__main__":
    pwd = input("비밀번호를 입력하세요: ")
    check_password(pwd)