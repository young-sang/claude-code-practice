# 간단한 대화형 계산기
# 사용자로부터 연산 종류와 두 숫자를 입력받아 결과를 출력한다.
# 다섯 가지 기본 연산(더하기, 빼기, 곱하기, 나누기, 제곱)을 지원한다.


def add(a, b):
    # 두 수를 더해 합을 반환한다.
    # 파라미터: a(float), b(float) — 피연산자 두 개
    # 반환값: a + b 의 결과
    return a + b


def subtract(a, b):
    # 첫 번째 수에서 두 번째 수를 뺀 차를 반환한다.
    # 파라미터: a(float) — 빼어지는 수(피감수), b(float) — 빼는 수(감수)
    # 반환값: a - b 의 결과
    return a - b


def multiply(a, b):
    # 두 수를 곱한 결과를 반환한다.
    # 파라미터: a(float), b(float) — 피연산자 두 개
    # 반환값: a * b 의 결과
    return a * b


def divide(a, b):
    # 첫 번째 수를 두 번째 수로 나눈 몫을 반환한다.
    # b가 0이면 ZeroDivisionError를 발생시켜 잘못된 연산을 막는다.
    # 파라미터: a(float) — 나뉘는 수(피제수), b(float) — 나누는 수(제수)
    # 반환값: a / b 의 결과(부동소수점 나눗셈)
    if b == 0:
        # 0으로 나누는 것은 수학적으로 정의되지 않으므로 예외를 던진다.
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b


def power(a, b):
    # 첫 번째 수를 두 번째 수만큼 거듭제곱한 값을 반환한다.
    # 파라미터: a(float) — 밑(base), b(float) — 지수(exponent)
    # 반환값: a ** b 의 결과
    return a ** b


def main():
    # 계산기의 메인 진입점.
    # 1) 지원하는 연산 목록을 메뉴로 출력하고
    # 2) 사용자로부터 연산 번호와 두 숫자를 입력받아
    # 3) 해당 연산을 수행한 뒤 결과를 화면에 보여준다.

    # --- 1단계: 메뉴 출력 ---
    print("간단한 계산기")
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")
    print("5. 제곱")

    # --- 2단계: 사용자 입력 수집 ---
    # strip()으로 앞뒤 공백을 제거해 "1 " 같은 입력도 "1"로 처리되도록 한다.
    choice = input("연산을 선택하세요 (1/2/3/4/5): ").strip()
    # 정수뿐 아니라 소수점 입력도 허용하기 위해 float로 변환한다.
    a = float(input("첫 번째 숫자: "))
    b = float(input("두 번째 숫자: "))

    # --- 3단계: 메뉴 번호 → (연산 기호, 연산 함수) 매핑 ---
    # 분기문(if/elif) 대신 딕셔너리를 써서 메뉴 추가/수정이 쉽도록 만들었다.
    # 키: 사용자 입력 문자열, 값: (출력용 기호, 실제 호출할 함수) 튜플
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("**", power),
    }

    # --- 4단계: 입력 검증 ---
    # 매핑에 없는 값을 넣으면 계산을 진행하지 않고 안내 후 종료한다.
    if choice not in operations:
        print("잘못된 선택입니다.")
        return

    # --- 5단계: 연산 실행 및 결과 출력 ---
    # 튜플 언패킹으로 기호와 함수를 한 번에 꺼낸다.
    symbol, func = operations[choice]
    # 선택된 함수에 두 피연산자를 전달해 결과를 계산한다.
    result = func(a, b)
    # f-string으로 "a 기호 b = 결과" 형태의 식을 사람이 읽기 쉽게 출력한다.
    print(f"{a} {symbol} {b} = {result}")


if __name__ == "__main__":
    # 이 파일을 직접 실행했을 때만 main()을 호출한다.
    # 다른 파일에서 `from calculator import add` 처럼 임포트할 때는
    # main()이 자동으로 실행되지 않도록 하기 위한 관용적 패턴.
    main()
