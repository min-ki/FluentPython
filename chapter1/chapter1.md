# Chapter 1

## 1.4 왜 len()은 메서드가 아닐까?

- 실용성이 순수성에 우선한다.
- len(), abs()는 파이썬 데이터 모델에서 메서드라 부르지 않는다.

## 1.5 요약
- 특별 메서드를 구현하면 사용자 정의 객체도 내장형 객체처럼 동작하게 되어, 파이썬스러운 코딩 스타일 구사 가능
- 파이썬 객체는 기본적으로 자신을 문자열 형태로 제공해야 한다. 그렇기 때문에 데이터 모델에 __repr__()과 __str__() 특별 메서드가 있다.

## 1.6 읽을거리
- 메타객체 프로토콜(metaobject protocol _ MOP) 
- 파이썬 데이터 모델도 MOP에 속한다.

## 기타
- 파이썬 데이터 모델은 파이썬 객체 모델이라고도 부른다.
- 메타객체는 언어 자체를 구현하는 객체를 말한다.
- 프로토콜은 인터페이스와 같은 의미
- 메타객체 프로토콜은 객체 모델(핵심 언어 구조체에 대한 API)의 동의어

