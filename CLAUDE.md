# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

Claude Code 사용기를 위한 파이썬 학습/실습용 스크립트 모음입니다. 각 `.py` 파일은 독립적으로 실행 가능한 단일 스크립트이며, 패키지 구조나 빌드 시스템은 없습니다. 외부 의존성 없이 표준 라이브러리만 사용합니다.

## 실행

```bash
python calculator.py            # 대화형 계산기 (사용자 입력 필요)
python temperature_converter.py # 온도 변환 예시 출력
```

단일 함수만 테스트할 때는 `python -c "from temperature_converter import convert; print(convert(25, 'C'))"` 형태로 모듈을 임포트해 호출합니다.

## 코딩 스타일 (사용자 규칙)

- 모든 함수에는 반드시 주석을 달아줘
- 변수명은 한국어 대신 영어로 작성해줘
- 코드 작성 후 항상 간단한 사용 예시도 보여줘

## 언어

- 나에게 대답할 때는 항상 한국어로 해줘
