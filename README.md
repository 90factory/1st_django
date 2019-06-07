# 개요

청와대 청원 중 정부의 답변을 받지는 못했지만 많은 사람들의 관심을 받은 청원을 재조명하고 토론할 수 있는 온라인 서비스

# Django Server

1. 터미널창에 pip install django 명령어를 입력하여 django 프레임워크를 설치한다.

2. requirements.txt에 있는 파이썬 라이브러리들을 버전에 맞게 설치한다.

3. 설치 후 django 프레임워크가 설치된 디렉토리(manage.py파일이 있는)로 경로를 이동한 후 터미널창에 python manage.py runserver 자신의IP주소:8000(예시 : 192.168.1.3:8000) 입력

# 클래스 구조
![꺼청 아키텍처(api서버)](https://user-images.githubusercontent.com/41987854/58460233-2d69c880-8168-11e9-99c6-8ca5f9c692fe.jpg)

˚ Crawler Class: 청와대 웹사이트에서 꺼청사이트에 구현할 데이터들이 어떠한 것인지 기준을 잡고 적합한 데이터들을 수집하는 크롤러 모듈

˚ Model Class: 수집한 청와대 데이터들을 저장, 업데이트, 원하는 api데이터 형식에 맞게 가져오는 기능

˚ Controller Class: 노드(메인서버)에서 원하는 요청에 따라 rest api 방식으로 필요한 api 제공

## Crawler Class

˚ cheongwadae_crawling
 - 청와대웹사이트에서 꺼청사이트의 UI에 보여질 청와대데이터API를 수집하는 크롤링을 구현

˚ setpage
 - 청와대웹사이트의 필요한 데이터를 가진 url들중 쿼리스트링패턴을 파악하여 페이지별로 설정할수 있도록 구현

## Model class

˚ insertinitialdata
  - 새로 수집된 데이터들을 DB에 삽입함
  
˚ updatedata
  - 수집된 데이터들을 DB에 최신화(업데이트)함

˚ entirequery
  - 노드(메인서버)에서 HTTP통신의 GET요청이오면 수집한 전체데이터들을 가져옴 
  
˚ top5query
  - 노드(메인서버)에서 HTTP통신의 GET요청이오면 수집한 데이터들중 상위5개 데이터들만 가져옴
  
˚ keywordquery
  - 노드(메인서버)에서 HTTP통신의 GET방식으로 데이터를 요청하면 알맞은 데이터(단어검색)를 가져옴 
  
˚ historyquery
  - 노드(메인서버)에서 HTTP통신의 GET방식으로 데이터를 요청하면 알맞은 데이터(회원의 히스토리)를 가져옴

## Controller Class

※ 서버가 동작하는 상태에서 매일 정각마다 데이터가 최신화되도록 스케줄러를 구현함

˚ entirecontroller
 - url을 rest에 알맞게 지정하여 전체데이터 api를 제공
 
˚ top5controller
 - url을 rest에 알맞게 지정하여 상위5개데이터 api를 제공
 
˚ keywordcontroller
 - url을 rest에 알맞게 지정하여 http get요청에 원하는 단어에 일치하는 데이터 api를 제공(요청방식이 다를경우 제공하지 않음)
 
˚ historycontroller
 - url을 rest에 알맞게 지정하여 http get요청에 원하는 히스토리(회원 접속기록) 데이터 api를 제공(요청방식이 다를경우 제공하지 않음)
 
 # 데이터베이스 구조
  ![K-001](https://user-images.githubusercontent.com/41987854/58462772-80924a00-816d-11e9-9544-8afc11edeb31.jpg)

˚ mydb라는 Database 안에 Crawler라는 collection이 있고 청원한건당 document로 정함 

˚ filed는 _id(한 document의 고유번호), 번호, 분류, 제목, 링크, 청원만료일, 참여인원 을 기준으로 정함


