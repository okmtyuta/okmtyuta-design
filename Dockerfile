FROM python:3
ENV PYTHONUNBUFFERED 1

# Create root directory
RUN mkdir /app
WORKDIR /app

# root
COPY ./requirements.txt ./
COPY . .

RUN pip install -r requirements.txt
