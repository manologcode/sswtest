FROM python:3.11-alpine
  
# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/latest-stable/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/latest-stable/community" >> /etc/apk/repositories
    
# install chromedriver
RUN apk --update add --no-cache
RUN apk add curl
RUN apk add chromium chromium-chromedriver
RUN apk add build-base jpeg-dev zlib-dev

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN adduser -D myuser
USER myuser

RUN python -m venv /home/myuser/venv
ENV PATH="/home/myuser/venv/bin:$PATH"

RUN pip install --upgrade pip
WORKDIR /app

COPY ./app/* /app/
ENV PATH="/home/myuser/.local/bin:$PATH" 

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./app.py"]