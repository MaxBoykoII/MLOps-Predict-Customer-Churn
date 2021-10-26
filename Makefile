
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest "src/tests"

lint:
	flake8 src &&\
		pylint src &&\
		isort src --profile black --check-only &&\
		black src --check

format:
	black src

all: install lint format test