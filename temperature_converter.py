# 섭씨 ↔ 화씨 온도 변환기


def celsius_to_fahrenheit(celsius: float) -> float:
    # 섭씨 온도를 화씨 온도로 변환한다. 공식: F = C * 9/5 + 32
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    # 화씨 온도를 섭씨 온도로 변환한다. 공식: C = (F - 32) * 5/9
    return (fahrenheit - 32) * 5 / 9


def convert(value: float, unit: str) -> float:
    # 입력 단위(unit)에 따라 반대 단위로 변환한다. unit은 'C' 또는 'F'.
    unit = unit.strip().upper()
    if unit == "C":
        return celsius_to_fahrenheit(value)
    if unit == "F":
        return fahrenheit_to_celsius(value)
    raise ValueError("단위는 'C' 또는 'F'여야 합니다.")


if __name__ == "__main__":
    # 사용 예시
    print(f"25°C -> {celsius_to_fahrenheit(25):.2f}°F")   # 25°C -> 77.00°F
    print(f"100°F -> {fahrenheit_to_celsius(100):.2f}°C")  # 100°F -> 37.78°C
    print(f"convert(0, 'C') = {convert(0, 'C'):.2f}°F")    # 0°C -> 32.00°F
    print(f"convert(32, 'F') = {convert(32, 'F'):.2f}°C")  # 32°F -> 0.00°C
