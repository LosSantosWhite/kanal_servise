FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY req.txt /code/
COPY credentials.json /code/
RUN pip install -r req.txt
COPY . /code/