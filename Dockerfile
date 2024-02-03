FROM python:3.10

ENV PYTHONUNBUFFERED = 1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python -B", "manage.py", "runserver.py"]