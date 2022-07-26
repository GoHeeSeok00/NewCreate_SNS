# SNS new_create.com 

### 📜 [New Create 노션 페이지](https://wool-cobalt-585.notion.site/SNS-new_create-com-84e9627ace194465ada3639f8c25d9bb) 

## 목차

1. [✅ 서비스 개요](#✅-서비스-개요)
2. [🛠 사용 기술](#🛠-사용-기술)
3. [🖼 ERD 모델링](#🖼-ERD-모델링)
4. [📜 API Document](#📜-API-Document)
5. [😎 컨벤션](#😎-컨벤션)
6. [📱 이슈, Task 관리](#📱-이슈,-Task-관리)
7. [🎪 배포](#🎪-서비스-아키텍처)


## ✅ 서비스 개요
  - 예술가(藝術家), 아티스트(Artist)의 혼을 가진 모든 사람이 자신이 new create 한 창작물, 발견 등을 공유하고 소통하는 SNS(Social Networking Service) 서비스입니다.
  - 전문성을 떠나 일상적인 생활속의 작은 창작물, 발견을 공유할 수 있습니다.
  - 자신이 만든 소중한 가치를 세상에 공유하고 싶다면 new create 하세요✨

<details>
<summary> 🚥 1차 개발기간 : 2022.07.20 ~ 2022.07.26 (7일) </summary> <br>
<div markdown="1">
  
- **이메일을 ID로 유저 회원가입**
  
- **유저 로그인 시 JTW 토큰을 발급하고 추후 사용자 인증으로 사용**
  
- **제목, 내용, 해시태그 등을 입력하여 게시글 생성**
   - 제목, 내용, 해시태그는 필수 입력사항이며, 작성자 정보는 request body에 존재하지 않고, 해당 API를 요청한 인증정보에서 추출하여 등록 
   - 해시태그는 #로 시작되고 ,로 구분되는 텍스트가 입력

- **게시글 수정**
   - 작성자만 수정 가능

- **게시글 삭제**
   - 작성자만 삭제 가능
   - 작성자는 삭제된 게시글을 다시 복구할 수 있음

- **게시글 상세보기**
   - 모든 사용자는 모든 게시물에 보기권한이 있음
   - 작성자를 포함한 사용자는 본 게시글에 좋아요를 누를 수 있음
   - 좋아요된 게시물에 다시 좋아요를 누르면 취소
   - 작성자 포함한 사용자가 게시글을 상세보기 하면 조회수 1 증가(횟수 제한 없음)

- **게시글 목록**
   - 모든 사용자는 모든 게시물에 보기권한이 있음
   - 게시글 목록에는 제목, 작성자, 해시태그, 작성일, 좋아요 수, 조회수가 포함
   - 아래 4가지 동작을 쿼리 파라미터로 구현 ex) ?search=..&orderBy=
     - Ordering (= Sorting, 정렬)
     - Searching (= 검색)
     - Filtering (= 필터링)
     - Pagination (= 페이지 기능)
</div>
</details>

🚥 업데이트(고도화, 리펙토링)

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

## 😎 컨벤션

### 🍀 커밋 컨벤션
```
# --- 제목(title) - 50자 이내로 ---
# <타입(type)> <제목(title)>
# 예시(ex) : Docs : #1 README.md 수정
# --- 본문(content) - 72자마다 줄바꾸기  ---
# 예시(ex) :
# - Workflow
# 1. 커밋 메시지에 대한 문서 제작 추가.
# 2. commit message docs add.
# --- 꼬리말(footer) ---
# <타입(type)> <이슈 번호(issue number)>
# 예시(ex) : Fix #122
# --- COMMIT END ---
# <타입> 리스트
#   Init    : 초기화
#   Feat    : 기능추가
#   Add     : 내용추가
#   Update  : 기능 보완 (업그레이드)
#   Fix     : 버그 수정
#   Refactor: 리팩토링
#   Style   : 스타일 (코드 형식, 세미콜론 추가: 비즈니스 로직에 변경 없음)
#   Docs    : 문서 (README.md, ignore파일 추가(Add), 수정, 삭제)
#   Test    : 테스트 (테스트 코드 추가, 수정, 삭제: 비즈니스 로직에 변경 없음)
#   Chore   : 기타 변경사항 (빌드 스크립트 수정 등)
#   Rename  : 이름(파일명, 폴더명, 변수명 등)을 수정하거나 옮기는 작업만인 경우
#   Remove  : 파일을 삭제하는 작업만 수행한 경우  
# ------------------
#     제목 첫 글자를 대문자로
#     제목은 명령문으로
#     제목 끝에 마침표(.) 금지
#     제목과 본문을 한 줄 띄워 분리하기
#     본문은 "어떻게" 보다 "무엇을", "왜"를 설명한다.
#     본문에 여러 줄의 메시지를 작성할 땐 "-" 혹은 "번호"로 구분
# ------------------ 
```

### ☘ 코드 컨벤션

- Class
  - Pascal case
- Model
  - snake case
- Function
  - snake case
- Variables
  - snake case
 
 ### 주석처리
 - Class, Function의 주석은 class, function 하단에 작성
   - 주석으로 Assignee 작성
 - API의 경우, 상단에 주석으로 url 주소 작성
 ```
 <example>
 
# api/v1/jobs/<int:id>/run
class JobTaskView(APIView):
  """
  Assignee : 김아무개
  """

  """
  여러 줄인 경우
  이와같이 주석을
  답니다.
  너무 길지 않게 작성합니다.
  """
```

### 🌿 브렌치 전략
- gitflow
```
main : 기준이 되는 브랜치로 제품을 배포하는 브랜치
develop : 개발 브랜치로 개발자들이 이 브랜치를 기준으로 각자 작업한 기능들을 Merge
feature : 단위 기능을 개발하는 브랜치로 기능 개발이 완료되면 develop 브랜치에 Merge
release : 배포를 위해 master 브랜치로 보내기 전에 먼저 QA(품질검사)를 하기위한 브랜치
```
<br>

## 📱 이슈, Task 관리
![image](https://user-images.githubusercontent.com/96563183/181050230-9e6995f1-26b7-4ff4-98d8-e13fed8ae9a2.png)

<br>

## 🎪 배포

### ▶ [http://43.200.91.89](http://43.200.91.89)

### 🎨 서비스 아키텍처

![image](https://user-images.githubusercontent.com/96563183/180921895-f6a4805b-6125-4346-8858-7e2ec0842daf.png)

<details>
<summary>🚀 Postman API 테스트</summary> <br>
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
