FROM python:3.7-alpine
WORKDIR /app
COPY backend .
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]