FROM python:3.10

WORKDIR /app

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY ./python/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the app
EXPOSE 5000

# Copy the files in
COPY ./python .

# Start it up
CMD ["flask", "run"]
