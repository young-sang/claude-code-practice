def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b


def power(a, b):
    return a ** b


def main():
    print("간단한 계산기")
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")
    print("5. 제곱")

    choice = input("연산을 선택하세요 (1/2/3/4/5): ").strip()
    a = float(input("첫 번째 숫자: "))
    b = float(input("두 번째 숫자: "))

    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("**", power),
    }

    if choice not in operations:
        print("잘못된 선택입니다.")
        return

    symbol, func = operations[choice]
    result = func(a, b)
    print(f"{a} {symbol} {b} = {result}")


if __name__ == "__main__":
    main()
