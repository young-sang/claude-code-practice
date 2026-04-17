"""입력값 검증 유틸리티"""


def is_number(value):
    # 주어진 값이 숫자(정수 또는 실수)로 변환 가능한지 검증한다
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def is_positive(value):
    # 주어진 숫자가 양수인지 검증한다
    if not is_number(value):
        return False
    return float(value) > 0


def is_in_range(value, min_value, max_value):
    # 주어진 숫자가 min_value 이상 max_value 이하 범위에 있는지 검증한다
    if not is_number(value):
        return False
    return min_value <= float(value) <= max_value


def is_non_empty_string(value):
    # 주어진 값이 비어있지 않은 문자열인지 검증한다
    return isinstance(value, str) and len(value.strip()) > 0


def is_valid_email(value):
    # 간단한 이메일 형식 검증 (@ 포함 여부 및 도메인 확인)
    if not isinstance(value, str):
        return False
    parts = value.strip().split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    return len(local) > 0 and "." in domain and len(domain) > 3


# === 사용 예시 ===
if __name__ == "__main__":
    print("=== 입력값 검증 유틸리티 ===\n")

    # 숫자 검증
    print(f"is_number('42')       -> {is_number('42')}")        # True
    print(f"is_number('hello')    -> {is_number('hello')}")     # False
    print(f"is_number('3.14')     -> {is_number('3.14')}")      # True

    # 양수 검증
    print(f"\nis_positive('10')    -> {is_positive('10')}")     # True
    print(f"is_positive('-5')     -> {is_positive('-5')}")      # False

    # 범위 검증
    print(f"\nis_in_range(50, 1, 100)  -> {is_in_range(50, 1, 100)}")   # True
    print(f"is_in_range(200, 1, 100) -> {is_in_range(200, 1, 100)}")    # False

    # 문자열 검증
    print(f"\nis_non_empty_string('hi')  -> {is_non_empty_string('hi')}")   # True
    print(f"is_non_empty_string('  ')   -> {is_non_empty_string('  ')}")    # False

    # 이메일 검증
    print(f"\nis_valid_email('user@example.com') -> {is_valid_email('user@example.com')}")  # True
    print(f"is_valid_email('invalid')           -> {is_valid_email('invalid')}")             # False
