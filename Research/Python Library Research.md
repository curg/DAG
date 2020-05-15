# Python Library Research

Python으로 Library를 만들기 위한 정략적인 체계 사전 조사

***
## 윤성 조사 부분

자주 사용되는 로직을 재사용하기 편리하도록 정리한 일련의 코드 집합 즉, 라이브러리를 만들기 위해 모듈과 패키지 만드는 방법을 알아야 한다. 변수, 함수, 클래스 등을 모아 놓은 스크립트 파일인 모듈을 여러 개로 묶어 패키지로 만들고, 이를 이용하여 라이브러리를 구성하도록 한다.

## Python Module
- 모든 모듈은 .py 확장자 파일로 관리된다.
- 모듈 속에 함수, 클래스, 변수가 포함될 수 있다.
- 여러 모듈을 패키지로 묶을 수 있다.
- 모듈은 ‘현재 폴더 - Python PATH (환경변수) - 파이썬 설치 경로’ 순으로 검색하여 사용할 수 있다.

**Python PATH 환경변수 확인 방법**
<img src="/lukepark327/DAG/blob/master/Research/sys%20path.png?raw=true" alt="sys path.png">

**Module을 불러와 사용하는 방법**
- import 모듈명
- import 모듈명1, 모듈명2, 모듈명3
- import 모듈명 as 모듈  // 함수 사용시 모듈.함수명(파라미터)
- from 모듈명 import 함수명  // 함수 사용시 함수명(파라미터)
- from 모듈명 import 함수명 as 함수
- from 모듈명 import *  // 모듈 내 모든 내용 포함

**Reference**

1. 모듈과 라이브러리 : https://blue-shadow.tistory.com/101
2. 파이썬 모듈 사용법 & 모듈 만들기 : https://withcoding.com/83
3. 모듈과 패키지 만들기 : https://dojang.io/mod/page/view.php?id=2447
