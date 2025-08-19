print('123456')
a = 123

# reveal_type(a) #mypy의 print와 같음. 파이썬 실행 전에 지워야함

my_var: list[str] = [1,2,3]
my_int: int = 123 # Literal: 값

my_str: str = "abc"
my_list: list[str] = ["abc", "def"]
# inference

# mutable(가변), immutable(불변)

my_tuple: tuple[str, str] = ("str", "str")

# 길이를 모르는 경우
my_tuple2: tuple[str, ...] = ('str','str')

my_dict: dict[str, int] = {'a':1,"b":2, "c":3}

or_type_list: list[str | int] = ["a", 1, True]
# 파이썬에서 bool은 int의 서브클래스! -> int로 치부되어 오류나지 않음.

