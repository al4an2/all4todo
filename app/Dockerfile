# official Python Image
FROM python:3.11-slim

# Make work directory in container
WORKDIR /app

# Cope files in workdir
COPY . /app

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Choose env
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Open port
EXPOSE 5000

# Run application
CMD ["python", "./app/app.py"]
