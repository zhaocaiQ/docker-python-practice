import os

app_env = os.getenv("APP_ENV", "local")

print("안녕하세요! Docker 안에서 실행 중입니다.")
print(f"현재 실행 환경 : {app_env}")