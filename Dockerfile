FROM ubuntu:20.04
RUN apt update && apt install -y python3
COPY . /app
WORKDIR /app
CMD ["python3", "app.py"]
