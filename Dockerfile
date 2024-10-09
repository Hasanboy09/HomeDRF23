
FROM python:3.10-slim

WORKDIR /app

# Fayllarni konteynerga nusxalash
COPY . /app

# Kutubxonalarni o'rnatish
RUN pip install --no-cache-dir -r req.txt

# Django serverini ishga tushirish
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
