# Python 3.10 이미지를 기반으로 설정
FROM python:3.10

# Nginx 설치
RUN apt-get update && apt-get install -y nginx

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 의존성 설치
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Python 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일 복사
COPY . .

# SSL 인증서 복사
COPY ./ssl /etc/nginx/ssl

# Nginx 설정 파일 복사
COPY nginx.conf /etc/nginx/nginx.conf

# 정적 파일 수집
RUN python manage.py collectstatic --noinput

# 포트 노출
EXPOSE 80 443

# 서버 실행 (Nginx와 Gunicorn)
CMD service nginx start && gunicorn vod.wsgi:application --bind 0.0.0.0:8000
