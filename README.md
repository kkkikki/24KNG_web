# 24KNG_web CI/CD pipeline
1. vod 폴더에 들어있는 django 프로젝트 내용물이 git push된다.
2. github actions 의 yml파일에 따라 아래 작업들이 수행됨.
 job1: django manage.py test
 job2: docker build & push
  - docker build 시에 위의 vod 폴더가 같이 탑재되어 도커 허브에 푸쉬됨.
  - 링크: https://hub.docker.com/repository/docker/kaseykim7123/24kng_webpages/general
 job3: git push argo_repo
  - 해당 도커 이미지가 kubernetes 배포를 위한 deployments.yaml파일에 들어감
3. argo_repo에 git push 된 yaml파일로 argocd sync되어 EC2에 container 돌아감
4. external IP로 접속 시 해당 장고페이지 확인가능