
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest "src/tests" --junit-xml pytest.xml

lint:
	flake8 src &&\
		pylint src &&\
		isort src --profile black --check-only &&\
		black src --check

format:
	black src &&\
		isort src --profile black

all: install lint format test