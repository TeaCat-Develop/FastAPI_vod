# pytest 설치
#
# def test_simple() -> None:    #pytest는 함수 이름이 test로 시작 해야 함
#     print('test')
#
# # 좌측 녹색 버튼 or ```pytest .``` 으로도 실행 가능
#     try:
#         1/0
#     except ZeroDivisionError:
#         print('error')
#
# 성공과 실패의 기준 = try-except 되지 않은 에러가 나면 실패
# 검증에 assert 사용


# 제품 코드
def add(a: int, b: int) -> int:
    return a + b


# 테스트 코드
def test_add() -> None:
    # Given: 재료를 준비
    # 버그는 경계를 좋아함.
    # int의 경우 -1,0,1
    a, b = 1, 1

    # When: 테스트 대상이 되는 함수를 호출 한다.
    result = add(a, b)  # result의 타입은 int

    # Then:
    assert result == 2  # =expression
    expression = result == 2
    if not expression:
        raise AssertionError


# 실전문제
# 예상 배송일 계산 단위 테스트
# 택배는 2영업일 이후 도착.
# 도서 산간 지역 고려하지 않음.
# 공휴일 고려하지 않음. (공공데이터 공휴일 오픈 api 제공)

from datetime import datetime, timedelta

# literal 대신 상수를 사용하는 이유
# 개발자는 배송일이 이틀임을 앎
# but 유지보수 등을 위해 2라는 숫자에 이름표를 달아줌.
# 미래의 나 자신 or 동료를 위해 배경을 알려줌.
# magic number를 쓰지 말자: 설명이 없는 특정한 값은 상수
DELIVERY_DAYS = 2


def is_holiday(day: datetime) -> bool:
    return day.weekday() > 5  # datetime의 함수. 요일을 숫자로 나타냄


def get_eta(purchase_date: datetime) -> datetime:
    current_date = purchase_date
    remaining_days = DELIVERY_DAYS

    while remaining_days > 0:
        current_date += timedelta(days=1)
        if not is_holiday(current_date):
            remaining_days -= 1

    return current_date


def test_get_eta_2023_12_01() -> None:
    result = get_eta(datetime(2023, 12, 1))
    assert result == datetime(2023, 12, 4)


def test_get_eta_2023_12_31() -> None:

    # 공휴일 정보가 없어서 1월 1일도 평일로 취급
    result = get_eta(datetime(2024, 12, 31))
    assert result == datetime(2025, 1, 2)


def test_get_eta_2024_02_28() -> None:
    result = get_eta(datetime(2024, 2, 28))
    assert result == datetime(2024, 3, 1)


def test_get_eta_2023_02_28() -> None:
    result = get_eta(datetime(2023, 2, 28))
    assert result == datetime(2023, 3, 2)
