"""로그 기록 유틸리티"""

import datetime
import os


# 로그 레벨 상수 정의
LOG_LEVEL_DEBUG = "DEBUG"
LOG_LEVEL_INFO = "INFO"
LOG_LEVEL_WARNING = "WARNING"
LOG_LEVEL_ERROR = "ERROR"

# 로그 레벨 우선순위 (숫자가 클수록 심각)
LEVEL_PRIORITY = {
    LOG_LEVEL_DEBUG: 0,
    LOG_LEVEL_INFO: 1,
    LOG_LEVEL_WARNING: 2,
    LOG_LEVEL_ERROR: 3,
}

# 기본 설정
DEFAULT_LOG_FILE = "app.log"
DEFAULT_MIN_LEVEL = LOG_LEVEL_DEBUG


def get_timestamp():
    # 현재 시각을 'YYYY-MM-DD HH:MM:SS' 형식의 문자열로 반환한다
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_message(level, message):
    # 로그 메시지를 '[시각] [레벨] 메시지' 형식으로 포맷팅한다
    timestamp = get_timestamp()
    return f"[{timestamp}] [{level}] {message}"


def write_log(message, level=LOG_LEVEL_INFO, log_file=DEFAULT_LOG_FILE, min_level=DEFAULT_MIN_LEVEL):
    # 로그 메시지를 파일과 콘솔에 기록한다 (min_level 이상만 출력)
    if LEVEL_PRIORITY.get(level, 0) < LEVEL_PRIORITY.get(min_level, 0):
        return
    formatted = format_message(level, message)
    print(formatted)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(formatted + "\n")


def debug(message, log_file=DEFAULT_LOG_FILE):
    # DEBUG 레벨 로그를 기록한다
    write_log(message, LOG_LEVEL_DEBUG, log_file)


def info(message, log_file=DEFAULT_LOG_FILE):
    # INFO 레벨 로그를 기록한다
    write_log(message, LOG_LEVEL_INFO, log_file)


def warning(message, log_file=DEFAULT_LOG_FILE):
    # WARNING 레벨 로그를 기록한다
    write_log(message, LOG_LEVEL_WARNING, log_file)


def error(message, log_file=DEFAULT_LOG_FILE):
    # ERROR 레벨 로그를 기록한다
    write_log(message, LOG_LEVEL_ERROR, log_file)


def clear_log(log_file=DEFAULT_LOG_FILE):
    # 로그 파일의 내용을 초기화한다
    if os.path.exists(log_file):
        with open(log_file, "w", encoding="utf-8") as f:
            f.write("")
        print(f"로그 파일 '{log_file}'이 초기화되었습니다.")


# === 사용 예시 ===
if __name__ == "__main__":
    print("=== 로그 기록 유틸리티 ===\n")

    test_log = "test.log"
    clear_log(test_log)

    debug("디버그 메시지입니다", test_log)
    info("서버가 시작되었습니다", test_log)
    warning("메모리 사용량이 80%를 초과했습니다", test_log)
    error("데이터베이스 연결에 실패했습니다", test_log)

    print(f"\n로그가 '{test_log}' 파일에 저장되었습니다.")
