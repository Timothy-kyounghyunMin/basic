import requests

def get_github_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # 예시로 몇 가지 정보만 추출
        user_info = {
            "login": data.get("login"),
            "name": data.get("name"),
            "company": data.get("company"),
            "location": data.get("location"),
            "public_repos": data.get("public_repos"),
            "followers": data.get("followers"),
            "following": data.get("following"),
            "created_at": data.get("created_at"),
            "bio": data.get("bio"),
            "blog": data.get("blog"),
        }
        return user_info
    elif response.status_code == 404:
        return f"사용자 '{username}'를 찾을 수 없습니다."
    else:
        return f"API 요청 중 오류 발생: 상태 코드 {response.status_code}"

# 사용 예시
if __name__ == "__main__":
    username = input("GitHub 사용자명을 입력하세요: ")
    info = get_github_user_info(username)
    print(info)