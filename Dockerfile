FROM python:3.7.11-stretch

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements-dev.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements-dev.txt

COPY . .

CMD jupyter notebook --port=8888 --no-browser --ip='*' --NotebookApp.token='' --NotebookApp.password='' --allow-root