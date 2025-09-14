
FROM python:3.9-slim
RUN apt-get update && apt-get install -y postgresql-client
COPY script.py .
CMD ["python","script.py"]