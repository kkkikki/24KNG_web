[![CI/CD Pipeline](https://github.com/kkkikki/24KNG_web/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/kkkikki/24KNG_web/actions/workflows/ci-cd.yml)

# 24KNG_web CI/CD pipeline

1. `vod` 폴더에 들어있는 Django 프로젝트 내용물이 git push된다.
2. GitHub Actions의 yml 파일에 따라 아래 작업들이 수행됨:
   - **job1**: `django manage.py test`
   - **job2**: Docker build & push
     - Docker build 시에 `vod` 폴더가 같이 탑재되어 Docker Hub에 푸쉬됨.
     - [링크](https://hub.docker.com/repository/docker/kaseykim7123/24kng_webpages/general)
   - **job3**: Git push argo_repo
     - 해당 Docker 이미지가 Kubernetes 배포를 위한 `deployments.yaml` 파일에 들어감
3. argo_repo에 git push된 yaml 파일로 ArgoCD가 sync되어 EC2에서 컨테이너가 돌아감
4. External IP로 접속 시 해당 Django 페이지 확인 가능
