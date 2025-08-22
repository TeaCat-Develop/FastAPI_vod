# #! => 쉬뱅
# import black

#!/usr/bin/env bash
set -eo pipefail

COLOR_GREEN=`tput setaf 2;`
COLOR_NC=`tput sgr0;` # No Color

echo "Starting black"
poetry run black .
echo 'Black OK'
echo 'Starting ruff'
echo run ruff check --select I --fix #isort. 린터수행
echo 'ruff OK'

echo 'starting mypy'
poetry run mypy .
echo 'mypy OK'

echo 'starting pytest with coverage'
poetry run coverage run -m pytest
poetry run coverage run report -m
poetry run coverage html
echo 'coverage OK'

echo '${COLOR_GREEN}All tests passed successfully!${COLOR_NC}'