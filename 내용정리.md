# 

## Meetifyr

- 일정 조율을 위한 웹 서비스
- 주요기능
    - 미팅 사이트 url을 발급해 인원 초대하기
    - 각자의 이름으로 일정 조율 테이블에 row를 만들어 참가 가능.
    - 날짜별로 Free/Busy 인원 / ⭐️의 개수 / 가까운 정도  등을 활용해 우선순위 체크
    - 수정기록 확인 가능. 댓글 사용가능.

# 개발환경

## Poetry

파이썬 프로젝트의 종속성 관리용 프로그램 ( brew와 유사)

```bash
설치하기
curl -sSL [https://install.python-poetry.org](https://install.python-poetry.org/) | python3 - --version 1.8.5
```

poetry.lock / pyproject.toml 을 사용해 설치된 프로그램들의 버전을 기록하고 관리함.

## Black

협업 중 코드 스타일을 통일하여 사용하기 위한 formatter (html/css에서 사용하는 Prettier같은 느낌…?)

```bash
# 설치하기
poetry add --group=dev black==24.10.0
```

```bash
# 실행하기
run black .
poetry run black .
```

## Ruff

linter + import sorter

Ruff 설치 (Linter + Import Sorter)

```bash
poetry add --group=dev ruff==0.8.2 
```

```bash
ruff check # 체크만
ruff check --fix # 자동수정
ruff check --select (규칙이름) # 특정 규칙만 검사
ruff check --select (규칙번호) --fix . # 특정 규칙만 자동수정
```

## Git init

- git init으로 현재 디렉토리 추적 시작
- .gitignore 파일 만들기 ( .idea   **pycache**/ 등 캐시파일 제외시키기)
- commit 탭 (command+0)
- 커밋할 파일 선택 후 내용 넣기
- 커밋하기 전에 무엇을 커밋하는지 꼭 확인하기
    - 의도하지 않은 수정
    - 삭제하지 않은 print (Input, Output 이용하므로 시간이 오래걸림)
- commit(command+enter)
- commit push
    - github에서 레포지토리 만들기
    - 주소복사
    - git status로 working tree clean 확인하기
    - git remote add origin
    - git push origin main ( = 왼쪽 쉬프트*2 ⇒ push )
    

## Mypy 설치

static ← → dynamic (input 등…)

→ static type checker (정적 타입 검사 도구 = 실행하기 전에 타입을 검증함)

```bash
poetry add --group=dev mypy==1.13.0
```

```bash
poetry run mypy .
```

pydantic → poetry.lock 파일에서 확인해보기

```bash
reveal_type(a)
```

## type hint (=type annotation)

int, str, bool 

dict, set, list, tuple ⇒ collection = 다른 자료형을 담기 위해 존재

```bash
my_int: int = 1
my_str: str = "abc"

# mutable한 특성 (가변)
my_list: list[str] = ["a", "b"]
my_dict: dict[str, int] = {"a": 1}

# immutable한 특성 (불변)
my_tuple: tuple[str, str] = ('abc','def')
my_tuple: tuple[str, ...] = ('abc','def') # 개수를 모르면 ...

or_type_list: list[str|int] = ["a",1,True, False] # bool은 int의 subclass
```

inference (추론)

→ literal = 단순 값 (변수가 아님)