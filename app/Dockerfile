# official Python Image
FROM 3.11-slim

# Make work directory in container
WORKDIR /app

# Cope files in workdir
COPY . /app

# Install requirements
RUN pip install -r requirements.txt

# Run application
CMD ["python", "app.py"]
