FROM python:3.7.11-stretch

WORKDIR /usr/src/app

# Prevent Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevent Python from buffering stdout and stderrr
ENV PYTHONUNBUFFERED 1

# Install make
RUN apt-get update && apt-get install make

COPY ./requirements.txt .
COPY ./Makefile .
RUN make install

COPY . .

CMD jupyter notebook --port=8888 --no-browser --ip='*' --NotebookApp.token='' --NotebookApp.password='' --allow-root