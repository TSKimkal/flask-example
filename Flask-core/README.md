# Core

## 파일 하나로 만드는 웹 애플리케이션

* ```hello.py``` 파일 하나만으로 웹 애플리케이션을 만든다.
* ```@app.route``` 데코레이터로 '/' URL 하나만 서비스한다.

## 애플리케이션과 실행 스크립트 분리

* ```run.py``` 실행 스크립트 파일과 hello.py 애플리케이션 파일을 분리한다.

## 애플리케이션을 패키지로 구성

* ```hello.py``` 애플리케이션 파일을 패키지로 구성한다.
* ```hello``` 폴더를 만들고 ```hello.py``` 파일의 내용이 그대로 ```__init__.py``` 파일이 된다.
* ```hello``` 폴더 안에 ```templates``` 폴더와 ```static``` 폴더를 구성하여 각각 템플릿과 css, js, 이미지 파일을 놓는다.

## 애플리케이션에 뷰 파일 분리 및 설정 클래스 정의

* ```__init__.py```에서 ```views.py```을 분리한다.
* ```app.debug``` 설정을 config 모듈 Configuration 클래스에서 정의하여 로드한다.

## 요청

### 라우팅

### 요청 메소드

요청 메소드는 GET, POST를 가장 많이 사용하고 HEAD, PUT, OPTIONS 등등이 있다.

### 요청 객체

### 데코레이터

## 응답

## 세션

## 쿠키

## 템플릿

### 변수

### 상속

### 인클루드