"""설정값 관리 유틸리티"""

import json
import os


DEFAULT_CONFIG_FILE = "settings.json"


def load_config(config_file=DEFAULT_CONFIG_FILE):
    # JSON 설정 파일을 읽어서 딕셔너리로 반환한다 (파일이 없으면 빈 딕셔너리)
    if not os.path.exists(config_file):
        return {}
    with open(config_file, "r", encoding="utf-8") as f:
        return json.load(f)


def save_config(config, config_file=DEFAULT_CONFIG_FILE):
    # 딕셔너리를 JSON 설정 파일에 저장한다
    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)


def get_value(key, default=None, config_file=DEFAULT_CONFIG_FILE):
    # 설정 파일에서 특정 키의 값을 조회한다 (없으면 기본값 반환)
    config = load_config(config_file)
    return config.get(key, default)


def set_value(key, value, config_file=DEFAULT_CONFIG_FILE):
    # 설정 파일에 키-값 쌍을 저장한다 (기존 키가 있으면 덮어쓴다)
    config = load_config(config_file)
    config[key] = value
    save_config(config, config_file)


def delete_value(key, config_file=DEFAULT_CONFIG_FILE):
    # 설정 파일에서 특정 키를 삭제한다 (키가 없으면 False 반환)
    config = load_config(config_file)
    if key not in config:
        return False
    del config[key]
    save_config(config, config_file)
    return True


def list_all(config_file=DEFAULT_CONFIG_FILE):
    # 설정 파일의 모든 키-값 쌍을 출력한다
    config = load_config(config_file)
    if not config:
        print("설정이 비어 있습니다.")
        return config
    for key, value in config.items():
        print(f"  {key} = {value}")
    return config


# === 사용 예시 ===
if __name__ == "__main__":
    print("=== 설정값 관리 유틸리티 ===\n")

    test_config = "test_settings.json"

    # 설정값 저장
    set_value("app_name", "MyApp", test_config)
    set_value("version", "1.0.0", test_config)
    set_value("debug_mode", True, test_config)
    set_value("max_retry", 3, test_config)
    print("설정값 저장 완료!\n")

    # 전체 설정 출력
    print("현재 설정:")
    list_all(test_config)

    # 개별 조회
    app_name = get_value("app_name", config_file=test_config)
    print(f"\napp_name 조회: {app_name}")

    # 존재하지 않는 키 조회 (기본값 사용)
    timeout = get_value("timeout", default=30, config_file=test_config)
    print(f"timeout 조회 (기본값): {timeout}")

    # 설정값 삭제
    delete_value("debug_mode", test_config)
    print("\ndebug_mode 삭제 후:")
    list_all(test_config)

    # 테스트 파일 정리
    os.remove(test_config)
    print(f"\n테스트 파일 '{test_config}' 삭제 완료.")
