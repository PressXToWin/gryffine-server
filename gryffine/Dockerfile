FROM python:3.9-slim

WORKDIR /app

RUN pip install gunicorn==21.2.0
COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

RUN chmod 777 /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "gryffine.wsgi"]