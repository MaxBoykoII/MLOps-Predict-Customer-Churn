
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --junit-xml pytest.xml

lint:
	flake8 src &&\
		flake8 tests &&\
		pylint src &&\
		pylint tests &&\
		isort src --profile black --check-only &&\
		isort tests --profile black --check-only &&\
		black src --check &&\
		black tests --check

format:
	black src &&\
		black tests &&\
		isort src --profile black
		isort tests --profile black

all: install lint format test