# SNS new_create.com 

### 📜 [New Create 노션 페이지](https://wool-cobalt-585.notion.site/SNS-new_create-com-84e9627ace194465ada3639f8c25d9bb) 

## 목차

1. [서비스 개요](#✅-서비스-개요)

## ✅ 서비스 개요
  - 예술가(藝術家), 아티스트(Artist)의 혼을 가진 모든 사람이 자신이 new create 한 창작물, 발견 등을 공유하고 소통하는 SNS(Social Networking Service) 서비스입니다.
  - 전문성을 떠나 일상적인 생활속의 작은 창작물, 발견을 공유할 수 있습니다.
  - 자신이 만든 소중한 가치를 세상에 공유하고 싶다면 new create 하세요✨


🚥 개발기간 : 2022.07.20 ~ 2022.07.26 (7일)

🚥 업데이트 날짜 : 

<details>
<summary>서비스 기능 소개</summary> <br>
<div markdown="1">
🗣 <b>New Create 서비스</b>에서는 다음과 같은 기능이 구현되어있습니다. <br>

1. 회원가입, 로그인, 로그아웃 / <b> JWT 토큰 인증, 인가 </b>
 
2. 사용자 CRUD
 
3. 게시글 CRUD / <b> 페이지네이션, 정렬, 검색, 필터기능 </b>
 
4. 게시글 좋아요, 좋아요 취소
 
</div>
</details>

## 🛠 사용 기술
- API<br>
![python badge](https://img.shields.io/badge/Python-3.8-%233776AB?style=plastic&logo=python&logoColor=white)
![django badge](https://img.shields.io/badge/Django-4.0.6-%23092E20?style=plastic&logo=Django&logoColor=white)
- DB<br>
![mysql badge](https://img.shields.io/badge/MySQL-8.0.28-%234479A1?style=plastic&logo=MySQL&logoColor=white)

- 배포<br>
![aws badge](https://img.shields.io/badge/AWS-EC2-%23FF9900?style=plastic&logo=Amazon%20EC2&logoColor=white)
![aws badge](https://img.shields.io/badge/AWS-RDS-%23FF9900?style=plastic&logo=Amazon%20EC2&logoColor=white)
![docker badge](https://img.shields.io/badge/Docker-20.10.17-%232496ED?style=plastic&logo=Docker&logoColor=white)
![nginx badge](https://img.shields.io/badge/Nginx-1.23.0-%23009639?style=plastic&logo=NGINX&locoColor=white)
![gunicorn badge](https://img.shields.io/badge/Gunicorn-20.1.0-%23499848?style=plastic&logo=Gunicorn&locoColor=white)

- ETC<br>
  <img src="https://img.shields.io/badge/Git-F05032?style=plastic&logo=Git&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub-grey?style=plastic&logo=github&logoColor=181717"/>

<br>

## 🖼 ERD 모델링
![image](https://user-images.githubusercontent.com/96563183/180920189-03065cb3-ac75-4927-8930-c96b4843435c.png)

<br>

## 📜 API Document
![image](https://user-images.githubusercontent.com/96563183/180922266-663f2b66-56bf-4cb1-b136-7cc99f6f110d.png)

자세한 request, response 예시는 노션 페이지에서 확인할 수 있습니다.

<br>

## 🎪 서비스 아키텍처

### ▶ [http://43.200.91.89](http://43.200.91.89)

![image](https://user-images.githubusercontent.com/96563183/180921895-f6a4805b-6125-4346-8858-7e2ec0842daf.png)

<details>
<summary>Postman API 테스트</summary> <br>
<div markdown="1">

1. 회원가입

![image](https://user-images.githubusercontent.com/96563183/180923516-7db43cd4-66ae-4406-9898-9133a5040584.png)
 
2. 로그인

![image](https://user-images.githubusercontent.com/96563183/180923588-2909d852-f2c6-4d88-b993-7050c330f22f.png)

3. 로그아웃

![image](https://user-images.githubusercontent.com/96563183/180923679-97d9a2ec-c47e-4c21-9053-20c78e662075.png)
 
4. 토큰 재발급

![image](https://user-images.githubusercontent.com/96563183/180923735-ff70a62e-b117-429f-9571-a6c678316777.png)

5. 사용자 목록 조회

![image](https://user-images.githubusercontent.com/96563183/180923811-12441a4b-5599-48ef-9833-bc91ce26768c.png)

6. 사용자 상세 조회

![image](https://user-images.githubusercontent.com/96563183/180923883-dee3d9af-9ba9-4729-a572-e49c0aa3271c.png)

7. 사용자 정보 수정

![image](https://user-images.githubusercontent.com/96563183/180924033-dcff9172-caf2-4ea2-92a6-f75dd4f9ae28.png)

![image](https://user-images.githubusercontent.com/96563183/180924066-a0f74acd-f2a1-4ecb-a99a-b1ebb8cc7646.png)

8. 회원 탈퇴

![image](https://user-images.githubusercontent.com/96563183/180926284-3fe28d61-9f6f-45d2-928c-9ed2b56bfc66.png)

9. 게시글 목록 조회

![image](https://user-images.githubusercontent.com/96563183/180924301-e395f4b6-4718-4904-b75b-44d3fe65e921.png)

10. 게시글 작성

![image](https://user-images.githubusercontent.com/96563183/180924827-50bbe3f1-2610-4473-8df6-1d2d252b9594.png)

11. 게시글 상세 조회

![image](https://user-images.githubusercontent.com/96563183/180924871-c250b9a6-caea-47c1-bd66-5c9ef174d2c4.png)

12. 게시글 수정

![image](https://user-images.githubusercontent.com/96563183/180924946-9aaf574e-c445-4a8a-a706-d5d1d2192d16.png)

13. 게시글 상태 변경

![image](https://user-images.githubusercontent.com/96563183/180925055-d5bf4424-ee03-44c4-847b-7d88b30a4f1f.png)

![image](https://user-images.githubusercontent.com/96563183/180925101-158be26d-1388-4b14-af07-daaab1b95249.png)

![image](https://user-images.githubusercontent.com/96563183/180925132-564b4448-2f97-4b74-b805-2621f10b4a28.png)

14. 게시글 이미지 등록

![image](https://user-images.githubusercontent.com/96563183/180925269-34a5beba-187e-4bd9-91b6-f48c2817cac2.png)

15. 게시글 이미지 삭제

![image](https://user-images.githubusercontent.com/96563183/180925361-8a7b60f0-179a-45b1-a217-ad816436c928.png)

16. 게시글 좋아요

![image](https://user-images.githubusercontent.com/96563183/180925467-be8db994-4b16-4115-bd2e-82e7ac970553.png)

![image](https://user-images.githubusercontent.com/96563183/180925476-78cd165e-9d19-43e7-b8d5-acd96d3ff554.png)

17. 게시글 좋아요 취소

![image](https://user-images.githubusercontent.com/96563183/180925596-ed796e5a-cf17-48a1-b05a-fe991c66f1fa.png)

![image](https://user-images.githubusercontent.com/96563183/180925605-d64f46ab-8904-4921-8233-5bba5ca563fe.png)
 
</div>
</details>
