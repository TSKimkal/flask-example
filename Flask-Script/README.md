# Flask-Script

[Flask-Script 공식문서](https://flask-script.readthedocs.io/en/latest/)

## Flask 앱 시작하는 방법

* Config의 종류
    * 모듈
    * 클래스
* 파일 하나
* 패키지 안에 팩토리
    * 인스턴스 변수
    * 콜백 함수
    
## 주요 예제

### 01-create-app

소스: [Flask-Login/01-create-app](01-create-app)

* ```create_app``` 팩토리 함수로 ```app``` 인스턴스를 생성한다.
* ```app``` 인스턴스를 ```Manager``` 인스턴스 생성할 때 파라미터로 넘겨준다.
* ```create_app``` 메소드 안에서 뷰 라우팅 함수를 정의한다.
* 팩토리 함수로 초기화할 경우 ```db``` 같은 전역변수는 외부에서 선언하고 함수 안에서 ```init_app``` 메소드로 초기화한다.
* ```db``` 전역변수는 ```manager.py``` 파일에서 임포트하여 다른 파이썬 모듈이 사용할 수 있도록 한다. (예, ```db.create_all()```)

### 02-create-app-blueprint

소스: [Flask-Login/02-create-app-blueprint](01-create-app-blueprint)

* ```01-create-app``` 예제에서는 ```create_app``` 팩토리 함수 안에서 뷰 라우팅 함수를 정의했으나 ```create_app``` 함수가 너무 길어져서 관리하기가 어려우므로 라우팅 처리 함수를 blueprint로 별도 모듈 파일로 분리한다.
* ```create_app``` 함수 안에서 ```@app.errorhandler``` 데코레이터로 404 에러 처리 함수를 정의했다. 이 정도 함수는 시스템 전역적으로 관리하는 것이 효율적이라 판단된다.
